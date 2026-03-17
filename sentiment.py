from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        label = "Positive"
    elif polarity < 0:
        label = "Negative"
    else:
        label = "Neutral"

    return polarity, label

def detect_risk(text):
    risk_words = ["risk", "decline", "loss", "uncertain", "debt"]

    found = []

    for word in risk_words:
        if word.lower() in text.lower():
            found.append(word)

    return found

def extract_keywords(text):
    keywords = ["AI", "revenue", "margin", "growth", "guidance"]

    found = []

    for word in keywords:
        if word.lower() in text.lower():
            found.append(word)

    return found