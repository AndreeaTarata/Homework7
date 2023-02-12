Obiective Întâlnire 7

● Să știm ce e o excepție și cum o ‘tratăm’
● Să înțelegem cei 4 piloni ai OOP
○ Encapsulare
○ Moștenire
○ Abstractizare
○ Polimorfism

Excepții

● Situații când codul nu poate executa instrucțiunile
● În acest caz codul ‘aruncă’ o excepție
● Programatorii se pot aștepta la ea, pot să o ‘prindă’ și să o ‘trateze’
● În acest sens putem anticipa erori și evităm să ‘crape’ aplicația
● Se folosește sintaxa try/except
● Uneori dorim să ‘ridicăm’ o excepție intenționat

Inheritance

● O clasă părinte poate fi moștenită de oricâte clase copil
● Aceste clase copil vor avea acces la toate atributele și metodele clasei părinte

Polymorphism

● Când există 2 funcții cu același nume dar au comportament diferit

Abstraction

● O clasă abstractă conține metode fără corp dar și metode cu logică definită
● O Interfață conține doar metode abstracte
● Aceste clase vor fi moștenite de clasele copil care vor trebui să scrie logica metodelor
● “Dog() class implements the Animal() Inteface”
● Clasa părinte e că o rețetă ce trebuie implementată exact așa de către toți moștenitorii

Encapsulation

● În general, că să nu aglomerăm opțiunile utilizatorului, atributele se ascund
● În loc să vadă toate fields și methods va vedea doar metodele
● Păstrăm codul clean/curat
● Și metodele care nu se doresc a fi expuse pot fi ascunse
● Se folosește sintaxa __fieldName sau __methodName

Encapsulation (optional)

● Decoratorul @property ne ajută să folosim getter, setter, deleter într-un mod ‘Pythonic’

Întrebări & curiozități?

j

Întrebări de interviu:
➢ Ce sunt excepțiile și când apar ?
➢ Ce este Polymorphism-ul ?
➢ La ce ne ajuta Encapsulation ?
➢ Ce este Abstraction ?