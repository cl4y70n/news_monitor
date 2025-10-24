# News & Trends Monitor

This project aggregates news articles, summarizes them, classifies by theme, and visualizes insights in an interactive dashboard.

## Features
- Scrape or load news from CSV (10–20 sample articles for demo)
- Summarize news content using NLP (Hugging Face mock)
- Classify news by theme (Technology, Economy, Politics, Sports, Other)
- Interactive dashboard with Plotly Dash
- Lightweight demo, easy to extend for real sources

## Setup
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m app.aggregator  # Aggregate news and generate CSV
python app/dashboard.py   # Run the dashboard
```

## Folder Structure
```
news_monitor/
├── app/
│   ├── scraper.py
│   ├── nlp_processor.py
│   ├── aggregator.py
│   └── dashboard.py
├── data/
│   └── news_sample.csv
├── reports/screenshots/
├── requirements.txt
└── README.md
```

## Future Improvements
- Connect to real news APIs (NYTimes, Reuters, Google News)
- Automated daily summary and alerts
- Advanced dashboards with trend analysis over time
- Email or Slack notifications
