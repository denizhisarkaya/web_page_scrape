# Bu sınıf, haber öğelerini oluşturmak için kullanılır
class newCreate:
    def __init__(self, url, header, summary):
        # URL, başlık ve özet bilgilerini saklar
        self.url = url
        self.header = header
        self.summary = summary
        # Haber detayları için yeni bir newDetail örneği oluşturur
        self.detail = newDetail('', [], '', '')
        
    # Haber detayları ekler    
    def add_detail(self, text, img_url_list, publish_date, update_date):
        # Metin, görsel URL listesi, yayınlanma ve güncelleme tarihlerini saklar
        self.detail.img_url_list = img_url_list
        self.detail.text = text
        self.detail.publish_date = publish_date
        self.detail.update_date = update_date
        return True
# Bu sınıf, bir haber öğesinin detaylarını saklar    
class newDetail:
    def __init__(self, text, img_url_list, publish_date, update_date):
        self.text = text
        self.img_url_list = img_url_list
        self.publish_date = publish_date
        self.update_date = update_date

        