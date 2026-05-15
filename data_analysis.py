import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def analyze_sales_data():
    # Create sample dataset
    np.random.seed(42)
    data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "Sales": np.random.randint(10000, 50000, 12),
        "Expenses": np.random.randint(5000, 30000, 12),
        "Customers": np.random.randint(100, 500, 12)
    }

    df = pd.DataFrame(data)

    # Calculate profit
    df["Profit"] = df["Sales"] - df["Expenses"]

    # Summary statistics
    print("=== Sales Summary ===")
    print(f"Total Sales: ${df['Sales'].sum():,}")
    print(f"Total Profit: ${df['Profit'].sum():,}")
    print(f"Best Month: {df.loc[df['Sales'].idxmax(), 'Month']}")
    print(f"Average Monthly Sales: ${df['Sales'].mean():,.0f}")

    # Save summary to CSV
    df.to_csv("sales_summary.csv", index=False)
    print("\nData saved to sales_summary.csv")

    # Create charts
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))

    # Sales vs Expenses chart
    axes[0].plot(df["Month"], df["Sales"], marker="o", label="Sales", color="blue")
    axes[0].plot(df["Month"], df["Expenses"], marker="o", label="Expenses", color="red")
    axes[0].set_title("Monthly Sales vs Expenses")
    axes[0].legend()
    axes[0].grid(True)

    # Profit bar chart
    axes[1].bar(df["Month"], df["Profit"], color="green")
    axes[1].set_title("Monthly Profit")
    axes[1].grid(True)

    plt.tight_layout()
    plt.savefig("sales_chart.png")
    print("Chart saved to sales_chart.png")

    return df

if __name__ == "__main__":
    analyze_sales_data()
