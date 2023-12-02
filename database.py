from pymongo import MongoClient
from pymongo.errors import CollectionInvalid
from logs import log

log = log();

class mongoDb:
    def __init__(self, connection_uri, database_name):
        try:
            self.client = MongoClient(connection_uri)
            self.db = self.client[database_name]
            log.add('Veritabanı bağlantısı başarıyla kuruldu.')
        except:
            log.add('Veritabanı bağlantısı kurulamadı.')
        
    """ 
        ne yaptığı
    """
    def create_collections(self):
         # News collection
        try:
            self.news_collection = self.db.create_collection('news')
        except CollectionInvalid:
            self.news_collection = self.db['news']

        # Word frequency collection
        try:
            self.word_frequency_collection = self.db.create_collection('word_frequency')
        except CollectionInvalid:
            self.word_frequency_collection = self.db['word_frequency']

        # Stats collection
        try:
            self.stats_collection = self.db.create_collection('stats')
        except CollectionInvalid:
            self.stats_collection = self.db['stats']

    def insert_news(self, news_data):
        try:
            self.news_collection.insert_one(news_data)
            log.add('Veritabanına haberler eklendi.')
            return True
        except:
            log.add('Veritabanına haberler eklenemedi.')
            return False
            

    def insert_word_frequency(self, word_frequency_data):
        try:
            self.word_frequency_collection.insert_many(word_frequency_data)
            log.add('En çok kullanılan kelimeler eklendi.')
            return True
        except:
            log.add('En çok kullanılan kelimeler eklenemedi.')
            return False
        

    def insert_stats(self, stats_data):
        try:
            self.stats_collection.insert_one(stats_data)
            log.add('Ölçüm değerleri eklendi.')
            return True
        except:
            log.add('Ölçüm değerleri eklenemedi.')
            return False
        
        
    def print_grouped_by_update_date(self):
        try:
            # MongoDB'den verileri gruplayarak alıyoruz
            pipeline = [
                {"$group": {"_id": "$update_date", "data": {"$push": "$$ROOT"}}},  # update_date'e göre gruplama
                {"$sort": {"_id": 1}}  # update_date'e göre sıralama
            ]
            
            grouped_data = self.news_collection.aggregate(pipeline)
            
            # Gruplanmış verileri ekrana yazdırma
            for group in grouped_data:
                print(f"Update Date: {group['_id']}")
                for data in group['data']:
                    print(data)
                print("\n")
            return True
        except:
            log.add('print_grouped_by_update_date fonksiyonunda hata meydana geldi')
            return False
        
