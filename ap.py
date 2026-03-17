from rag_search import retrieve
from sentiment import analyze_sentiment, detect_risk, extract_keywords

query = "What did company say about AI?"

results = retrieve(query)
answer = " ".join([item[0] for item in results])

sentiment = analyze_sentiment(answer)
risk = detect_risk(answer)
keywords = extract_keywords(answer)

print("Query:", query)
print("Retrieved Answer:", answer)
print("Sentiment Score:", sentiment[0])
print("Sentiment Label:", sentiment[1])
print("Risk:", risk)
print("Keywords:", keywords)