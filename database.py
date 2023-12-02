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
        self.news_collection.insert_one(news_data)

    def insert_word_frequency(self, word_frequency_data):
        self.word_frequency_collection.insert_many(word_frequency_data)

    def insert_stats(self, stats_data):
        self.stats_collection.insert_one(stats_data)
        
    def print_grouped_by_update_date(self):
        # MongoDB'den verileri gruplayarak alıyoruz
        pipeline = [
            {"$group": {"_id": "$update_date", "data": {"$push": "$$ROOT"}}},  # update_date'e göre gruplama
            {"$sort": {"_id": 1}}  # update_date'e göre sıralama
        ]
        
        grouped_data = self.news_collection.aggregate(pipeline)
        
        # Gruplanmış verileri ekrana yazdırma
        print("Update Date\t\tCount")
        # Gruplanmış verileri ekrana yazdırma
        for group in grouped_data:
            print(group)
            """ print(f"Update Date: {group['_id']}")
            for data in group['data']:
                print(data) """
            print("\n")
