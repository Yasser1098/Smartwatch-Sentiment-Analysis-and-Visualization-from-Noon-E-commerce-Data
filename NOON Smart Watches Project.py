#!/usr/bin/env python
# coding: utf-8

# # Importing In use libraries

# In[ ]:


import csv
from bs4 import BeautifulSoup
import datetime
import requests
from time import sleep
from selenium import webdriver
from urllib.parse import urljoin
import csv
import asyncio
from aiohttp import ClientSession
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urljoin
from textblob import TextBlob


# # Scraping The Data out of the Website

# In[ ]:


L_of_Headers = ['Product Title', 'Rating', 'Number of Raters', 'P-product price', 'link to the product',
                        'Model of the product', 'P-Review 1', 'P-Review 2', 'P-Review 3', 'P-Review 4', 'P-Review 5']
csv_file_path = 'C:/Users/HP/Downloads/Sales-Data-Analysis-main/Noon-data.csv'
# Write headers to the CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(L_of_Headers)
    
    
for i in range(1, 45):      ##Page range from which data are going to be collected
    
    url = f'https://www.noon.com/uae-en/search/?limit=50&originalQuery=smart%20watch&page={i}&q=smart%20watch&searchDebug=false&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    ## Here we use Selenium instead of requests as noon as a website is dynamic website it is not static which means the data
    ## is being rendered by Java script
    # Use Selenium to open the webpage
    driver = webdriver.Chrome()  # You need to have ChromeDriver installed and in your PATH
    driver.get(url)

    # Give the page some time to load dynamically rendered content
    ##ztime.sleep(5)

    # Get the updated HTML content after JavaScript execution
    html_content = driver.page_source

    # Close the Selenium webdriver
    driver.quit()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    ## Here we searched for the class that represents a product inh a page and found that it is a Span and have
    ## word productContainer in it's name
    # Find all span elements with class 'productContainer' within the body
    span_elements = soup.body.find_all('span', {'class': 'productContainer'})
    ################################################################################################################
    for z in range(0,51):
        
        product = span_elements[z]

        # Extract title
        title_element = product.find('div', {'data-qa': 'product-name'})
        title = title_element.text if title_element is not None else "Title not found"

        # Extract rating
        rating_element = product.find('div', {'class': 'sc-363ddf4f-0 bXxLif'})
        rating = rating_element.text if rating_element is not None else "Rating not found"

        # Extract number of raters
        number_of_raters_element = product.find('span', {'class': 'sc-363ddf4f-5 bBssC'})
        number_of_raters = number_of_raters_element.text if number_of_raters_element is not None else "Number of raters not found"

        product_price= product.find('strong',{'class':'amount'}).text
        price_currency= product.find('span',{'class':'currency'}).text
        product_price= f'{product_price} {price_currency}'
        link_element = product.find('a', {'class': product})
        link= link_element.get('href')
        full_url= urljoin('https://www.noon.com',link)

        product_page= requests.get(full_url,headers=header)
        product_soup= BeautifulSoup(product_page.content)

        watch_model_element1= product_soup.find('td', text= 'Model Name')
        watch_model= watch_model_element1.find_next('td').text if watch_model_element1 is not None else "No model for this watch"
        #watch_model= watch_model_element2.text if watch_model_element is not None else "No model for this watch"

        driver2 = webdriver.Chrome()
        driver2.get(full_url)

        page_source = driver2.page_source

        # Close the Selenium webdriver
        driver2.quit()

        # Use BeautifulSoup to parse the page source
        product_soup = BeautifulSoup(page_source, 'html.parser')



        comment_soup = product_soup.find_all('div', {"class": "sc-4cfd0356-5 gcvqxj"})

        if comment_soup:
            if 1 <= len(comment_soup) < 2:
                l_fstincomm_element = comment_soup[0].find('div', {'class': 'sc-4cfd0356-3 gmOris'})
                l_fstincomm = l_fstincomm_element.text if l_fstincomm_element is not None else ""

                l_sndincomm_element = comment_soup[0].find('div', {'class': 'sc-4cfd0356-11 hSOIxg'})
                l_sndincomm= l_sndincomm_element.text if l_sndincomm_element is not None else ""
                concatenated_commentsl = f"{l_fstincomm}-{l_sndincomm}"        
                ll_fstincomm = "NO"
                ll_sndincomm= "NO"
                concatenated_commentsll = f"{ll_fstincomm}-{ll_sndincomm}" 
                lll_fstincomm = "NO"
                lll_sndincomm= "NO"
                concatenated_commentslll = f"{lll_fstincomm}-{lll_sndincomm}" 
                llll_fstincomm = "NO"
                llll_sndincomm= "NO"
                concatenated_commentsllll = f"{llll_fstincomm}-{llll_sndincomm}" 
                lllll_fstincomm = "NO"
                lllll_sndincomm= "NO"
                concatenated_commentslllll = f"{lllll_fstincomm}-{lllll_sndincomm}" 

            elif 2 <= len(comment_soup) < 3:
                l_fstincomm_element = comment_soup[0].find('div', {'class': 'sc-4cfd0356-3 gmOris'})
                l_fstincomm = l_fstincomm_element.text if l_fstincomm_element is not None else ""

                l_sndincomm_element = comment_soup[0].find('div', {'class': 'sc-4cfd0356-11 hSOIxg'})
                l_sndincomm= l_sndincomm_element.text if l_sndincomm_element is not None else ""
                concatenated_commentsl = f"{l_fstincomm}-{l_sndincomm}"
                ll_fstincomm_element = comment_soup[1].find('div', {'class': 'sc-4cfd0356-3 gmOris'})
                ll_fstincomm = ll_fstincomm_element.text if ll_fstincomm_element is not None else ""

                ll_sndincomm_element = comment_soup[1].find('div', {'class': 'sc-4cfd0356-11 hSOIxg'})
                ll_sndincomm= ll_sndincomm_element.text if ll_sndincomm_element is not None else ""
                concatenated_commentsll = f"{ll_fstincomm}-{ll_sndincomm}"        
                lll_fstincomm = "NO"
                lll_sndincomm= "NO"
                concatenated_commentslll = f"{lll_fstincomm}-{lll_sndincomm}" 
                llll_fstincomm = "NO"
                llll_sndincomm= "NO"
                concatenated_commentsllll = f"{llll_fstincomm}-{llll_sndincomm}" 
                lllll_fstincomm = "NO"
                lllll_sndincomm= "NO"
                concatenated_commentslllll = f"{lllll_fstincomm}-{lllll_sndincomm}" 
            elif 3 <= len(comment_soup) < 4:
                l_fstincomm_element = comment_soup[0].find('div', {'class': 'sc-4cfd0356-3 gmOris'})
                l_fstincomm = l_fstincomm_element.text if l_fstincomm_element is not None else ""

                l_sndincomm_element = comment_soup[0].find('div', {'class': 'sc-4cfd0356-11 hSOIxg'})
                l_sndincomm= l_sndincomm_element.text if l_sndincomm_element is not None else ""
                concatenated_commentsl = f"{l_fstincomm}-{l_sndincomm}"
                ll_fstincomm_element = comment_soup[1].find('div', {'class': 'sc-4cfd0356-3 gmOris'})
                ll_fstincomm = ll_fstincomm_element.text if ll_fstincomm_element is not None else ""

                ll_sndincomm_element = comment_soup[1].find('div', {'class': 'sc-4cfd0356-11 hSOIxg'})
                ll_sndincomm= ll_sndincomm_element.text if ll_sndincomm_element is not None else ""
                concatenated_commentsll = f"{ll_fstincomm}-{ll_sndincomm}"
                lll_fstincomm_element = comment_soup[2].find('div', {'class': 'sc-4cfd0356-3 gmOris'})
                lll_fstincomm = lll_fstincomm_element.text if lll_fstincomm_element is not None else ""

                lll_sndincomm_element = comment_soup[2].find('div', {'class': 'sc-4cfd0356-11 hSOIxg'})
                lll_sndincomm= lll_sndincomm_element.text if lll_sndincomm_element is not None else ""
                concatenated_commentslll = f"{lll_fstincomm}-{lll_sndincomm}"        
                llll_fstincomm = "NO"
                llll_sndincomm= "NO"
                concatenated_commentsllll = f"{llll_fstincomm}-{llll_sndincomm}" 
                lllll_fstincomm = "NO"
                lllll_sndincomm= "NO"
                concatenated_commentslllll = f"{lllll_fstincomm}-{lllll_sndincomm}" 

            elif 4 <= len(comment_soup) < 5:
                l_fstincomm_element = comment_soup[0].find('div', {'class': 'sc-4cfd0356-3 gmOris'})
                l_fstincomm = l_fstincomm_element.text if l_fstincomm_element is not None else ""

                l_sndincomm_element = comment_soup[0].find('div', {'class': 'sc-4cfd0356-11 hSOIxg'})
                l_sndincomm= l_sndincomm_element.text if l_sndincomm_element is not None else ""
                concatenated_commentsl = f"{l_fstincomm}-{l_sndincomm}"
                ll_fstincomm_element = comment_soup[1].find('div', {'class': 'sc-4cfd0356-3 gmOris'})
                ll_fstincomm = ll_fstincomm_element.text if ll_fstincomm_element is not None else ""

                ll_sndincomm_element = comment_soup[1].find('div', {'class': 'sc-4cfd0356-11 hSOIxg'})
                ll_sndincomm= ll_sndincomm_element.text if ll_sndincomm_element is not None else ""
                concatenated_commentsll = f"{ll_fstincomm}-{ll_sndincomm}"
                lll_fstincomm_element = comment_soup[2].find('div', {'class': 'sc-4cfd0356-3 gmOris'})
                lll_fstincomm = lll_fstincomm_element.text if lll_fstincomm_element is not None else ""

                lll_sndincomm_element = comment_soup[2].find('div', {'class': 'sc-4cfd0356-11 hSOIxg'})
                lll_sndincomm= lll_sndincomm_element.text if lll_sndincomm_element is not None else ""
                concatenated_commentslll = f"{lll_fstincomm}-{lll_sndincomm}"
                llll_fstincomm_element = comment_soup[3].find('div', {'class': 'sc-4cfd0356-3 gmOris'})
                llll_fstincomm = llll_fstincomm_element.text if llll_fstincomm_element is not None else ""

                llll_sndincomm_element = comment_soup[3].find('div', {'class': 'sc-4cfd0356-11 hSOIxg'})
                llll_sndincomm= llll_sndincomm_element.text if llll_sndincomm_element is not None else ""
                concatenated_commentsllll = f"{llll_fstincomm}-{llll_sndincomm}"        
                lllll_fstincomm = "NO"
                lllll_sndincomm= "NO"
                concatenated_commentslllll = f"{lllll_fstincomm}-{lllll_sndincomm}" 

            elif len(comment_soup) >= 5:
                l_fstincomm_element = comment_soup[0].find('div', {'class': 'sc-4cfd0356-3 gmOris'})
                l_fstincomm = l_fstincomm_element.text if l_fstincomm_element is not None else ""

                l_sndincomm_element = comment_soup[0].find('div', {'class': 'sc-4cfd0356-11 hSOIxg'})
                l_sndincomm= l_sndincomm_element.text if l_sndincomm_element is not None else ""
                concatenated_commentsl = f"{l_fstincomm}-{l_sndincomm}"
                ll_fstincomm_element = comment_soup[1].find('div', {'class': 'sc-4cfd0356-3 gmOris'})
                ll_fstincomm = ll_fstincomm_element.text if ll_fstincomm_element is not None else ""

                ll_sndincomm_element = comment_soup[1].find('div', {'class': 'sc-4cfd0356-11 hSOIxg'})
                ll_sndincomm= ll_sndincomm_element.text if ll_sndincomm_element is not None else ""
                concatenated_commentsll = f"{ll_fstincomm}-{ll_sndincomm}"
                lll_fstincomm_element = comment_soup[2].find('div', {'class': 'sc-4cfd0356-3 gmOris'})
                lll_fstincomm = lll_fstincomm_element.text if lll_fstincomm_element is not None else ""

                lll_sndincomm_element = comment_soup[2].find('div', {'class': 'sc-4cfd0356-11 hSOIxg'})
                lll_sndincomm= lll_sndincomm_element.text if lll_sndincomm_element is not None else ""
                concatenated_commentslll = f"{lll_fstincomm}-{lll_sndincomm}"
                llll_fstincomm_element = comment_soup[3].find('div', {'class': 'sc-4cfd0356-3 gmOris'})
                llll_fstincomm = llll_fstincomm_element.text if llll_fstincomm_element is not None else ""

                llll_sndincomm_element = comment_soup[3].find('div', {'class': 'sc-4cfd0356-11 hSOIxg'})
                llll_sndincomm= llll_sndincomm_element.text if llll_sndincomm_element is not None else ""
                concatenated_commentsllll = f"{llll_fstincomm}-{llll_sndincomm}"
                lllll_fstincomm_element = comment_soup[4].find('div', {'class': 'sc-4cfd0356-3 gmOris'})
                lllll_fstincomm = lllll_fstincomm_element.text if lllll_fstincomm_element is not None else ""

                lllll_sndincomm_element = comment_soup[4].find('div', {'class': 'sc-4cfd0356-11 hSOIxg'})
                lllll_sndincomm= lllll_sndincomm_element.text if lllll_sndincomm_element is not None else ""
                concatenated_commentslllll = f"{lllll_fstincomm}-{lllll_sndincomm}"
        else:
            # If there are no comments
            concatenated_commentsl= "NO"
            concatenated_commentsll= "NO"
            concatenated_commentslll= "NO"
            concatenated_commentsllll= "NO"
            concatenated_commentslllll= "NO"
            


        #### Print the results
        # print(f"P-Product Title: {title}")
        # print(f"P-Rating: {rating}")
        # print(f"P-Number of Raters: {number_of_raters}")
        # print(f'P-product price: {product_price}')
        # print(f'P-The link to the product: {full_url}')
        # print(f'P-Model of the product: {watch_model}')
        # print(f'P-Review 1: {concatenated_commentsl}')
        # print(f'P-Review 2: {concatenated_commentsll}')
        # print(f'P-Review 3: {concatenated_commentslll}')
        # print(f'P-Review 4: {concatenated_commentsllll}')
        # print(f'P-Review 5: {concatenated_commentslllll}')

        L_of_Headers= ['Product Title','Rating','Number of Raters','P-product price','link to the product',\
                       'Model of the product','P-Review 1','P-Review 2','P-Review 3','P-Review 4','P-Review 5']

        L_of_Data= [title,rating,number_of_raters,product_price,full_url,watch_model,concatenated_commentsl,\
                    concatenated_commentsll,concatenated_commentslll,concatenated_commentsllll,concatenated_commentslllll]
        ## thsi runs only once then using the adding to the CSV syntax so it runs at the begining then Hashed
        csv_file_path = 'C:/Users/HP/Downloads/Noon-data.csv'

        ## Write headers to the CSV file
        # with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        #     csv_writer = csv.writer(csv_file)
        #     csv_writer.writerow(L_of_Headers)
        with open(csv_file_path, 'a+', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(L_of_Data)


# # Applying Sentiment Analysis

# In[ ]:


df_sent= pd.read_excel(r'C:\Users\HP\Downloads\Sales-Data-Analysis-main\NOON.xlsx',sheet_name='Noon-data')

df_sent['Sentiment_Polarity'] = 0.0

# Apply sentiment analysis using TextBlob on each review column
review_columns = ['P-Review 1', 'P-Review 2', 'P-Review 3']

for col in review_columns:
    # Add a check for empty or missing reviews
    df_sent[col + '_Sentiment'] = df_sent[col].apply(lambda x: TextBlob(str(x)).sentiment.polarity if str(x).strip() != '' else 0.0)

    # Update the overall sentiment polarity for each product
    df_sent['Sentiment_Polarity'] += df_sent[col + '_Sentiment']

# Create a new column for sentiment category based on polarity
df_sent['Sentiment_Category'] = pd.cut(df_sent['Sentiment_Polarity'],
                                   bins=[-float('inf'), -1, -0.5, 0.5, 1, float('inf')],  # Adjusted for extreme values
                                   labels=['Very Negative', 'Negative', 'Neutral', 'Positive', 'Very Positive'])


# In[ ]:


df_sent.to_excel('non-with-sentiment.xlsx',index=False)

