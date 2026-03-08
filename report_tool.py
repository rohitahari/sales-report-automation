import pandas as pd
import os
import time
import argparse
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


parser = argparse.ArgumentParser(description="CSV Sales Automation Tool")
parser.add_argument("--input", default="data", help="Input folder")
parser.add_argument("--output", default="reports", help="Output folder")

args = parser.parse_args()

INPUT_FOLDER = args.input
OUTPUT_FOLDER = args.output

os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def process_file(path):
    try:
        df = pd.read_csv(path)

        columns = [c.lower() for c in df.columns]

        if "sales" in columns:
            sales_col = df.columns[columns.index("sales")]
        elif "amount" in columns:
            sales_col = df.columns[columns.index("amount")]
        else:
            print("No sales column found.")
            return

        if "product" in columns:
            product_col = df.columns[columns.index("product")]
        elif "item" in columns:
            product_col = df.columns[columns.index("item")]
        else:
            print("No product column found.")
            return

        df[sales_col] = df[sales_col].astype(str).str.replace(",", "").astype(float)

        total_sales = df[sales_col].sum()

        product_sales = df.groupby(product_col)[sales_col].sum()

        top_product = product_sales.idxmax()

        summary_data = {
            "Metric": ["Total Sales", "Top Product"],
            "Value": [total_sales, top_product]
        }

        summary_df = pd.DataFrame(summary_data)

        filename = os.path.basename(path)

        output_file = os.path.join(
            OUTPUT_FOLDER,
            f"report_{filename.replace('.csv','.xlsx')}"
        )

        with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
          summary_df.to_excel(writer, sheet_name="Summary", index=False)

        product_sales.reset_index().to_excel(
        writer,
        sheet_name="Sales by Product",
        index=False
    )

        logging.info(f"Report generated: {output_file}")

    except Exception as e:
        print(f"Error processing {path}: {e}")


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith(".csv"):
            time.sleep(1)
            process_file(event.src_path)


print("Automation system running")
print(f"Watching folder: {INPUT_FOLDER}")

event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, INPUT_FOLDER, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
