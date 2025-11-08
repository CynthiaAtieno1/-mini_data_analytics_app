import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from modules.data_loader import load_csv
from modules.processor import clean_data, categorize_spenders, mean_purchase_by_category, CustomerAnalysis
from modules.visualization import plot_sales_by_category, plot_purchase_histogram

BASE = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE, 'data', 'sales_data.csv')
OUTPUT_DIR = os.path.join(BASE, 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    df = load_csv(DATA_PATH)
    df = clean_data(df)
    df = categorize_spenders(df)
    mean_by_cat = mean_purchase_by_category(df)
    ca = CustomerAnalysis(df)
    total = ca.total_sales()
    sales_cat = ca.sales_by_category()
    age_dist = ca.age_distribution()
    mean_by_cat.to_csv(os.path.join(OUTPUT_DIR,'mean_by_category.csv'), index=False)
    sales_cat.to_csv(os.path.join(OUTPUT_DIR,'sales_by_category.csv'), index=False)
    with open(os.path.join(OUTPUT_DIR,'summary.txt'),'w') as f:
        f.write(f'Total Sales: {total}\n')
        f.write('Sales by Category:\n')
        f.write(sales_cat.to_string(index=False))
        f.write('\n\nAge distribution:\n')
        f.write(age_dist.to_string())
    plot_sales_by_category(df, os.path.join(OUTPUT_DIR,'sales_by_category.png'))
    plot_purchase_histogram(df, os.path.join(OUTPUT_DIR,'purchase_histogram.png'))
    print('Analysis complete. Outputs saved in', OUTPUT_DIR)

if __name__ == '__main__':
    main()
