import requests
from bs4 import BeautifulSoup
import json


def parse():
    url = "https://quotes.toscrape.com"
    next_page = ""

    authors_json = []
    quotes_json = []
    author_list = []

    while True:
        page_url = url + next_page
        response = requests.get(page_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            blocks = soup.find_all("div", class_="quote")

            for block in blocks:
                author_dict = {}
                quote_dict = {}

                author_name = block.find("small", class_="author").text
                if not author_name in author_list:
                    author_url = url + block.find("a")["href"]
                    author_page = requests.get(author_url)
                    author = BeautifulSoup(author_page.text, "lxml")

                    author_dict.update({"fullname": author_name})
                    author_dict.update(
                        {
                            "born_date": author.find(
                                "span", class_="author-born-date"
                            ).text
                        }
                    )
                    author_dict.update(
                        {
                            "born_location": author.find(
                                "span", class_="author-born-location"
                            ).text
                        }
                    )
                    author_dict.update(
                        {
                            "description": author.find(
                                "div", class_="author-description"
                            ).text.strip()
                        }
                    )
                    author_list.append(author_name)
                    authors_json.append(author_dict)

                quote_dict.update(
                    {
                        "tags": block.find("div", class_="tags")
                        .find("meta", class_="keywords")["content"]
                        .split(",")
                    }
                )
                quote_dict.update({"author": author_name})
                quote_dict.update({"quote": block.find("span", class_="text").text})
                quotes_json.append(quote_dict)

            try:
                next_page = soup.find("li", class_="next").find("a")["href"]
            except:
                break

    with open("data/authors.json", "w", encoding="utf-8") as fh:
        json.dump(authors_json, fh, ensure_ascii=False, indent=2)

    with open("data/quotes.json", "w", encoding="utf-8") as fh:
        json.dump(quotes_json, fh, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    parse()
