import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from symbols import get_tradeable_symbols
from price import store_price_history
from integrated import get_cointegrated_pairs
import json 

if __name__ == "__main__":

    # Get list of symbols
    print("Getting symbols...")
    sym_response = get_tradeable_symbols()

    # Construct and save price history
    print("Constructing and saving price data to JSON...")
    if len(sym_response) > 0:
        store_price_history(sym_response)

    # Find Cointegrated pairs
    print("Calculating co-integration...")
    with open("1_price_list.json") as json_file:
        price_data = json.load(json_file)
        if len(price_data) > 0:
            coint_pairs = get_cointegrated_pairs(price_data)
      
