# Weather Web Scraper with the use of a SQL Database
## A web scraper application that utilizes realtime changing data by keeping log in a database and providing visualization.
The functioning application monitors the global average temperature and updates on a set interval, storing all data in a SQL database using SQLite. Plotly Express is used to visualize the changes on Streamlit.
The application is made with shows sample codes to do the following.

* Uses an online API for constantly updating temperature data and scrapes the necessary global temperature using selectorlib library.
* Establishes connection with SQL database using SQLite3.
* The SQL database is updated with incoming data and queried as necessary.
* Data visualization conducted on a streamlit using plotly express libraries.

## Sample of how the app looks.


## SQL Database example.

## Possible Additions
The app can include data for each continent/countries and demonstrate the possible countries that contribute to the higher or lower global temperatures.