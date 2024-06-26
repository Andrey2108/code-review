import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from config import *


class WebScraper:
    def __init__(self):
        self.client = MongoClient("mongodb", 27017)
        self.db = self.client.matrix12
        self.collection = self.db.products

    def get_html(self, url, params=""):
        r = requests.get(url, headers=headers, params=params)
        return r

    def get_content(self, html):
        soup = BeautifulSoup(html, "html.parser")
        items = soup.find_all("div", class_="catalog_item")
        cards = []

        for item in items:
            card = {
                "Название": item.find("div", class_="catalog_item_info").get_text(
                    strip=True
                ),
                "Ссылка": host
                + item.find("div", class_="catalog_item_layer").find("a").get("href"),
                "Цена": item.find("span", class_="editor-pane-num").get_text(
                    strip=True
                ),
            }
            cards.append(card)

        card_documents = []
        for card in cards:
            if not self.collection.find_one(card):
                card_documents.append(card)

        if card_documents:
            self.collection.insert_many(card_documents)

        return card_documents
