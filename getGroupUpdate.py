from database import mongoDb

# database connection
# MongoDB bağlantı URI'si ve veritabanı adı
connection_uri = 'mongodb://localhost:27017/'  # MongoDB adresi ve portu
database_name = 'deniz_hisarkaya'  # Veritabanı adı
# NewsDatabase sınıfını kullanarak bağlantıyı kurma ve koleksiyonları oluşturma
news_db = mongoDb(connection_uri, database_name)
news_db.create_collections()
news_db.print_grouped_by_update_date()
