# KULLANILAN KÜTÜPHANELER:
Bir benzerlik oranı bulma algoritması oluşturulmuştur. Veri seti 1000kitap sitesinden çekilmiş kitap isimleri ve kitapların konularından oluşmaktadır. Veri setinde bulunan farklı türdeki kitaplarla ilgili model eğitiliyor ve gönderilen konunun hangi kitaba daha benzer olduğu tespit ediliyor.
## Kullanılan Kütüphaneler:
### •pandas
### •scikit-learn
### •spacy
### •simplemma
### •numpy
### •ast
### •re
### •nltk
### •torch
### •transformers

## VERİ SETİNİN OLUŞTURULMASI:
Veri seti 1000kitap sitesinden çekilen kitap isimleri ve konuları ile oluşturulmuştur.
İlk olarak selenium kütüphanesi ile sitenin en beğenilen kitapları gösterdiği https://1000kitap.com/kitaplar/en-begenilenler adresinden kitapların linklerini txt dosyasına kaydettim.
![image](https://github.com/IlknuraySudeBilgin/Ddi-Odev/assets/116540925/50d07116-de4d-4cdf-bb0c-edca1509d1bc)


Sonra bu linkleri tek tek gezerek kitapların isimlerini ve konularını çekerek txt dosyasına kaydettim ve bu verileri excel dosyasına kaydederek veri setini oluşturdum.
Veri setinde “Kitap” ve “Konu” olmak üzere 2 sütun var.
![image](https://github.com/IlknuraySudeBilgin/Ddi-Odev/assets/116540925/816a2fef-30e3-4754-a3b6-77d689bbc8ab)
![image](https://github.com/IlknuraySudeBilgin/Ddi-Odev/assets/116540925/07b50026-9bbf-40c1-932b-c377c8f36c8a)

 
## KONULARIN TEMİZLENMESİ
Veri setini temizlememizin amacı metin verisinin analizi sırasında daha tutarlı ve anlamlı sonuçlar elde etmektir.Veri setinde kitap konularında bulunan dolgu sözcüklerini,noktalama işaretlerini temizledim.Daha sonra lemmatization uyguladım.Böylece daha temiz bir veri seti elde ettim.Bu da analiz işleminde daha tutarlı sonuçlar elde etmemi sağlayacak. 
![image](https://github.com/IlknuraySudeBilgin/Ddi-Odev/assets/116540925/6a07c218-bcdc-4624-b2f8-eed8e277f991)


## MODEL OLUŞTURMA VE BENZERLİK ORANI BULMA:
Veri seti analizinin hangi modelde daha yüksek başarı oranına sahip olacağına dair araştırma yapılıp 3 model üzerinde test edilmiştir.By modeller TF-IDF, Universal Sentence Encoder,Doc2Vec modelleridir.Veri setinde bu modellerin aynı kitap konusu üzerindeki benzerlik oranı en yüksek 5 kita bulunmuştur.Örnekte inceleyeceğimiz kitap konusu “rüya evreni”.Projedeki test veri seti sonuçlarına baktığımızda:


TF-IDF Modeli için en yüksek benzerlik oranı: 0.6013
En yüksek benzerlik oranına sahip kitabın adı: Başka Bir Şey
En yüksek benzerlik oranına sahip ilk 5 kitap ve benzerlik oranları:

![image](https://github.com/IlknuraySudeBilgin/Ddi-Odev/assets/116540925/21a108cb-8292-4b4c-8f5e-2776a4a425bb)

Universal Sentence Encoder Modeli için en yüksek benzerlik oranı: 0.21017774939537048
En yüksek benzerlik oranına sahip kitabın adı: Daktiloya Çekilmiş Şiirler
En yüksek benzerlik oranına sahip ilk 5 kitap ve benzerlik oranları:
![image](https://github.com/IlknuraySudeBilgin/Ddi-Odev/assets/116540925/5bfdce2b-994f-4ebc-81a4-3e941f1aa07b)


Doc2Vec Modeli için en yüksek benzerlik oranı: 0.6565651893615723
En yüksek benzerlik oranına sahip kitabın adı: Daktiloya Çekilmiş Şiirler
En yüksek benzerlik oranına sahip ilk 5 kitap ve benzerlik oranları:
![image](https://github.com/IlknuraySudeBilgin/Ddi-Odev/assets/116540925/ee1e9f70-963f-4791-96b9-b3378767cd6b)

Sonuçları incelediğimizde en başarısız modelin yaklaşık oranına sahip olan 0.21018 Universal Sentence Encoder Modeli olduğu görülmektedir. En yüksek başarı oranına sahip model ise 0.6566 oranıyla Doc2Vec Modelidir.Bu nedenle Doc2Vec Modelini kullanmak daha iyi olacaktır.TF-IDF modelinin benzerik oranı da Doc2Vec modeline çok yakındır.

## MODELLERİN BAŞARISINA GÖRE ÇIKARIMLAR:

TFIDF, belgelerdeki kelimelerin önemini belirlemek için kullanılan bir modeldir; bir kelimenin belgedeki frekansı, genel koleksiyon içindeki yaygınlığına orantılanarak belirlenir. TD-IDF, kelime sıklıklarına dayalı bir vektörleme yöntemidir, ancak kısa metinlerde veya benzer anlamlı ifadelerde kısıtlı anlam taşıyabilir.
Universal Sentence Encoder, metin verilerini sayısal vektörlerle temsil etmek ve çeşitli doğal dil işleme görevlerini gerçekleştirmek üzere tasarlanmış bir modelidir. Universal Sentence Encoder, geniş bir metin anlama yeteneğine sahiptir ve kısa metinleri başarılı bir şekilde işleyebilir.
Doc2Vec ise metin belgelerini vektörlerle temsil ederek belge düzeyinde semantik ilişkileri analiz edebilen bir modeldir. 
Doc2Vec, uzun metinleri daha iyi anlama yeteneğine sahiptir. Model, metin belgelerini vektörlerle temsil ederek belgeler arasındaki semantik ilişkileri öğrenir. Ancak, modelin performansı eğitim veri kümesi ve parametrelerine bağlıdır.
