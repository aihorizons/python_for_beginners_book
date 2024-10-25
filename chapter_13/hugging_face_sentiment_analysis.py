from transformers import pipeline
 
# Load the pre-trained sentiment-analysis pipeline
classifier = pipeline("sentiment-analysis")
 
# Analyze the sentiment of a sentence
result = classifier("I love learning Python!")[0]
 
print(f"Label: {result['label']}, Score: {result['score']:.4f}")
