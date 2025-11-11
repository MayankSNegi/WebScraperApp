import requests
from bs4 import BeautifulSoup
from typing import List, Dict
import charset_normalizer


class BookScraper:
    """Handles web scraping from books.toscrape.com (now with auto-encoding detection)"""

    BASE_URL = "https://books.toscrape.com"
    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    @staticmethod
    def scrape_books(max_pages: int = 5) -> List[Dict]:
        """
        Scrapes book data from the target website.
        Automatically detects encoding for global compatibility.
        """
        books = []

        try:
            for page in range(1, max_pages + 1):
                url = f"{BookScraper.BASE_URL}/catalogue/page-{page}.html"
                print(f"📖 Scraping page {page}...")

                # Fetch page content
                response = requests.get(url, headers=BookScraper.HEADERS, timeout=10)
                response.raise_for_status()

                # 🧠 Auto-detect correct encoding
                detected = charset_normalizer.from_bytes(response.content).best()
                encoding = detected.encoding if detected else "utf-8"
                response.encoding = encoding
                print(f"🌍 Detected encoding for page {page}: {encoding}")

                # Parse HTML using detected encoding
                soup = BeautifulSoup(response.text, "html.parser")

                book_articles = soup.find_all("article", class_="product_pod")
                if not book_articles:
                    print(f"⚠️  No books found on page {page}")
                    continue

                print(f"✅ Found {len(book_articles)} books on page {page}")

                for article in book_articles:
                    try:
                        # Extract title
                        h3_tag = article.find("h3")
                        a_tag = h3_tag.find("a") if h3_tag else None
                        title = a_tag["title"].strip() if a_tag and "title" in a_tag.attrs else None
                        if not title:
                            continue

                        # Extract price (keep symbol)
                        price_tag = article.find("p", class_="price_color")
                        price = price_tag.get_text(strip=True) if price_tag else "N/A"

                        # Extract availability
                        availability_tag = article.find("p", class_="instock availability")
                        availability = availability_tag.get_text(strip=True) if availability_tag else "Unknown"

                        # Extract rating
                        rating_tag = article.find("p", class_="star-rating")
                        rating = "N/A"
                        if rating_tag and "class" in rating_tag.attrs and len(rating_tag["class"]) > 1:
                            rating = rating_tag["class"][1]

                        # Add book record
                        books.append({
                            "title": title,
                            "price": price,
                            "availability": availability,
                            "rating": rating
                        })

                    except Exception as e:
                        print(f"⚠️  Error parsing book: {e}")
                        continue

        except Exception as e:
            print(f"❌ Error during scraping: {e}")
            return []

        print(f"\n✅ Successfully scraped {len(books)} total books")
        return books
