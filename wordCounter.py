from collections import Counter
import matplotlib.pyplot as plt

class WordCounter:
    def __init__(self):
        self.word_counts = Counter()

    def count_words_in_article(self, article_text):
        words = article_text.split()
        word_counts = Counter(words)
        return word_counts

    def add_article_words(self, article_text):
        article_word_counts = self.count_words_in_article(article_text)
        self.word_counts += article_word_counts

    def get_top_words(self, n=10):
        return self.word_counts.most_common(n)
    
    def savePlot(self, topWords, savePath):
        # topWords listesinden verileri ayırma
        words, counts = zip(*topWords)

        # Çubuk grafik oluşturma
        plt.figure(figsize=(10, 6))
        plt.bar(words, counts, color='skyblue')
        plt.xlabel('Kelimeler')
        plt.ylabel('Sayı')
        plt.title('En Çok Geçen Kelimeler')
        plt.xticks(rotation=45)  # X ekseni etiketlerini döndürme
        plt.tight_layout()

        # Grafik dosyasına kaydetme
        plt.savefig(savePath)