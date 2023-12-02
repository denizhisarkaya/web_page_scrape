class newCreate:
    def __init__(self, url, header, summary):
        self.url = url
        self.header = header
        self.summary = summary
        self.detail = newDetail('', [], '', '')
        
        
    def add_detail(self, text, img_url_list, publish_date, update_date):
        self.detail.img_url_list = img_url_list
        self.detail.text = text
        self.detail.publish_date = publish_date
        self.detail.update_date = update_date
        return True
    
class newDetail:
    def __init__(self, text, img_url_list, publish_date, update_date):
        self.text = text
        self.img_url_list = img_url_list
        self.publish_date = publish_date
        self.update_date = update_date

        