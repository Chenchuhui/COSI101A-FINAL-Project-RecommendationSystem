import pandas as pd
import re

def word_count(text):
    return len(text.split())

def clean_text(text):
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove non-English characters
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    # Remove all numbers (including dates)
    text = re.sub(r'\d+', '', text)
    # Insert a space before a capital letter if it's not preceded by a space or another capital letter
    text = re.sub(r'(?<![A-Z\s])(?=[A-Z])', ' ', text)
    # Remove punctuation and non-letter characters
    text = re.sub(r'[^a-zA-Z\s-]', '', text)
    # Trim whitespace at the beginning and end
    text = text.strip()

    return text


df = pd.read_csv('data/devpost_data_update3.csv')
df = df[df['description'].notna() & (df['description'] != '')]
df['description'] = df['description'].apply(clean_text)
df = df[df['description'].apply(word_count) >= 10]

df.to_csv("data/devpost_data_update4.csv", index=False)