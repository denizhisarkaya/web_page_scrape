class log:
    def __init__(self, file_name='log.txt'):
        self.file_name = file_name
    
    def add(self, message):
        with open(self.file_name, 'a') as file:
            file.write(f"{message}\n")
            print(f"Log '{message}' written to {self.file_name}")
