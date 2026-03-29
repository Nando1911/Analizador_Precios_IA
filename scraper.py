import requests
from bs4 import BeautifulSoup

def get_data():
    url = "https://books.toscrape.com/"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("article", class_="product_pod")

    data = []

    for product in products:
        name = product.h3.a["title"]
        price = product.find("p", class_="price_color").text
        
        data.append({
            "name": name,
            "price": price
        })

    return data