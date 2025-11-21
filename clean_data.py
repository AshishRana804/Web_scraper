import re

INPUT = "scraper/scraped_content.txt"
OUTPUT = "scraper/cleaned_content.txt"

with open(INPUT, "r", encoding="utf-8") as f:
    text = f.read()

# Normalize spaces
text = re.sub(r'\n+', '\n', text)
text = re.sub(r'\s+', ' ', text)

# Clean HTML remains or JS
text = re.sub(r'<.*?>', '', text)

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(text)

print("✔ Cleaned data saved to:", OUTPUT)
