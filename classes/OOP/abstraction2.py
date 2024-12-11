from abc import ABC, abstractmethod

class WebScrapper(ABC):
    @abstractmethod
    def scrape(self, url: str):
        pass
    
class HTMLScrapper(WebScrapper):
    def scrape(self, url: str):
        # Code to scrape HTML content
        print(f"Scraping HTML content from {url}")
        
class JSONScrapper(WebScrapper):
    def scrape(self, url: str):
        # Code to scrape JSON data
        print(f"Scraping JSON data from {url}")

# Using polymorphism
scrapers = [HTMLScrapper(), JSONScrapper()]

for scraper in scrapers:
    scraper.scrape("http://example.com")