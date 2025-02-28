# News Headlines Scraping Project

## Overview

This project is a Python-based web scraping tool designed to extract news headlines, subtitles, and links from a specified website. The scraped data is stored in a CSV file for further analysis or usage. The project utilizes the Selenium library for web automation and scraping, along with Pandas for data manipulation.

## Features

- Scrapes the following information from the website:
  - News titles
  - Subtitles
  - Links to the news articles
- Saves the extracted data into a CSV file.
- Runs in headless mode for efficient and non-intrusive scraping.

## Requirements

To run this project, ensure you have the following installed:

- Python 3.x
- Required Python libraries:
  - selenium
  - webdriver-manager
  - pandas

## Workflow

### 1. Setup

- Configure Chrome options for headless mode and maximized window.
- Initialize the Selenium WebDriver.

### 2. Scraping

- Navigate to the specified website.
- Locate the containers holding the news data using XPath.
- Extract the title, subtitle, and link for each news item.
- Handle exceptions if elements are not found.

### 3. Data Storage

- Store the extracted data in lists.
- Convert the lists into a Pandas DataFrame.
- Save the DataFrame to a CSV file.

### 4. Cleanup

- Close the browser session.

## Example Output

The output CSV file will have the following structure:

| Title | Subtitle | Link |
| --- | --- | --- |
| Sample News Title 1 |  Sample Subtitle 1 | <https://example.com/news1> |
| Sample News Title 2 | Sample Subtitle 2 | <https://example.com/news2> |
