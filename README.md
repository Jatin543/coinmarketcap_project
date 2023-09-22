# CoinMarketCap Data Scraper and Viewer

This Django project allows you to scrape cryptocurrency data from CoinMarketCap and view it in a tabular format on a web page. It includes a web scraper that periodically fetches data and sends it to Django via HTTP POST requests, a Django app to handle the data, and a webpage for viewing the data in a table.


## Setup
  **Clone the Repository**

   git clone https://github.com/Jatin543/coinmarketcap_project.git
   cd coinmarketcap-scraper

 **Install Dependencies**
	python -m venv venv
	source venv/bin/activate  # On Windows, use: venv\Scripts\activate
	pip install -r requirements.txt

**Database Configuration**
python manage.py makemigrations
python manage.py migrate

**Run the Scraper**
python coinscrapper.py


**Start the Django Development Server**
python manage.py runserver

Access the web page to view the cryptocurrency data at http://127.0.0.1:8000/coinmarketcap/get_latest_data/


