from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

chunks = []

with open("transcripts/sample_call.txt", "r", encoding="utf-8") as f:
    text = f.read()

sentences = text.split(".")

for sentence in sentences:
    if sentence.strip():
        vector = model.encode(sentence)
        chunks.append((sentence.strip(), vector))

print("Transcript embedded successfully")