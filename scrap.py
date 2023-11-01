import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.amazon.com/Lenovo-Tab-P11-Plus-1st/dp/B09B17DVYR/ref=sr_1_2?qid=1695021332&rnid=16225007011&s=computers-intl-ship&sr=1-2&th=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    # title_element = soup.find('span', id='productTitle')
    # title = title_element.get_text(strip=True) if title_element else 'Title not found'
    
    # price_element = soup.find('span', class_='a-price-whole')
    # price = price_element.get_text(strip=True) if price_element else 'Price not found'
    
    # description_element = soup.find('div', id='productDescription')
    # description = description_element.get_text() if description_element else 'Description not found'
    
    # image_element = soup.find('div', id='imgTagWrapperId')
    # if image_element:
    #     image_url = image_element.find('img')['src']
    # else:
    #     image_url = 'Image link not found'
    
    # rating_element = soup.find('span', class_='reviewCountTextLinkedHistogram')
    # rating = rating_element['title'] if rating_element else 'Rating not found'
    
    # reviews_element = soup.find('span', id='acrCustomerReviewText')
    # reviews = reviews_element.get_text(strip=True) if reviews_element else 'Number of reviews not found'
    
    # with open('product_data.csv', mode='w', newline='') as csv_file:
    #     writer = csv.writer(csv_file)
    #     writer.writerow(['Title', 'Price', 'Description', 'Image Link', 'Rating', 'Number of Reviews'])
    #     writer.writerow([title, price, description, image_url, rating, reviews])
    
    # print('Data has been saved to product_data.csv')
else:
    print(str(response.status_code)+' - Error loading the page')