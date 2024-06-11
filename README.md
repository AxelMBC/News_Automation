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
  - [Automation](#automation)

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

2. **Run the script**
   ```sh
    python scrape_yahoo_finance_bs4.py
   ```

The script will output the titles and links of the first three news articles from each source and send an email with this information.

## Automation

1. **Open Task Scheduler**

   - Press `Win + S`, type "Task Scheduler", and hit Enter.

2. **Create a new task:**

   - In the "Actions" pane, click "Create Basic Task...".
   - Follow the wizard to name the task and give a description.

3. **Set the trigger:**

   - Choose "Daily" and set the time you want the script to run.

4. **Set the action:**

- Select "Start a program" and browse to the Python executable in your file explorer:

```sh
 "C:\path\to\your_script.py"
```

- Add the script path in the "Add arguments" field:

  ```sh
  C:\path\to\your\scrape_yahoo_finance_bs4.py
  ```

5. **Finish the setup:**

- Review your settings and click "Finish" .
