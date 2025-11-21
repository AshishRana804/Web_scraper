# Web Scraper – Python Project

This repository contains a simple and efficient web scraping script written in Python.  
The tool extracts clean textual content from any website URL and saves it into a text file.

- Python's built-in file handling for saving output

## Features

- Scrapes text from any webpage
- Cleans unwanted HTML tags
- Saves output automatically in `scraped_data.txt`
- Error handling for invalid or slow websites
- Easy to modify and use for personal automation tasks

## How It Works

1. Enter any website URL in the script.
2. The scraper fetches the HTML content.
3. BeautifulSoup parses and extracts clean text.
4. Data is saved in a local text file.

## Usage

```bash
python scraper.py
