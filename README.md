# News Scraper and Email Sender

This Python script scrapes the latest news articles from TechCrunch, AP News, and Yahoo Finance, compiles them into a formatted email, and sends it to a specified email address. This tool is useful for automating the collection and distribution of the latest news.

## Description

The script performs the following tasks:

1. **Scrapes TechCrunch for the latest tech news.**
2. **Scrapes AP News for the latest world news.**
3. **Scrapes Yahoo Finance for the latest US economy news.**
4. **Formats the scraped news into an HTML email.**
5. **Sends the email to a specified recipient using SMTP.**

## Table of Contents

- [News Scraper and Email Sender](#news-scraper-and-email-sender)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/news-scraper-email-sender.git
   cd news-scraper-email-sender
   ```

2. **Install the required packages:**
   ```sh
    pip install requests beautifulsoup4
   ```

## Usage

1. **Configure the script:**
   - Open the "scrape_yahoo_finance_bs4.py" script.
   - Set the "to_email", "from_email", and "app_password" variables with your email details and the app-specific password.
