Bilgisayar Uygulamalarında Çizge Kuramı

Proje

Python dilinde yazılacak programda aşağıdakiler uygulanacaktır. Herhangi bir kütüphane

kullanılmayacaktır. Raporunuzu https://www.overleaf.com/latex/templates/latex-template-for-technical-

report/qtznkrpkjybm linkindeki teknik rapor formatında yazınız ve kodlarınızı paylaşınız.

1. Program iki şekilde alabilmelidir.

Örnek Komşuluk Matrisi (tab ile birbirinden ayrılmıştır.) İlk satırda Matrix kelimesi yazılacaktır. M

karakteri korunacaktır.

Matrix

M a b c d

a 0 1 0 1

b 1 0 1 1

c 0 1 0 0

d 1 1 0 0

Örnek Komşuluk Listesi (ilk karakterden sonra belirtilen karakterler ilk karakter ile belirtilen tepeye bağlı

olan tpeleri göstermektedir.) Tab ile birbirlerinden ayrılmıştır. Yukarıdaki örnek ile aynıdır. İlk satırda List

kelimesi yazılacaktır.

List

a b d

b a c d

c b

d a b

a. Girdi txt dosyası kullanarak “komşuşuk matrisi (adjacency matrix)” veya “komşuluk listesi

(adjacency list)” formatında çizge topolojisi alınacaktır. Program her iki girdiyi alabilmelidir.

b. Tepe sayısı (vertex) ve ayrıt (edge) sayısı girdi olarak alınacak ve çizge topolojisi rasgele bu

değerler kullanılarak oluşturulacaktır.

2. Çizge topolojisi hem “komşuşuk matrisi (adjacency matrix)” hem de “komşuluk listesi (adjacency

list)” formatında bir txt dosyasına aynı formatında yazılabilmelidir.

3. Soyutlanmış (isolated) tepeleri bulunuz.

4. Asılı (pendant) tepeleri bulunuz.5. 6. 7. 8. 9. Veriğen bir 𝑛 değeri için tam (complete) çizge oluşturunuz. 𝐾𝑛 , 𝑛 >= 1

Veriğen bir 𝑛 değeri için döngü (cycle) çizge oluşturunuz. 𝐶𝑛 , 𝑛 >= 3

Veriğen bir 𝑛 değeri için çark (wheel) çizge oluşturunuz. 𝑊 𝑛 , 𝑛 >= 3

Veriğen bir 𝑛 değeri için 𝑛-küp (𝑛-cube) çizge oluşturunuz. 𝑄𝑛 , 𝑛 >= 1

Bir çizgenin tam (complete), döngü (cycle), çark (wheel) veya 𝑛-küp (𝑛-cube) olduğunu belirleyiniz.

Hiçbiri değilse, bunlar olmadığı belirtilmelidir.

10. Verilen bir çizgenin iki parçalı (bipartite) bir çizge olup olmadığını, öyle ise iki kümenin tepelerini

belirtiniz.

11. Verilen bir çizgenin iki parçalı tam (bipartite complete) bir çizge olup olmadığını, öyle ise iki kümenin

tepelerini belirtiniz.

12. Verilen bir çizgenin bağlı (connected) bir çizge olup olmadığını bulunuz. Değil ise, birbirinden ayrı

tepe kümelerini bulunuz.

13. Verilen iki çizgenin tepe, sayısı, ayrıt sayısı, tepelerin dereceleri gibi temel bilgileri kullana