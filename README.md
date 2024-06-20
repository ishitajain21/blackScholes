# Black Scholes Options Pricing with Transaction Fees

This Python script implements the Black Scholes Options Pricing Formula, with the addition of accounting for transaction fees, a condition not included in the original algorithm. It retrieves stock and options data from the Alpha Vantage API and calculates the ideal option value based on the Black Scholes model, adjusting for transaction costs.

## Features

- Retrieves historical stock prices and options data from the Alpha Vantage API
- Calculates the current stock price from the daily open and close prices
- Determines the number of days until the option expiration date
- Implements the Black Scholes formula to calculate the ideal option value
- Accounts for transaction fees by multiplying the ideal option value by a constant factor
- Displays the calculated ideal option values along with relevant option details

## Requirements

- Python 3.x
- Required Python packages: `streamlit`, `requests`, `pandas`, `numpy`, `matplotlib`, `yfinance`, `scipy`

## Usage

1. Install the required Python packages: `pip install streamlit requests pandas numpy matplotlib yfinance scipy`
2. Obtain an API key from [Alpha Vantage](https://www.alphavantage.co/) (a free API key is available)
3. Replace the `KEY` variable in the code with your Alpha Vantage API key
4. Run the script: `streamlit run <script_name>.py`
5. Enter the stock ticker symbol and your Alpha Vantage API key when prompted
6. The script will retrieve and process the data, displaying the ideal option values and relevant details in a tabular format

## File Structure

- `<script_name>.py`: The main Python script containing the code implementation
- `options.csv`: A CSV file containing the retrieved options data
- `prices.csv`: A CSV file containing the retrieved stock price data

## Note

This implementation assumes European-style options (not American-style options). The model by Robert Merton can be incorporated in further iterations to handle American-style options.

## License

This project is licensed under the [MIT License](LICENSE).
