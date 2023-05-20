# Weather Web Scraper with the use of a SQL Database
## A web scraper application that utilizes realtime changing data by keeping log in a database and providing visualization.
The functioning application monitors the global average temperature and updates on a set interval, storing all data in a SQL database using SQLite. Plotly Express is used to visualize the changes on Streamlit.
The application is shows sample codes to do the following.

* Uses an online API for constantly updating temperature data and scrapes the necessary global temperature using selectorlib library.
* Establishes connection with SQL database using SQLite3.
* The SQL database is updated with incoming data and queried as necessary.
* Data visualization conducted on a streamlit using plotly express libraries.

## Sample of how the app looks.
![image](https://github.com/ilyan146/data_programs/assets/123881167/ff3b0512-fe06-4ef3-8b29-f1ef4c1017b0)

## SQL Database example.
![image](https://github.com/ilyan146/data_programs/assets/123881167/0d800372-077b-4c7e-9e07-dc896f9cfb6a)

## Possible Additions
The app can include data for each continent/countries and demonstrate the possible countries that contribute to the higher or lower global temperatures.
