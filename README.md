# BIO Projekt

#### Dane:
http://www.cs.put.poznan.pl/mkasprzak/bio/testy.html

Wprowadzenie
Problemy sekwencjonowania łańcuchów DNA, z wykorzystaniem standardowych bibliotek oligonukleotydów o stałej długości i przy założeniu obecności odpowiednio błędów negatywnych lub pozytywnych w danych wejściowych, mogą zostać sformułowane następująco. Pojęcie "idealne spektrum" oznacza kompletny i bezbłędny zbiór słów o jednakowej długości l, które można wyodrębnić w sekwencji o długości n, gdzie l ≤ n.
Problem 1: Sekwencjonowanie łańcuchów DNA z błędami negatywnymi
Instancja: Zbiór S słów o jednakowej długości l nad alfabetem {A, C, G, T}, długość n sekwencji oryginalnej, przy czym S jest podzbiorem idealnego spektrum dla tej sekwencji.
Odpowiedź: Sekwencja o długości nie większej niż n zawierająca wszystkie słowa z S.
Problem 2: Sekwencjonowanie łańcuchów DNA z błędami pozytywnymi
Instancja: Zbiór S słów o jednakowej długości l nad alfabetem {A, C, G, T}, długość n sekwencji oryginalnej, przy czym S jest nadzbiorem idealnego spektrum dla tej sekwencji.
Odpowiedź: Sekwencja o długości n zawierająca n-l+1 słów z S.

Problem ogólny zakładający równocześnie obecność obu typów błędów (negatywnych i pozytywnych) w danych wejściowych może zostać sformułowany następująco.
Problem 3: Sekwencjonowanie łańcuchów DNA z błędami negatywnymi i pozytywnymi
Instancja: Zbiór S słów o jednakowej długości l nad alfabetem {A, C, G, T}, długość n sekwencji oryginalnej.
Odpowiedź: Sekwencja o długości nie większej niż n zawierająca maksymalną liczbę słów z S.
Zadanie
Projekt realizowany na zajęciach laboratoryjnych podzielony jest na dwa etapy, każdy zakończony oddaniem sprawozdania. Pierwszy etap polega na teoretycznym opracowaniu metody heurystycznej rozwiązującej optymalizacyjny problem 3. Metoda ma działać w wielomianowym czasie. W sprawozdaniu, oprócz opisu metody, należy dodatkowo zamieścić rozważania, jak można by zwiększyć jakość generowanych rozwiązań w przypadku dodatkowej wiedzy, że instancja zawiera błędy tylko jednego typu (negatywne lub pozytywne, problemy 1 i 2).

Drugi etap polega na zaimplementowaniu i przetestowaniu opracowanej wcześniej heurystyki dla problemu 3. Testy należy przeprowadzić co najmniej na obowiązkowych zbiorach instancji testowych. Mile widziane dodatkowe testy na instancjach wygenerowanych we własnym zakresie, zwłaszcza trudnych; proszę wtedy zwrócić uwagę na to, żeby kolejność podawanych algorytmowi słów była przypadkowa (nie podpowiadała rozwiązania). W sprawozdaniu należy zamieścić wyniki testów (czas obliczeń i jakość generowanych rozwiązań), porównanie działania heurystyki dla zbiorów testowych różniących się rodzajem zawartych błędów, wnioski obejmujące plusy i minusy zaproponowanego rozwiązania.

Projekt realizowany jest w grupach dwuosobowych, ewentualnie jednoosobowo. Program nie potrzebuje interfejsu graficznego, język implementacji dowolny. Sprawozdania należy oddawać wyłącznie na nośniku papierowym (wydrukowane bądź napisane odręcznie). Na ocenę wpłynie oryginalność i zaawansowanie metody, jakość generowanych rozwiązań oraz złożoność obliczeniowa algorytmu.
