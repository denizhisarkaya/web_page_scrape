import requests
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt

class newScraper:
    def __init__(self, url, page):
        self.url = url + '/page/' + str(page)
        self.news = "kategori_yazilist"
        self.headers = "haber-baslik"
        self.summaries = "haber-desc"
        self.urls = "post-link"
        self.textInterior = "yazi_icerik"
        self.date = "tarih"
        self.textBio = "yazibio"

    def get_soup(self, url = None):
        url = url or self.url
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        else:
            return None
        
    def findAll(self, elem, className, soup = None):
        soup = soup or self.get_soup()
        if soup:
            class_property = getattr(self, className, None)
            result = soup.find_all(elem, class_=class_property)
        else:
            result = False
        return result
    
    def find(self, elem, className, soup = None):
        soup = soup or self.get_soup()
        if soup:
            class_property = getattr(self, className, None)
            result = soup.find(elem, class_=class_property)
        else:
            result = False
        return result

    def get_article_content(self, article_soup, className):
        if article_soup:
            class_property = getattr(self, className, None)
            article_content = article_soup.find('div', class_=class_property)
            if article_content:
                all_text = ''
                p_tags = article_content.find_all('p')
                for p_tag in p_tags:
                    all_text = all_text + p_tag.get_text(strip=True)
                return all_text
            else:
                return None
        else:
            return None

    def get_article_images(self, article_soup):
        if article_soup:
            image_list = []
            img_tags = article_soup.find_all('img')
            for img_tag in img_tags:
                image_list.append(img_tag.get('data-src'))
            return image_list
        else:
            return None

    def get_date_update_append(self, soup = None):
        soup = soup or self.get_soup()
        yazibioSoup = self.find('div', 'textBio', soup)
        dates = self.findAll('span', 'date', yazibioSoup)
        # Yayınlanma tarihi
        time_tag = dates[0].find('time')
        date_value_publish = time_tag['datetime']
        # Güncelleme tarihi
        time_tag = dates[1].find('time')
        date_value_update = time_tag['datetime']
        return [date_value_publish, date_value_update]
    
    def get_article_details(self, article_url):
        article_soup = self.get_soup(article_url)
        article_text = self.get_article_content(article_soup, 'textInterior')
        article_images = self.get_article_images(article_soup)
        dates = self.get_date_update_append(article_soup)
        publish_date = dates[0]
        update_date = dates[1]
            
        return article_text, article_images, publish_date, update_date

    def textCounter(self, tum_metin):
        # Metni küçük harflere dönüştür ve noktalama işaretlerini temizle
        temizlenmis_metin = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in tum_metin.lower())

        # Kelimelere ayır ve kelime sayısını hesapla
        kelimeler = temizlenmis_metin.split()
        kelime_sayilari = Counter(kelimeler)

        # En çok kullanılan 10 kelimeyi bul
        en_cok_kullanilan_10_kelime = kelime_sayilari.most_common(10)

        # Kelimeler ve sıklıkları
        kelimeler = [kelime[0] for kelime in en_cok_kullanilan_10_kelime]
        sikliklar = [kelime[1] for kelime in en_cok_kullanilan_10_kelime]
        return [kelimeler, sikliklar]
