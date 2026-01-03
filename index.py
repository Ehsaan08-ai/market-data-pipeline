import time
import requests
from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import Error

URL = "https://www.google.com/finance/quote/AAPL:NASDAQ"

stocks_to_track = {
    "MSFT": "https://www.google.com/finance/quote/MSFT:NASDAQ",
    "TSLA": "https://www.google.com/finance/quote/TSLA:NASDAQ",
    "BTC":  "https://www.google.com/finance/quote/BTC-INR",
    "GOLD": "https://www.google.com/finance/quote/GOLD:NYSE"
}

#print(response.status_code)

#if response.status_code == 200:
#print(response.headers)


def connect_to_mysql():
    try:
        # 1. Establish the connection
        connection = mysql.connector.connect(
        host='127.0.0.1',  
        user='root',       
        password='Ehsaan@08', 
        port=3306,  
        database='market_tracker'
        )
        
        if connection.is_connected():
            mycursor = connection.cursor()

            for ticker, URL in stocks_to_track.items():
                response = requests.get(URL)
                soup = BeautifulSoup(response.text, "lxml")
                Price = soup.select_one("div.YMlKec.fxKbKc").getText()
                new_Price = Price.replace('$', '').replace(',','')
                
                current_cleaned_prices = float(new_Price)

                sql = "INSERT INTO stock_prices (ticker, price) VALUES (%s, %s)"
                val = (ticker, current_cleaned_prices)
                mycursor.execute(sql,val)
            
            connection.commit()

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

while True:
    connect_to_mysql()
    print("Scrapping Complete! Sleeping for 10 Minutes.")
    time.sleep(600)