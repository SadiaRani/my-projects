from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

# Load HTML file
with open("Amazon2.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all divs with specified class
products = soup.find_all("div", class_="puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v2v5pwx3nl8aar2aoxf0782v1pf s-latency-cf-section puis-card-border")

# Initialize lists to store data
product_names = []
product_prices = []
product_reviews = []

# Iterate over each product
for product in products:
    # Find product name
    name_tag = product.find("span", class_="a-size-medium a-color-base a-text-normal")
    product_name = name_tag.text.strip() if name_tag else ""
    product_names.append(product_name)

    # Find product price
    price_tag = product.find("span", class_="a-price-whole")
    product_price = price_tag.text.strip() if price_tag else ""
    product_prices.append(product_price)

    # Find product reviews
    reviews_tag = product.find("span", class_="a-size-base s-underline-text")
    product_review = reviews_tag.text.strip() if reviews_tag else ""
    product_reviews.append(product_review)

# Create a DataFrame
data = {
    "Product_name": product_names,
    "Product_price": product_prices,
    "Product_reviews": product_reviews
}
df = pd.DataFrame(data)

# Write DataFrame to Excel file
df.to_excel("Amazon_products2.xlsx", index=False)
