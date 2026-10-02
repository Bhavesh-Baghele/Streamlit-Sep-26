import streamlit as st
import yfinance as yf
st.title("Stock Price Analyzer")
st.subheader("This application helps you to analyse the stock price of a company")

ticker=yf.Ticker("MSFT")
ticker_data=ticker.history(period="1mo")
st.write(ticker_data)
