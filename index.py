from newScraper import newScraper
from newCreate import newCreate
from wordCounter import WordCounter
from database import mongoDb
import os
from logs import log
import time
from datetime import datetime

beginning_time = time.time()

url_page = 'https://turkishnetworktimes.com/kategori/gundem/'
max_pages = 1  # İlk iki sayfayı çekmek için

success_count = 0
unsuccess_count = 0

now_time = datetime.now()

wordCounter = WordCounter()
log = log()

# database connection
# MongoDB bağlantı URI'si ve veritabanı adı
connection_uri = 'mongodb://localhost:27017/'  # MongoDB adresi ve portu
database_name = 'deniz_hisarkaya'  # Veritabanı adı
# NewsDatabase sınıfını kullanarak bağlantıyı kurma ve koleksiyonları oluşturma
news_db = mongoDb(connection_uri, database_name)
news_db.create_collections()

for page_num in range(1, max_pages + 1):
    scraper = newScraper(url_page, page_num)
    currentScraper = scraper.find('div', 'news')
    urls = scraper.findAll('a', 'urls', currentScraper)
    headers = scraper.findAll('h2', 'headers')
    summaries = scraper.findAll('div', 'summaries')

    for index, url in enumerate(urls):
        currentUrl = url.get('href')
        currentNew = newCreate(currentUrl, headers[index].text, summaries[index].text)
        article_text, article_images, publish_date, update_date = scraper.get_article_details(currentNew.url)
        currentNew.add_detail(article_text, article_images, publish_date, update_date)
        
        wordCounter.add_article_words(article_text)
        
        currentNew_data = {
            "url": currentNew.url,
            "header": currentNew.header,
            "summary": currentNew.summary,
            "text": currentNew.detail.text,
            "img_url_list": currentNew.detail.img_url_list,
            "publish_date": currentNew.detail.publish_date,
            "update_date": currentNew.detail.update_date
        }
        addedResult = news_db.insert_news(currentNew_data)
        if (addedResult):
            success_count += 1
        else: 
            unsuccess_count += 1
        
topWords = wordCounter.get_top_words(10)
word_frequency_documents = [
    {"word": word, "count": count} for word, count in topWords
]
news_db.insert_word_frequency(word_frequency_documents)

figPath = os.path.join(os.getcwd(), 'mostCommonWords.png')
wordCounter.savePlot(topWords, figPath)

finish_time = time.time()
pass_time = finish_time - beginning_time

stats_data = {
    "elapsed_time": pass_time,
    "count": success_count + unsuccess_count,
    "date": now_time.strftime("%Y-%m-%d %H:%M"),
    "success_count": success_count,
    "fail_count": unsuccess_count,
}
news_db.insert_stats(stats_data)
