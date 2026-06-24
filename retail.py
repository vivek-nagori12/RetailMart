import pandas as pd
import numpy as np
import sqlite3


def run_pipeline():
    try:
        # Load Files
        sales = pd.read_csv("sales_data.csv")
        products = pd.read_csv("products.csv")
        stores = pd.read_csv("stores.csv")

        print("Sales Data")
        print(sales.head())

        print("\nProducts Data")
        print(products.head())

        print("\nStores Data")
        print(stores.head())

        # Missing Values
        print("\nMissing Values in Sales Data")
        print(sales.isnull().sum())

        print("\nMissing Values in Products Data")
        print(products.isnull().sum())

        print("\nMissing Values in Stores Data")
        print(stores.isnull().sum())

        # Remove Duplicates
        duplicate_count = sales.duplicated().sum()
        sales = sales.drop_duplicates()

        print("\nDuplicate Rows Removed:", duplicate_count)

        # Data Cleaning
        sales["quantity"] = sales["quantity"].fillna(0)

        sales = sales.dropna(subset=["amount"])
        sales = sales.dropna(subset=["product_id", "sale_date"])

        sales["sale_date"] = pd.to_datetime(sales["sale_date"])
        sales["amount"] = sales["amount"].astype(float)

        print("\nCleaned Sales Data Shape:")
        print(sales.shape)

        # Merge Data
        final_df = pd.merge(sales, products, on="product_id")
        final_df = pd.merge(final_df, stores, on="store_id")

        # Revenue Column
        final_df["total_revenue"] = (
            final_df["quantity"] * final_df["price"]
        )

        print("\nRevenue Statistics")
        print("Mean Revenue:", np.mean(final_df["total_revenue"]))
        print("Max Revenue:", np.max(final_df["total_revenue"]))
        print("Min Revenue:", np.min(final_df["total_revenue"]))

        # Revenue By City
        city_revenue = (
            final_df.groupby("city")["total_revenue"]
            .sum()
            .sort_values(ascending=False)
        )

        print("\nRevenue By City")
        print(city_revenue)

        # Database Connection
        conn = sqlite3.connect("retail.db")

        final_df.to_sql(
            "retail_sales",
            conn,
            if_exists="replace",
            index=False
        )

        print("\nData Loaded Successfully")

        # Top 3 Products
        query1 = """
        SELECT product_name,
               SUM(quantity) AS total_qty
        FROM retail_sales
        GROUP BY product_name
        ORDER BY total_qty DESC
        LIMIT 3;
        """

        result = pd.read_sql(query1, conn)

        print("\nTop 3 Best Selling Products")
        print(result)

        # Revenue Per Store Per Day
        query2 = """
        SELECT store_name,
               sale_date,
               SUM(total_revenue) AS revenue
        FROM retail_sales
        GROUP BY store_name, sale_date
        ORDER BY revenue DESC;
        """

        result2 = pd.read_sql(query2, conn)

        print("\nRevenue Per Store Per Day")
        print(result2)

        # Summary Report
        print("\nSUMMARY REPORT")

        print("Total Transactions:", len(final_df))

        print("Total Revenue:",
              final_df["total_revenue"].sum())

        print("Top Selling City:",
              city_revenue.idxmax())

        print("Top Selling Product:",
              result.iloc[0]["product_name"])

        conn.close()

    except FileNotFoundError:
        print("One or more CSV files are missing.")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    run_pipeline()