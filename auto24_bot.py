import requests
from bs4 import BeautifulSoup

AUTO24_URL = 'https://www.auto24.ee/kasutatud/nimekiri.php?ae=1&ak=0'

# Example of previous listings (for illustration purposes)
previous_listings = []

def scrape_auto24():
    response = requests.get(AUTO24_URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        listings = soup.find_all('div', class_='row nimekiri-kandet')

        new_listings = []
        for listing in listings:
            title_element = listing.find('div', class_='make_model_text')
            price_element = listing.find('div', class_='hinta_text')

            if title_element and price_element:
                title = title_element.get_text().strip()
                price = price_element.get_text().strip()
                new_listings.append({'title': title, 'price': price})

        # Compare new_listings with previous_listings
        new_listings_to_send = []
        for new_listing in new_listings:
            if new_listing not in previous_listings:
                new_listings_to_send.append(new_listing)
                # Add new_listing to previous_listings
                previous_listings.append(new_listing)

        return new_listings_to_send

if __name__ == '__main__':
    new_listings = scrape_auto24()
    if new_listings:
        for listing in new_listings:
            print(f"New listing: {listing['title']} - {listing['price']}")
