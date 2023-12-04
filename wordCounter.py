from collections import Counter
import matplotlib.pyplot as plt

# Bu sınıf, metinlerdeki kelimelerin sayısını hesaplar
class WordCounter:
    def __init__(self):
        # Kelime sayılarını saklamak için bir Counter nesnesi oluşturur
        self.word_counts = Counter()

    # Metindeki kelimelerin sayısını döndürür
    def count_words_in_article(self, article_text):
        # Metindeki kelimelerin sayısını Counter ile hesaplar
        words = article_text.split()
        word_counts = Counter(words)
        return word_counts

    # Haberdeki kelimelerin sayısını word_counts'a ekler
    def add_article_words(self, article_text):
        # Makaledeki kelimelerin sayısını hesaplar ve word_counts'a ekler
        article_word_counts = self.count_words_in_article(article_text)
        self.word_counts += article_word_counts

    # En çok geçen kelimelerin listesini döndürür
    def get_top_words(self, n=10):
        return self.word_counts.most_common(n)
    
    # En çok geçen kelimelerin çubuk grafiğini kaydeder
    def savePlot(self, topWords, savePath):
        # topWords listesinden verileri ayırma   .  Kelimeler ve sayılarını ayrıştırır
        words, counts = zip(*topWords)

        # Çubuk grafiği oluşturur ve kaydeder
        plt.figure(figsize=(10, 6))
        plt.bar(words, counts, color='skyblue')
        plt.xlabel('Kelimeler')
        plt.ylabel('Sayı')
        plt.title('En Çok Geçen Kelimeler')
        plt.xticks(rotation=45)  # X ekseni etiketlerini döndürme
        plt.tight_layout()

        # Grafik dosyasına kaydetme
        plt.savefig(savePath)
        