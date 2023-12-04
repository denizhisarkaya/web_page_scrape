class log:
    def __init__(self, file_name='log.txt'):
        # Log dosyasının adını saklar
        self.file_name = file_name
    
    def add(self, message):
        # Belirtilen mesajı log dosyasına ekler
        with open(self.file_name, 'a') as file:
            file.write(f"{message}\n")
            # Belirtilen mesajın log dosyasına yazıldığını ekrana yazdırır
            #print(f"Log '{message}' written to {self.file_name}")
            
