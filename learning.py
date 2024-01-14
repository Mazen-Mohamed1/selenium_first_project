from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv

user_input = input('Enter the product: ').replace(' ', '%20')

# getting Google chrome
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

url = f'https://www.noon.com/egypt-en/search/?q={user_input}&gclid=Cj0KCQiAhomtBhDgARIsABcaYylLRnSwoSrKZbbdAAkG5BRn1KaidgQ2f6hww7II-QZy8OIkzKj5l4AaAnbbEALw_wcB&utm_campaign=C1000151355N_eg_en_web_searchxxexactandphrasexxbrandpurexx08082022_noon_web_c1000088l_acquisition_sembranded_&utm_medium=cpc&utm_source=C1000088L'

def main(link):
    products_details = []

    # gathering the Data
    browser.get(link)
    product_prices = browser.find_elements('class name', 'amount')
    discount = browser.find_elements('class name', 'discount')
    product_name = browser.find_elements('css selector', '.sc-a080589e-21')

    for i in range(len(product_prices)):
        print(product_prices[i].text, product_name[i].text)

        if i < len(discount):
            discount_text = discount[i].text
        else:
            discount_text = 'No Discount'

        print(discount_text)

        products_details.append({
            'PRODUCT PRICE': product_prices[i].text,
            'Discount': discount_text,
            'Brand Name': product_name[i].text
        })

    # creating the csv file
    path = 'D:/projects/products_details.csv'
    keys = products_details[0].keys()
    with open(path, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(products_details)

main(url)