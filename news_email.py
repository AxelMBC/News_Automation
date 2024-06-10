import requests
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def scrap_techchrunch_tech():
    res_tech = requests.get('https://techcrunch.com/')
    soup = BeautifulSoup(res_tech.text, 'html.parser')
    container = soup.select('.wp-block-post-title')
    all_news = []
    
    for item in container[:3]:
        news_title = item.getText()
        a_tag = item.find('a', href=True)["href"]
        all_news.append({'title': news_title, 'link': a_tag})

    return all_news

def scrap_ap_news_world():
    res_ap = requests.get('https://apnews.com/world-news')
    soup = BeautifulSoup(res_ap.text, 'html.parser')
    container_item = soup.select('.PagePromo-title')
    all_news = []
    for item in container_item[5:8]:
        news_title = item.getText()
        a_tag = item.find('a', href=True)["href"]
        all_news.append({'title': news_title.strip(), 'link': a_tag})

    return all_news

def scrap_yahoo_finance_economy():
    res_ap = requests.get('https://finance.yahoo.com/topic/economic-news/')
    res_ap.raise_for_status()
    soup = BeautifulSoup(res_ap.text, 'html.parser')
    articles = soup.find_all('a', class_='mega-item-header-link')
    all_news = []

    for article in articles[:3]:
        title = article.get_text(strip=True)
        link = article['href']
        if not link.startswith('http'):
            link = 'https://finance.yahoo.com' + link  # Ensure the link is complete
        all_news.append({'title': title, 'link': link})

    return all_news


def format_email(tech_news, world_news, economy_news):
    html = """
    <html>
    <body>
        <h2>Latest News Digest</h2>
        <h3>Tech News</h3>
        <ul>
    """
    for news in tech_news:
        html += f"<li><strong style='font-size: 18px;'>{news['title']}</strong><br><a href='{news['link']}'>{news['link']}</a></li>"
    
    html += """
        </ul>
        <h3>World News</h3>
        <ul>
    """
    for news in world_news:
        html += f"<li><strong style='font-size: 18px;'>{news['title']}</strong><br><a href='{news['link']}'>{news['link']}</a></li>"
    
    html += """
        </ul>
        <h3>US Economy News</h3>
        <ul>
    """
    for news in economy_news:
        html += f"<li><strong style='font-size: 18px;'>{news['title']}</strong><br><a href='{news['link']}'>{news['link']}</a></li>"
    
    html += """
        </ul>
    </body>
    </html>
    """
    return html

def send_email(body, to_email, from_email, app_password):
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Latest News Digest"

    msg.attach(MIMEText(body, 'html'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, app_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    tech_news = scrap_techchrunch_tech()
    world_news = scrap_ap_news_world()
    economy_news = scrap_yahoo_finance_economy()
    email_body = format_email(tech_news, world_news, economy_news)
    to_email = "axel.barraza099@gmail.com"
    from_email = "axel.barraza099@gmail.com"
    app_password = "iyts nbft ukmy thhw"  # Use the app password here

    send_email(email_body, to_email, from_email, app_password)

if __name__ == "__main__":
    main()