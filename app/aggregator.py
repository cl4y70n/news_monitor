import pandas as pd
from app.scraper import scrape_news
from app.nlp_processor import summarize_news, classify_theme

def aggregate_news():
    news_list = scrape_news()
    aggregated = []
    for news in news_list:
        summary = summarize_news(news['Content'])
        theme = classify_theme(news['Title'], news['Content'])
        aggregated.append({
            'Title': news['Title'],
            'Summary': summary,
            'Theme': theme,
            'Date': news['Date']
        })
    df = pd.DataFrame(aggregated)
    df.to_csv("data/news_aggregated.csv", index=False)
    return df
