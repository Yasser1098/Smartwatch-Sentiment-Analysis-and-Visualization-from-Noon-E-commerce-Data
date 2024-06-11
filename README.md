# 📊 Smartwatch Sentiment Analysis and Visualization from Noon E-commerce Data

## Project Overview

This project involves scraping data about smartwatches from the Noon e-commerce website using Python. The primary goal was to perform sentiment analysis on customer comments and visualize the results using Power BI.

## 🛠️ Libraries and Tools Used

- **Python**: For data scraping and sentiment analysis
  - `BeautifulSoup` and `requests`: For web scraping
  - `Selenium` and `webdriver_manager`: For handling dynamic web pages
  - `asyncio` and `aiohttp`: For asynchronous web requests
  - `TextBlob`: For sentiment analysis
- **Excel**: For initial data cleaning
- **Power BI**: For data visualization

## 📈 Process

### 1. Data Scraping

The data was scraped from Noon using Python scripts. The libraries `BeautifulSoup` and `requests` were used to handle static content, while `Selenium` and `webdriver_manager` were utilized for dynamic content. Additionally, asynchronous web requests were managed using `asyncio` and `aiohttp` to improve efficiency.

### 2. Data Cleaning

After scraping the data, it was exported to Excel for initial cleaning. This step involved:
- Removing duplicates
- Handling missing data
- Removing unnecessary columns

### 3. Sentiment Analysis

Sentiment analysis was performed on the scraped comments using the `TextBlob` library. This allowed us to classify comments as positive, negative, or neutral.

### 4. Data Visualization

The cleaned data and sentiment analysis results were imported into Power BI to create a comprehensive dashboard. The dashboard provided insights such as:
- The strong correlation between price and ratings
- The distribution of sentiment (most comments were neutral)
- Identification of the top-rated smartwatch on the website at the time of analysis

## 🔍 Insights

- **Price and Ratings**: There is a strong relationship between the price of smartwatches and their ratings.
- **Sentiment Distribution**: The majority of the comments are neutral, with a balanced mix of positive and negative comments.
- **Top Smartwatch**: The analysis revealed the top-rated smartwatch available on Noon during the data collection period.

## 📌 Conclusion

This project demonstrates skills in web scraping, data cleaning, sentiment analysis, and data visualization. By combining these techniques, we can derive meaningful insights from e-commerce data, which can be valuable for businesses looking to understand customer feedback and product performance.

![image](https://github.com/Yasser1098/Smartwatch-Sentiment-Analysis-and-Visualization-from-Noon-E-commerce-Data/assets/129599070/08671256-996c-4378-9f1d-aac82abd6f95)

