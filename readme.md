### Web Page Scrape

Smart-Maple projesi için geliştirilmiştir.

## Index.py adlı dosyada yapılanlar

Index.py adlı dosyamızda istenilen haber sitesinden veri çekilip, bu veriler işleniyor, en çok kullanılan kelimeleri sayıyor ve sonra ilgili bilgileri MongoDB veritabanına kaydediyor. 
Kod başladığında zamanı kaydediyor ve MongoDB'ye bağlantı kuruyor.
“newScraper” modülüyle verilen URL'den sayfa içeriğini çekiyor.
Her sayfadan haberleri işliyor, başlık, özet ve URL gibi temel bilgileri alıyor.
Her haberin detayları için detay sayfasına geçiyor ve metin, görseller, yayınlanma ve güncelleme tarihlerini alıyor.
Bu bilgileri MongoDB veritabanına kaydediyor.
En çok geçen kelimeleri buluyor, bunların sıklıklarını hesaplıyor ve bunları da veritabanına kaydediyor.
İşlem süresi, haber sayısı, başarı ve başarısızlık sayıları verimlilik için ölçüm değerlerini veritabanına ekleniyor.


## database.py adlı dosyada yapılanlar

database.py adlı dosyanın genel amacı, MongoDB veritabanına veri eklemek ve belirli işlemleri gerçekleştirmektir. İlgili koleksiyonları oluşturarak, verileri ekliyoruz. 
“ __init__ “ fonksiyonu, belirtilen URI üzerinden MongoDB'ye bağlanmayı ve ilgili veritabanını seçmeyi sağlar. Bağlantı kurulduğunda, bir log kaydı oluşturulur.
 “create_collections” fonksiyonu, önceden tanımlanmış koleksiyonları oluşturur veya zaten varsa onları kullanır. Bu koleksiyonlar, haberler için 'news', kelime kullanım sıklığı için 'word_frequency' ve ölçüm verileri için 'stats' dir.
“insert_news” fonksiyonu haber verilerini 'news' koleksiyonuna eklememizi sağlar.
“insert_word_frequency” fonksiyonu kelime sıklık verilerini 'word_frequency' koleksiyonuna ekler.
insert_stats: fonksiyonu  ölçüm verilerini 'stats' koleksiyonuna ekler.
“print_grouped_by_update_date” fonsiyonu ile MongoDB'deki belirli bir koleksiyondan verileri gruplayarak alma işlemini yapılmasını ve grup-lanmış verileri ekrana yazdırılmasını sağlar.


## newScraper.py adlı dosyada yapılanlar

“newScraper” sınıfı, web sayfalarından haberleri çekmek için oluşturulmuştur. “__init__ “metodu, sınıfın başlatıcısıdır ve bir URL ve sayfa numarası alarak sınıfın özelliklerini belirler.
“get_soup” metodu, BeautifulSoup nesnesini elde etmek için kullanılır. Verilen URL'den sayfanın HTML içeriğini çeker ve bunu bir BeautifulSoup nesnesi olarak döndürür.
findAll ve find: Belirtilen sınıftan (başlık, özet, URL vb.) tüm öğeleri veya ilk öğeyi bulmamızı sağlar..
“get_article_content” metodu, bir haberin içeriğini çekmek için kullanılır. Haberin içeriği “article_soup” argümanı içerisindeki HTML içeriğinden çekilir. Kısacası haber içeriğini bulur ve metin olarak döndürür.
“get_article_images” fonksiyonu haberdeki görselleri bulur ve bir liste olarak döndürür.
“get_date_update_append” fonksiyonu haberin yayınlanma ve güncelleme tarihlerini bulur.
get_article_details: fonksiyonu haberin içeriğini, görsellerini ve tarih bilgilerini alır.
“textCounter” metodu, verilen bir metindeki kelimelerin sayısını hesaplamak için kullanılır. Metindeki kelimelerin sıklığını hesaplar ve en sık geçen 10 kelimeyi ve bu kelimelerin sayısını döndürür.
Bu sınıfın genel amacı, bir web sitesinden haber içeriklerini çekmek, bu içerikleri analiz etmek ve metin içeriğindeki kelimelerin sıklığını hesaplamaktır. Ancak şu anki halinde sadece bu işlevleri barındırmaktadır.



## newCreate.py adlı dosyada yapılanlar

Bu sınıfların amacı, bir haber öğesinin genel bilgilerini saklamak ve daha sonra haberin detaylarını eklemek için ayrı bir yapı oluşturmaktır. 


## wordCounter.py adlı dosyada yapılanlar

Bu sınıf, metinlerdeki kelime sayılarını saymak, en sık geçen kelimelerin listesini oluşturmak ve bu verileri çubuk grafik olarak kaydetmek için yazılmıştır.
Kelime sayılarını saklamak için bir Counter nesnesi oluşturulur.
“count_words_in_article” fonksiyonu bir haber metnindeki kelimelerin sayısını “Counter” kullanarak hesaplar ve geri döndürür.
“add_article_words” fonksiyonu bir makalenin metnindeki kelimelerin sayısını “count_words_in_article” yöntemini kullanarak hesaplar ve bu kelimeleri “word_counts”a ekler.
“get_top_words” fonksiyonu “Counter” nesnesinde en çok geçen kelimelerin listesini alır ve en sık geçen 10 kelimeyi döndürür.
“savePlot” fonksiyonu en çok geçen kelimelerin çubuk grafiğini oluşturur ve kaydeder.
“topWords” parametresi, kelimelerin listesi ve sayılarıdır.
“savePath” parametresi oluşturulan grafik dosyasının kaydedileceği konumu belirtir. 
![Açıklama metni](C:\Users\deniz\OneDrive\Masaüstü\web_page_scrape\mostCommonWords.png)


## getGroupUpdate.py adlı dosyada yapılanlar

MongoDB ile etkileşime geçerek veri tabanında işlemler gerçekleşir. Öncelikle veri tabanı bağlantısını kurar, ardından veri tabanı içerisinde gerekli koleksiyonları oluşturur ve son olarak da güncelleme tarihlerine göre gruplandırılmış verileri çıktılarla elde etmenizi sağlar. 
 

## logs.py adlı dosyada yapılanlar

Bu sınıf, basit bir loglama işlevselliği sağlar. Özellikle uygulama çalışırken hangi adımların gerçekleştiğini izlemek ve hata ayıklama yapmak için kullanılmıştır. 