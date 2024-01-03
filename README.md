Literatür

İlk aşama olan veri toplama, genellikle web scraping adı verilen bir teknikle gerçekleştirilir. Web scraping, Python gibi dillerdeki Beautiful Soup gibi araçlar kullanılarak yapılan, web sayfalarından veri çekme işlemidir. Bu yöntem, genellikle yapılandırılmamış veriyi yapılandırılmış bir formata dönüştürmek için kullanılır. Projede bahsedilen Wikipedia'dan dizi bilgilerinin çekilmesi, bu yöntemin tipik bir uygulamasıdır.
Veri ön işleme aşaması, toplanan verilerin analize uygun hale getirilmesini içerir. Bu aşama genellikle veri temizleme, eksik veri doldurma, kategorik verileri sayısal verilere dönüştürme ve gerekirse özellik mühendisliği gibi işlemleri içerir. Ön işleme, modellemenin doğruluğunu ve verimliliğini doğrudan etkileyen kritik bir aşamadır.
Modelleme aşamasında, çeşitli istatistiksel ve makine öğrenimi teknikleri kullanılır. Decision Tree Classifier, RandomForestClassifier ve XGBoost (XGBClassifier) gibi algoritmalar, sınıflandırma problemlerinde sıkça kullanılan yöntemlerdendir. Her bir algoritma, veri üzerinde farklı bir yaklaşım sunar ve sonuçların doğruluğunu etkileyebilir. Projede belirtildiği gibi, bu modellerin her birinin başarı oranları farklılık göstermiştir, bu da seçilen modelin veri setinin yapısına ve özelliklerine ne kadar uygun olduğuna bağlıdır.
Literatürde, benzer projeler genellikle veri bilimi, makine öğrenimi, yapay zeka ve bilgisayar bilimleri alanlarında yer alır. Bu projeler, genellikle akademik dergilerde veya konferanslarda sunulur ve çeşitli veri kümeleri üzerinde yapılan deneyler, kullanılan yöntemlerin etkinliğini değerlendirir. Ayrıca, bu tür projeler genellikle büyük veri analizi, doğal dil işleme ve örüntü tanıma gibi daha geniş konularla ilişkilidir.
Sonuç olarak, televizyon dizileri hakkında bilgi toplama ve analiz etme projesi, veri bilimi ve makine öğrenimi alanlarında önemli ve güncel bir konuya odaklanmaktadır. Bu tür projeler, derinlemesine bilgi ve dikkatli bir yaklaşım gerektirir ve sonuçlar, alanda bilgi birikimine önemli katkılar sağlar.

Decision Tree Classifier:
Decision Tree Classifier, karar verme süreçlerini taklit eden ve bir dizi karar kurallarını uygulayarak verileri sınıflandıran gözetimli öğrenme modelidir. Bu model, her bir düğümde en iyi ayrımı yapan özelliği seçerek, bir ağaç yapısı oluşturur.

Literatürdeki Yeri: Karar ağaçları, 1980'lerden beri kullanılmakta olup, basitlikleri ve yorumlanabilirlikleri nedeniyle popülerdir. Çeşitli sektörlerde, özellikle tıp ve finans alanlarında risk analizi, teşhis koyma ve müşteri segmentasyonu gibi alanlarda kullanılmıştır.

Avantajları: Anlaşılması ve yorumlanması kolaydır. Verinin lineer olmasını gerektirmez ve hem sayısal hem de kategorik verilerle çalışabilir.

Dezavantajları: Aşırı dallanmaya eğilimlidir (overfitting), bu da modelin genelleme yeteneğini düşürebilir. Ayrıca, karar ağaçları veri değişikliklerine karşı hassastır; küçük bir değişiklik, tamamen farklı bir ağaç oluşturabilir.

2. RandomForestClassifier:
Random Forest, birçok karar ağacının tahminlerini birleştirerek çalışan bir ensemble öğrenme tekniğidir. Her bir ağaç, veri setinin rastgele alt kümelerinden bağımsız olarak oluşturulur ve son tahmin, tüm ağaçların tahminlerinin ortalaması alınarak yapılır.

Literatürdeki Yeri: 2001 yılında Leo Breiman tarafından tanıtılan Random Forest, karar ağaçlarının aşırı uyum (overfitting) sorununu azaltmak için geliştirilmiştir. Geniş bir uygulama yelpazesine sahiptir ve biyoenformatikten görüntü analizine kadar birçok alanda başarıyla kullanılmıştır.

Avantajları: Overfitting'e karşı daha dirençlidir ve genellikle karar ağaçlarından daha iyi performans gösterir. Değişkenlerin önemini anlamada kullanılabilir.

Dezavantajları: Yorumlanabilirlik konusunda zorluklar olabilir çünkü rastgele ormanlar birçok ağaçtan oluşur ve bu, bireysel tahminleri anlamayı zorlaştırır.

3. XGBoost (XGBClassifier):
XGBoost, Gradient Boosting frameworkunu optimize ederek yüksek performanslı ve hızlı çalışma imkanı sunan bir makine öğrenimi kütüphanesidir. XGBoost, karar ağaçlarını iteratif bir şekilde iyileştirerek modeli geliştirir.

Literatürdeki Yeri: 2016'da tanıtılan XGBoost, kısa sürede veri bilimi topluluğunda büyük popülerlik kazandı. Kaggle yarışmalarında birçok kazananın kullandığı bir teknik olması, etkinliğinin bir göstergesidir.

Avantajları: Yüksek performanslı ve hızlıdır, ayrıca ölçeklenebilir yapısı sayesinde büyük veri setleriyle çalışabilir. Overfitting'e karşı dirençlidir ve modelin düzenlenmesi için birçok parametre sunar.

Dezavantajları: Yüksek derecede ayarlama gerektirebilir ve yanlış ayarlandığında modelin performansı düşebilir. Yüksek hesaplama kaynakları gerektirebilir ve yorumlanması diğer modellere göre daha zordur.


Beautiful Soup
Beautiful Soup, Python programlama dilinde web scraping için yaygın olarak kullanılan bir kütüphanedir. Verileri HTML ve XML dosyalarından çıkarmak için kullanılır. Bu kütüphane, web sayfalarındaki verileri ayrıştırma ve düzenleme işlemlerini kolaylaştırır, böylece veri bilimcileri ve geliştiriciler hızlı ve etkili bir şekilde bilgi toplayabilirler.

Gelişimi ve Kullanımı: Leonard Richardson tarafından geliştirilen Beautiful Soup, ilk olarak 2004 yılında kullanıma sunuldu. Zaman içinde, çeşitli güncellemelerle daha etkin ve kullanıcı dostu hale getirildi. Bugün, veri toplama, veri madenciliği ve web tarama gibi alanlarda yaygın olarak kullanılmaktadır.


Kolay Ayrıştırma: Beautiful Soup, HTML ve XML dosyalarını kolayca ayrıştırmaya olanak tanır. Belirli etiketler, sınıflar ve id'ler kullanarak verilere hızlı bir şekilde erişebilirsiniz.

Farklı Parser Desteği: Çeşitli parserlar (lxml, html5lib gibi) ile uyumlu çalışabilir. Bu, farklı türdeki verileri daha etkin bir şekilde işlemeye yardımcı olur.

Beautiful Soup, akademik araştırmalardan ticari projelere kadar çeşitli alanlarda kullanılır. 


Algoritma Açıklaması 

Bu Python kodu, bir web sayfasındaki belirli verileri çekmek ve düzenlemek için yazılmıştır. Bu script, dizi listesi içeren bir Wikipedia sayfasından veri toplamak için Beautiful Soup kütüphanesini kullanmaktadır.

Başlangıç:
Kodun başında, isimler, linkler, bölüm_adet, sezon_adet, durumlar ve yayıncılar adında boş listeler oluşturulmuştur. Bu listeler, çekilecek olan verileri depolamak için kullanılacaktır. Her liste, dizilerin farklı özelliklerini (isim, link, bölüm sayısı, sezon sayısı, durum ve yayıncı bilgisi) tutacak şekilde ayrılmıştır.

Döngü ve Veri Çekme:
Kod, diziler[21:] listesini dolaşan bir for döngüsü içerir. Bu, diziler listesinin 22. elemanından (Python'da index 0'dan başlar) itibaren tüm elemanları döngüye alır. Her bir iterasyonda, dizi adında bir eleman üzerinde işlem yapılır.

Veri Çekme:

dizi_veriler adlı değişken, her bir dizi elemanının içindeki "td" etiketlerine (HTML'de tablo hücrelerini belirtir) sahip tüm alt elemanları bulur ve bir liste olarak kaydeder. Bu, her bir dizi için tablodaki sütun bilgilerini içerir.
Ardından, if (len(dizi_veriler)) != 5: ifadesi ile her bir dizi için beş sütun verisi olup olmadığı kontrol edilir. Eğer beşten farklı bir sayıda sütun varsa, continue komutu ile döngünün bu iterasyonu atlanır ve bir sonraki diziye geçilir. Bu, veri yapısının tutarlılığını sağlamak için bir kontrol mekanizmasıdır.

Veri İşleme ve Kaydetme:

Her bir sütundaki veri, adı, link, bölüm_sayısı, sezon_sayısı, durumu, yayıncı adlı değişkenlere atanır. Bu veriler, dizi_veriler listesinin ilgili indekslerinden çekilir.
adı ve link için ek bir işlem yapılır. Eğer bir link bulunamazsa (except bloğu), o iterasyon atlanır. Bulunursa, link https://tr.wikipedia.org ile birleştirilir, çünkü çekilen linkler genellikle göreceli bir pathtir.
Her bir özellik için, sonunda bulunan yeni satır karakterleri ("\n") kaldırılır ve bu düzenlenmiş veri ilgili listeye (isimler, linkler, bölüm_adet, sezon_adet, durumlar, yayıncılar) eklenir.

Bu kod parçası, belirli bir web sayfasından veri toplamak ve düzenlemek için etkili bir yöntem sunar. Her adım, verilerin doğru ve kullanılabilir bir formatta toplanmasını sağlamak için dikkatlice tasarlanmıştır. elde edilen listeler, dizilerin isimleri, ilgili linkleri, bölüm sayıları, sezon sayıları, durumları ve yayıncı bilgilerini içeren yapılandırılmış veri setleri haline gelir. Bu veri seti, analiz, raporlama  ve bir veri bilimi uygulaması için kullanılabilir hale getirilmiştir. 


Bu Python script'i, bir Excel dosyasından okunan verileri kullanarak, belirli web sayfalarından daha fazla bilgi çekmek ve bu bilgileri düzenleyerek genişletilmiş bir veri seti oluşturmak için tasarlanmıştır. Kullanılan ana kütüphaneler requests, BeautifulSoup, ve pandas'tır.

Başlangıç ve Gerekli Kütüphaneler:
Imports: İlk olarak, HTTP istekleri için requests, HTML içeriği ayrıştırmak için BeautifulSoup, ve veri çerçeveleri ile çalışmak için pandas kütüphaneleri içe aktarılır.
Excel Dosyası Okuma: pd.read_excel("wiki_veriler.xlsx") komutu ile "wiki_veriler.xlsx" adlı Excel dosyasından veriler okunur ve excel_df adlı DataFrame'e atanır.

Veri Çekme ve İşleme Döngüsü:
Döngü Başlangıcı: for i in (range(len(excel_df))): döngüsü, excel_df DataFrame'indeki her bir satır için tekrarlanır. Bu, her bir dizi için ayrı ayrı işlem yapılacağı anlamına gelir.
HTTP İstekleri ve HTML Ayrıştırma:
requests.get(url) ile her bir dizinin sayfasından HTML içeriği çekilir.
BeautifulSoup(html_content, 'html.parser') kullanılarak HTML içeriği ayrıştırılır ve soup nesnesine dönüştürülür.
soup.find_all("table", class_ = "infobox") ile sayfada bulunan bilgi kutuları (infobox) bulunur.
Bilgi Kutularının İşlenmesi:
Try-Except Bloğu: Her bir bilgi kutusu için içerik çekme işlemi try-except bloğu içinde gerçekleştirilir. Eğer bir hata oluşursa, boş bir DataFrame oluşturulup, ana DataFrame'e eklenir.
Detay Bilgilerin Çekilmesi ve Düzenlenmesi:
Bilgi kutusundaki her bir satır (row) için, başlık (th) ve içerik (td) bilgileri çekilir.
Eğer bir satırda hem başlık hem de içerik varsa (yani hem th hem de td etiketleri bulunuyorsa), bu bilgiler işlenir.
Başlıklar ve içerikler, dizi_detay_bilgiler adlı bir sözlüğe kaydedilir. İçeriklerin daha karmaşık yapıları (örneğin birden fazla isim içeren yapılarda) BeautifulSoup ile işlenerek temizlenir ve düzenlenir.
Veri Çerçevesi Oluşturma ve Birleştirme:
DataFrame Oluşturma: Her bir dizi için, çekilen detay bilgileri içeren bir DataFrame (df) oluşturulur. Bu DataFrame'in index'i, o dizinin ismi olacak şekilde ayarlanır.
Ana DataFrame ile Birleştirme: Çekilen detay bilgileri içeren DataFrame, diziler_detaylar_df adlı ana DataFrame ile pd.concat kullanılarak birleştirilir. Bu işlem, tüm diziler için tekrarlanır ve sonunda genişletilmiş bir veri seti elde edilir.
Son Veri Setinin Oluşturulması:
Excel Verileri ile Detay Bilgilerin Birleştirilmesi: Orijinal Excel verileri (excel_df) ve çekilen detay bilgileri içeren diziler_detaylar_df, yine pd.concat kullanılarak birleştirilir. Bu, her bir dizi için hem orijinal Excel verilerini hem de yeni çekilen detay bilgileri içeren genişletilmiş bir veri seti oluşturur.

Sonuç:
Web scraping ve veri işleme teknikleri kullanılarak, her bir diziye ait detaylı bilgiler çekilir ve düzenli bir yapıda sunulur. Bu yöntem, veri bilimi, pazar araştırması, içerik analizi gibi alanlarda değerli içgörüler elde etmek için kullanılacaktır. 

Model

Projenin bu aşamasında, öncelikle elde edilen veri setindeki kategorik verilere label encoding uygulanmıştır. Daha sonra, bu veri seti üzerinde çeşitli sınıflandırma modelleri denenmiştir.

Label Encoding İşlemi:
Label Encoding Nedir: Label encoding, kategorik verileri sayısal değerlere dönüştürme işlemidir. Bu dönüşüm, makine öğrenimi modellerinin kategorik verileri işleyebilmesi için gereklidir, çünkü çoğu makine öğrenimi algoritması yalnızca sayısal verilerle çalışabilir.

Uygulama Süreci: Projede, Excel dosyasındaki kategorik veriler (örneğin, dizi isimleri, yayıncılar, durumlar gibi) label encoder kullanılarak sayısal değerlere dönüştürülmüştür. Python'un sklearn.preprocessing kütüphanesinden LabelEncoder sınıfı kullanılarak her bir benzersiz kategorik değer, benzersiz bir sayısal değere eşlenmiştir. Bu işlem, veri setindeki her bir kategorik sütun için tekrarlanmıştır.

Sınıflandırma Modellerinin Uygulanması:
Model Seçimi: Projede çeşitli sınıflandırma modelleri kullanılmıştır. Bunlar arasında Decision Tree Classifier, RandomForestClassifier ve XGBoost (XGBClassifier) gibi popüler ve etkili sınıflandırma algoritmaları bulunmaktadır. Her bir model, farklı sınıflandırma teknikleri ve yaklaşımları kullanır.

Model Eğitimi: Label encoding ile dönüştürülmüş veri seti, seçilen sınıflandırma modellerine beslenmiştir. Modeller, veri setini kullanarak dizi özelliklerine göre sınıflandırma yapmayı öğrenir. Bu süreçte, veri setinin bir kısmı modelin eğitimi için, diğer kısmı ise modelin performansını test etmek için ayrılmıştır (genellikle eğitim ve test seti olarak ayrılır).

Model Performansının Değerlendirilmesi: Her bir modelin performansı, genellikle doğruluk (accuracy), hassasiyet (precision), duyarlılık (recall) ve F1 skoru gibi metrikler kullanılarak değerlendirilmiştir. Bu metrikler, modelin sınıflandırma doğruluğunu ve genel etkinliğini ölçmek için kullanılır.

Sonuç:
Bu aşamada, projenin amacına uygun olarak, dizi verilerinin kategorik özellikleri sayısal değerlere dönüştürülerek makine öğrenimi modelleri için uygun hale getirilmiştir. Daha sonra, çeşitli sınıflandırma modelleri kullanılarak veri seti üzerinde sınıflandırma işlemi gerçekleştirilmiştir. Bu modellerin performansının değerlendirilmesi, hangi modelin veri seti için en uygun olduğunu belirlemeye yardımcı olmuştur. Bu süreç, veri bilimindeki tipik bir modelleme ve değerlendirme iş akışını temsil eder ve makine öğrenimi projelerinde sıkça kullanılan bir yöntemdir. Bu yaklaşım, hem veri setinin anlaşılmasını kolaylaştırır hem de veri bilimi projelerinde karşılaşılan gerçek dünya problemlerinin çözülmesine yardımcı olur.


Gelecekte Yapılabilecekler

1. Veri Setinin Genişletilmesi:
Daha Fazla Özellik Eklemek: Dizilerin başarısını etkileyebilecek daha fazla özelliği veri setine eklemek, modelin doğruluğunu artırabilir. Örneğin, dizi hakkındaki sosyal medya etkileşimleri, izleyici demografisi, bütçe bilgileri ve eleştirmen yorumları gibi veriler eklenebilir.
Zaman Serisi Verileri: Dizinin yayınlandığı süre boyunca reytinglerin ve sosyal medya etkileşimlerinin nasıl değiştiğini gösteren zaman serisi verileri de modeli geliştirebilir.
2. Yeni Modeller ve Algoritmalar Denemek:
Derin Öğrenme: CNN (Convolutional Neural Networks) veya RNN (Recurrent Neural Networks) gibi derin öğrenme modelleri, özellikle metin ve görüntü gibi karmaşık veri türleri için daha iyi sonuçlar verebilir.
Enseble Öğrenme Yöntemleri: Birden fazla modelin tahminlerini birleştiren Enseble yöntemler (örneğin, stacking veya boosting), genellikle tek bir modelden daha iyi performans gösterir.
3. Model İyileştirmeleri:
Hiperparametre Ayarlama: Modellerin hiperparametrelerini ayarlamak (örneğin, ağaç sayısı, öğrenme oranı), performansı önemli ölçüde etkileyebilir.
Özellik Mühendisliği: Mevcut verilerden daha anlamlı özellikler çıkarmak veya verileri farklı şekillerde kombinlemek, modelin daha iyi öğrenmesine yardımcı olabilir.
4. Model Değerlendirme Yöntemlerini Geliştirmek:
Çapraz Doğrulama: Veri setinin farklı bölümlerini kullanarak modeli değerlendirmek, modelin genelleştirme yeteneğinin daha iyi anlaşılmasını sağlar.
Farklı Metrikler Kullanmak: Doğruluk dışında hassasiyet, geri çağırma, F1 skoru gibi başka metriklerle model değerlendirilebilir. Ayrıca, iş probleminize özgü özel metrikler geliştirmek de faydalı olabilir.
5. Kullanıcı Geri Bildirimlerini Entegre Etmek:
İzleyici Geri Bildirimleri: İzleyicilerin yorumları ve puanlamaları, modelin daha gerçekçi tahminler yapmasını sağlayabilir.
Uzman Görüşleri: Sektör uzmanlarından alınacak geri bildirimler, hangi özelliklerin daha önemli olduğunu anlamada ve modelin doğruluğunu artırmada yardımcı olabilir.
6. Uygulama ve Görselleştirme Araçları Geliştirmek:
Kullanıcı Arayüzü: Modeli, son kullanıcılar için erişilebilir hale getirecek bir web arayüzü veya mobil uygulama geliştirmek.
Görselleştirmeler: Modelin tahminlerini ve performansını görselleştiren araçlar, sonuçları daha anlaşılır hale getirebilir.
Sonuç:
Bu projede geliştirilen model, televizyon dizilerinin başarısını tahmin etmek için önemli bir adımdır. Ancak, modelin sürekli olarak güncellenmesi, yeni veriler ve algoritmalarla denemeler yapılması, ve gerçek dünya uygulamalarına entegre edilmesi, projenin değerini ve etkisini artıracaktır. Ayrıca, etik ve yasal hususları göz önünde bulundurmak, modelin güvenilir ve sorumlu bir şekilde kullanılmasını sağlar. Bu öneriler, projenin gelecekteki yönlerini şekillendirmek ve dizilerin başarısını daha doğru bir şekilde tahmin etmek için değerli birer rehber olacaktır.



Giriş


Günümüzde, televizyon ve dijital yayın platformları, izleyicilere sayısız dizi ve program sunarak eğlence sektörünün önemli bir parçası haline gelmiştir. Bu çeşitlilik, sektördeki rekabeti arttırırken, yapımcılar ve yayıncılar için hangi dizilerin başarılı olacağını önceden tahmin etmek büyük bir zorluk teşkil etmektedir. Başarılı bir dizinin, yüksek izleyici sayıları, reklam gelirleri ve marka değeri gibi birçok olumlu sonucu olabilir. Bu nedenle, dizilerin potansiyel başarısını önceden belirleyebilen bir modelin geliştirilmesi, sektördeki karar vericiler için büyük bir avantaj sağlayabilir.

Bu rapor, televizyon dizilerinin başarısını tahmin etmeye yönelik bir veri bilimi projesini ele almaktadır. Proje, web scraping teknikleri kullanarak Wikipedia'dan dizilerle ilgili verilerin toplanması, bu verilerin ön işleme tabi tutulması, ve çeşitli sınıflandırma modelleri kullanarak dizilerin başarı durumlarının tahmin edilmesi süreçlerinden oluşmaktadır. Projenin amacı, veri bilimi ve makine öğrenimi tekniklerini kullanarak, dizi yapımcılarına ve yayıncılarına stratejik kararlarında rehberlik edecek bilgiler sağlamaktır.

Rapor, öncelikle projenin arka planını ve önemini açıklamakta, ardından kullanılan metodolojiyi ve elde edilen bulguları detaylı bir şekilde sunmaktadır. Son olarak, projenin gelecekteki gelişim yönleri ve potansiyel uygulamalarına dair önerilerde bulunmaktadır. Bu girişim, medya ve eğlence endüstrisinin karşı karşıya olduğu zorluklara yenilikçi çözümler getirme ve bu dinamik sektörde başarıyı öngörme yeteneğimizi artırma potansiyeline sahiptir.

Sonuçların Yorumlanması:

Projede uygulanan üç farklı sınıflandırma modelinin performanslarını değerlendirmek, bu modellerin dizilerin başarısını ne kadar iyi tahmin edebildiğini anlamamıza yardımcı olur. Modellerin performansları, doğruluk skoru (accuracy) kullanılarak ölçülmüştür; bu skor, modelin tahminlerinin gerçek değerlerle ne kadar sık doğru eşleştiğini gösterir. Elde edilen doğruluk skorları aşağıdaki gibidir:

Decision Tree Classifier: 0.5174
RandomForestClassifier: 0.6269
XGBClassifier: 0.6269
Decision Tree Classifier:
Karar Ağacı modelinin doğruluk skoru yaklaşık olarak 0.5174 olarak hesaplanmıştır. Bu skor, modelin %51.74 oranında doğru tahmin yapabildiğini gösterir. Bu oran, rastgele tahminlerden daha iyi olsa da, modelin çok sayıda yanlış tahmin yaptığını ve belirli bir güvenilirlik düzeyinin altında performans gösterdiğini göstermektedir. Karar ağaçlarının aşırı uyuma (overfitting) eğilimi ve veri setindeki karmaşıklıkları yeterince genelleştirememe gibi sorunlar bu düşük performansın olası nedenleri arasındadır.

RandomForestClassifier:
Rastgele Orman modeli, %62.69'luk bir doğruluk skoru ile Karar Ağacı modelinden önemli ölçüde daha iyi performans göstermiştir. Bu modelin daha yüksek performansı, birden fazla karar ağacının tahminlerini birleştirerek aşırı uyum sorununu azaltmasından ve daha kararlı tahminler yapmasından kaynaklanabilir. Ancak, bu modelin hala yaklaşık %37'lik bir hata oranı bulunmaktadır, bu da bazı önemli faktörlerin veya etkileşimlerin model tarafından yakalanamadığını gösterebilir.

XGBClassifier:
XGBoost, aynı %62.69'luk doğruluk skoru ile Rastgele Orman modeli ile eşit performans göstermiştir. Bu, gradient boosting tekniklerinin kullanımının, modelin veri setindeki karmaşık örüntüleri ve etkileşimleri öğrenmesine yardımcı olduğunu gösterir. Ancak, XGBoost'un da mükemmel olmadığı ve bazı durumlarda yanlış tahminler yapabildiği unutulmamalıdır.

Genel Değerlendirme:
Üç modelin de mükemmel olmadığı ve belirli bir hata oranı ile tahminler yaptığı görülmektedir. Bu, dizilerin başarısının çok sayıda faktöre bağlı olduğunu ve bu faktörlerin bazılarının model tarafından yakalanamamış olabileceğini göstermektedir. Ayrıca, veri setinin boyutu, kalitesi ve çeşitliliği gibi faktörler de modelin performansını önemli ölçüde etkileyebilir.

İleriye Dönük Öneriler:
Sonuçlar, daha iyi tahminler yapmak için modelin iyileştirilmesi gerektiğini göstermektedir. Bu, daha fazla veri toplamak, daha karmaşık ve çeşitli özellikler eklemek, modelin hiperparametrelerini ayarlamak ve alternatif modelleri değerlendirmek gibi adımları içerebilir. Ayrıca, modelin yanlış tahminler yaptığı durumları daha detaylı analiz etmek, hangi faktörlerin model tarafından yeterince öğrenilemediğini anlamak için faydalı olabilir.

