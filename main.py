# Emir Tarik Dede

import time
from crawler import Crawler

crawler = Crawler()

start = time.time()

# Belirtilen aralık
start_id = 3_332_000
end_id = 3_338_000

current_id = start_id  # Başlangıç ID'si
while current_id <= end_id:
    try:
        print(f"{current_id} ID'si için veri indiriliyor...")
        crawler.get_news(current_id, current_id + 1)  # Sadece tek bir ID'yi işliyoruz
        current_id += 1  # İşlem başarılı olursa sıradaki ID'ye geç
        time.sleep(1)  # Sunucuyu rahatlatmak için isteklere bekleme ekledik
    except Exception as e:
        print(f"{current_id} ID'sinde bir hata oluştu: {e}. Yeniden denenecek...")

# Tüm veriler indirildikten sonra kaydet
try:
    crawler.save_news()
    print("Tüm haberler başarıyla kaydedildi.")
except Exception as e:
    print(f"Haberler kaydedilirken bir hata oluştu: {e}")

end = time.time()
print(f"Toplam süre: {end - start} saniye")
