🚀 Project Overview
This project demonstrates an end-to-end data lifecycle. It features an autonomous "Harvester" that polls Google Finance for various asset classes (Stocks, Crypto, Commodities), cleans the data, and persists it into a MySQL database. The second phase utilizes JupyterLab to perform Time-Series analysis and visualization.

🛠️ Tech Stack

- Language: Python 3.x
- Libraries: BeautifulSoup4, Requests (Web Scraping)
- Database: MySQL (Relational Data Storage)
- Analysis: Pandas (Data Manipulation)
- Visualization: Seaborn, Matplotlib (Time-Series Plotting)

📁 Project Structure

- harvester.py: The automation script that scrapes data and pushes to MySQL.
-analysis_dashboard.ipynb: Jupyter Notebook for data extraction and visualization.
- requirements.txt: List of necessary Python libraries.

🌟 Key Features

- Autonomous Ingestion: Uses a while True loop with scheduled time.sleep intervals to collect data without manual intervention.
- Relational Persistence: Implements a structured MySQL schema to handle historical price data and timestamps.
- Data Cleaning Pipeline: Handles complex currency strings ($, ₹) and numerical formatting (commas) to ensure mathematical accuracy.
- Technical Indicators: Implements a 3-period Rolling Moving Average to smooth price volatility and identify trends.
- Dynamic Filtering: Built-in logic to handle high-variance assets (like Bitcoin) separately from traditional stocks for better visual clarity.

🔧 Setup & Installation

1.Clone the repo:
  git clone https://github.com/Ehsaan08-ai/market-data-pipeline.git

2. Install dependencies:
    pip install -r requirements.txt

3. Database Configuration:

   - Ensure MySQL is running.
   - Create a database named market_tracker.
   - Create a table stock_prices with columns: id, ticker, price, and timestamp.

4. Database Configuration:

   - Ensure MySQL is running.
   - Create a database named market_tracker.
   - Create a table stock_prices with columns: id, ticker, price, and timestamp.

5. Run the Python file:
    - python index.py

