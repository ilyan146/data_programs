import requests
import selectorlib
from datetime import datetime
import pandas as pd
import streamlit as st
import plotly.express as px
import sqlite3


URL = "https://programmer100.pythonanywhere.com/"

connection = sqlite3.connect("temperature.db")


def temp_scrape(url):
    response = requests.get(url)
    content = response.text
    return content

def temp_extract(content):
    extractor = selectorlib.Extractor.from_yaml_file("temp_extract.yaml")
    temp_value = extractor.extract(content)["temp"]
    date = extractor.extract(content)["date"]
    return temp_value, date


now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


def temp_store(temp_value):
    #with open("temp_data.txt","a") as file:
       #file.write(f"{dt_string}, {temp_value}" + "\n")
    row = dt_string,temp_value
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperatures VALUES(?,?)", row)
    connection.commit()


def temp_read():
    #with open("temp_data.txt", "r") as file:
       #return file.readlines()
    cursor = connection.cursor()
    data = cursor.execute("SELECT Date,Temperatures FROM temperatures")
    data = cursor.fetchall()
    #temperature = cursor.execute("SELECT Temperatures FROM temperatures")
    #temperature = cursor.fetchall()
    return data


def temp_read2():
    df = pd.read_csv("temp_data.txt")
    return df


if __name__ == "__main__":
    content = temp_scrape(URL)
    temp_value, date = temp_extract(content)
    print(temp_extract(content))
    print(date)
    print(temp_value)
    temp_store(temp_value)
    df = temp_read2()
    print(df["date_time"])
    data1 = temp_read()
    print(data1)
    dates = [i[0]for i in data1]
    temp = [i[1] for i in data1]
    #fig = px.line(x=df["date_time"], y=df[" temperature"], labels={"x": "Date", "y": "Temperature (C)"})
    fig = px.line(x=dates, y=temp, labels={"x": "Date", "y": "Temperature (C)"})
    st.plotly_chart(fig)