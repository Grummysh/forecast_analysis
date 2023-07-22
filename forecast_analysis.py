import gspread
import pandas as pd

# Function to get the top 3 product categories with negative forecasted quantities
def get_top3_negative_forecasted_products(data):
    # Filter the data to include only products with negative forecasted quantities
    negative_forecasted_data = data[data['Forecasted Quantity'] < 0]

    # Group the data by product categories and calculate the total forecasted quantity for each category
    category_forecasts = negative_forecasted_data.groupby('Product Category').sum()

    # Sort the categories by forecasted quantities in descending order
    sorted_categories = category_forecasts.sort_values(by='Forecasted Quantity', ascending=False)

    # Get the top 3 product categories with negative forecasted quantities
    top3_categories = sorted_categories.head(3).index.tolist()

    return top3_categories

def main():
    # Connect to the Google Sheets document using the service account JSON file
    filename = 'C:\\Users\\grumm\\Downloads\\focused-bridge-393601-425247c08206.json'
    gc = gspread.service_account(filename=filename)

    # Specify the spreadsheet key and worksheet name
    spreadsheet_key = '1IwjamCfqQP6JRzs2hooqVMrd5gm5xQqamD-Z31JJ_8Y'
    worksheet_name = 'product.template.csv'

    # Open the worksheet
    worksheet = gc.open_by_key(spreadsheet_key).worksheet(worksheet_name)

    # Get the data from the worksheet as a Pandas DataFrame
    data = worksheet.get_all_values()
    df = pd.DataFrame(data[1:], columns=data[0])

    # Convert numeric columns to numeric data types
    df['Forecasted Quantity'] = pd.to_numeric(df['Forecasted Quantity'])

    # Get the top 3 product categories with negative forecasted quantities
    top3_negative_forecasted_categories = get_top3_negative_forecasted_products(df)

    # Print the result
    print("Top 3 Product Categories with Negative Forecasted Quantities:")
    print(top3_negative_forecasted_categories)

if __name__ == "__main__":
    main()