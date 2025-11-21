import re
import json

INPUT = "scraped_content.txt"
OUTPUT = "pages.json"

with open(INPUT, 'r', encoding='utf-8') as f:
    text = f.read()

# Based on scraper format:
pages = re.split(r'PAGE_START:', text)
pages_data = []

for p in pages:
    if not p.strip():
        continue
    
    try:
        url, content = p.split("PAGE_END", 1)
        pages_data.append({
            "url": url.strip(),
            "content": content.strip()
        })
    except:
        pass

json.dump(pages_data, open(OUTPUT, "w", encoding="utf-8"), indent=2)

print("✔ Pages saved:", OUTPUT)
print("Total pages:", len(pages_data))
