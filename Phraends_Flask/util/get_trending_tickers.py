import pandas as pd

def get_top_trending_tickers(csv_file_path):
    # Read the CSV file into a DataFrame
    data = pd.read_csv(csv_file_path)
    
    # Assuming the column name is 'Tickers'
    ticker_counts = data['Ticker'].value_counts()
    
    # Get the top 5 trending tickers
    top_tickers = ticker_counts.head(5)
    
    return top_tickers.index.tolist()