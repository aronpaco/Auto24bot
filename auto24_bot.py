import requests
from bs4 import BeautifulSoup
import time
import telegram

# Set up your Telegram bot
bot_token = '6489915608:AAFxCr4yNb5DyicAZNnnywvE0U3HfFAy7BM'
chat_id = '2021133565'
bot = telegram.Bot(token=bot_token)

# URL of the car listings page
url = 'https://www.auto24.ee/kasutatud/nimekiri.php?bn=2&a=101102&ae=1&af=50&otsi=otsi&ak=0'

# Keep track of already seen listings to avoid duplicates
seen_listings = set()

def get_new_listings():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    listings = soup.find_all('div', class_='result-row')

    new_listings = []
    for listing in listings:
        listing_id = listing['id']
        if listing_id not in seen_listings:
            new_listings.append(listing)
            seen_listings.add(listing_id)
    return new_listings
    print("Returning new listings...")

def send_telegram_message(message):
    bot.send_message(chat_id=chat_id, text=message)
    print("Sending Telegram message...")

def main():
    while True:
        new_listings = get_new_listings()
        if new_listings:
            message = "New car listings:\n"
            for idx, listing in enumerate(new_listings, start=1):
                link = listing.find('a', class_='h2')['href']
                message += f"{idx}. {link}\n"
            send_telegram_message(message)
        time.sleep(30)
        print("Waited for 30 seconds...")

if __name__ == '__main__':
    main()
