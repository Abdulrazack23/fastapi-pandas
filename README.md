FastAPI Data Generation and Export Example

This repository contains a Python script demonstrating how to use FastAPI to generate fake user data and export it to a CSV file, which can be downloaded directly from the browser.
FastAPI

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. It's designed to be easy to use and learn, while also being highly efficient.
Faker

Faker is a Python library that generates fake data for you. Whether you need to bootstrap your database, create good-looking XML documents, fill in placeholder text for UI mockups, or anonymize data taken from a production service, Faker is for you.
Random

The random module in Python provides functions for generating random numbers. In this script, we use it to generate random integers for user age, mood rating, steps taken, active minutes, and sleep duration.
Pandas

Pandas is a fast, powerful, flexible, and easy-to-use open-source data analysis and manipulation library built on top of the Python programming language. It provides data structures like Series and DataFrame, which are essential for working with structured data efficiently.

    Series: A one-dimensional labeled array capable of holding any data type. It is similar to a Python list or dictionary and is the building block of a DataFrame.
    DataFrame: A two-dimensional, size-mutable, and heterogeneous tabular data structure with labeled axes (rows and columns). It is similar to a spreadsheet or SQL table.
    read_csv(): A function in Pandas used to read data from a CSV file into a DataFrame.
    to_csv(): A method in Pandas used to write a DataFrame to a CSV file.

Starlette

Starlette is a lightweight ASGI framework/toolkit for building high-performance asyncio services. It is used under the hood by FastAPI for handling responses.
Running the Script

To run the script:

    Install the required packages by running pip install -r requirements.txt.
    Run the script using uvicorn main:app --reload.
    Access the root URL (http://127.0.0.1:8000/) in your browser.
    The script will generate the CSV file and return it as a downloadable file in the browser.

Feel free to explore and modify the script according to your needs
