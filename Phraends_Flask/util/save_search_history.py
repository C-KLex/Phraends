import pandas as pd
import os

def save_search_history(ticker):
    # Load existing search history if the CSV file exists
    
    phraends_folder = os.path.join(os.getcwd(), 'Phraends_Flask')
    data_folder = os.path.join(phraends_folder, 'util')

    search_history_csv = os.path.join(data_folder, 'search_history.csv')
    search_history_df = pd.read_csv(search_history_csv, header=0,usecols=["Ticker"])

    csv_file = 'search_history.csv'
    if os.path.exists(search_history_csv):
        search_history_df = pd.read_csv(search_history_csv, header=0,usecols=["Ticker"])
    else:
        search_history_df = pd.DataFrame(columns=['Ticker'])

    # Append the new search entry to the DataFrame
    search_history_df = search_history_df.append({'Ticker': ticker}, ignore_index=True)

    # Save the updated DataFrame to the CSV file
    search_history_df.to_csv(search_history_csv, index=False)