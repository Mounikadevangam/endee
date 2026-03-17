import requests

response = requests.post(
    "http://127.0.0.1:5000/ask",
    json={"query": "What did company say about AI?"}
)

print("Status Code:", response.status_code)
print("Output:", response.text)