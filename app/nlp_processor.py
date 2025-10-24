# Mock NLP processor using Hugging Face (summarization and classification)
def summarize_news(content):
    # Replace with real Hugging Face summarization
    return content[:60] + "..."

def classify_theme(title, content):
    # Mock classification logic
    if 'AI' in title or 'tech' in title.lower():
        return 'Technology'
    elif 'stock' in title.lower() or 'economy' in title.lower():
        return 'Economy'
    elif 'politic' in title.lower() or 'debate' in title.lower():
        return 'Politics'
    elif 'sport' in title.lower():
        return 'Sports'
    else:
        return 'Other'
