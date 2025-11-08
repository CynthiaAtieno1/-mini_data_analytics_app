
import matplotlib.pyplot as plt

def plot_sales_by_category(df, outpath):
    agg = df.groupby('Product_Category')['Purchase_Amount'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(6,4))
    agg.plot(kind='bar', ax=ax)
    ax.set_title('Total Sales by Category')
    ax.set_ylabel('Total Sales')
    fig.tight_layout()
    fig.savefig(outpath)
    plt.close(fig)

def plot_purchase_histogram(df, outpath):
    fig, ax = plt.subplots(figsize=(6,4))
    ax.hist(df['Purchase_Amount'].dropna(), bins=20)
    ax.set_title('Histogram of Purchase Amounts')
    ax.set_xlabel('Purchase Amount')
    ax.set_ylabel('Count')
    fig.tight_layout()
    fig.savefig(outpath)
    plt.close(fig)
