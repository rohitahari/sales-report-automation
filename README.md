# Sales Report Automation Tool

A Python automation tool that monitors a folder for new sales CSV files and automatically generates Excel reports with summary statistics and product-level sales analysis.

## Features

- Monitors a folder for incoming CSV files
- Automatically processes sales data
- Generates Excel reports
- Provides summary metrics and product-level analysis
- Handles multiple files automatically

## Tech Stack

- Python
- pandas
- watchdog
- openpyxl

## Project Structure

sales-report-automation/
│
├── report_tool.py
├── requirements.txt
├── README.md
│
├── data
│   └── sample_sales.csv
│
└── reports

## Installation

Install dependencies:

pip install -r requirements.txt

## Run the Automation Tool

python report_tool.py

## Usage

1. Start the tool
<<<<<<< HEAD
2. Drop CSV files into the `data` folder
3. Reports will automatically appear in the `reports` folder

## Example Output

The generated Excel file includes:

Sheet 1: Summary
- Total Sales
- Top Product

Sheet 2: Sales by Product

## Example CSV Format

Product,Sales  
Laptop,1200  
Phone,800  
Tablet,500  





## Example Workflow

1. Start the automation tool.
2. Drop a CSV file into the `data` folder.
3. The tool automatically processes the file.
4. An Excel report is generated in the `reports` folder.

## Example Output

The Excel report includes:

- Summary sheet
- Sales by Product analysis
>>>>>>> 2cf71b8 (Improve automation tool structure and logging)
