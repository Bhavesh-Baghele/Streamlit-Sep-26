import streamlit as st
import yfinance as yf
import datetime as dt
st.title("Stock Price Analyzer")
st.subheader("This application helps you to analyse the stock price of a company")

# ticker=yf.Ticker("MSFT")
symbol = st.text_input(
    "Enter a stock ticker",
    value="MSFT"
)
ticker = yf.Ticker(symbol)
# ticker_data=ticker.history(period="1mo")

start_date = st.date_input(
    "Start date",
    dt.date.today()
)

end_date = st.date_input(
    "End date",
    dt.date.today()
)

ticker_data = ticker.history(
    start = start_date,
    end = end_date
)

st.write(ticker_data)

st.subheader("Price Movement")
st.line_chart(ticker_data["Close"])

st.header("Volume Movement")
st.bar_chart(ticker_data["Volume"])