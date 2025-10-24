# Mock scraper for demo purposes
import pandas as pd

def scrape_news(file_path="data/news_sample.csv"):
    # In real case, implement BeautifulSoup/Scrapy scraping here
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')
