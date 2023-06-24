'''
1. Pobierz tekst od użytkownika 
2. Zapisz każdy znak osobono w tablicy, chyba że jest to '-' -> wtedy to znak minus
3. Zamień tablicę tak, aby zostały uniklane znaki
4. z tego, co powstało wyświetl:

    - A. Sumę liczb dodatnich 

    - B. Słowo powstałe z liter, które zostały 

    - C. Liczbę tych liter 

5. Po skończeniu zapytaj, czy użytkonwik chce kolejne słowo 
6. Jeśli tak -> zacznij od 1. Jeśli nie -> zakończ 
'''

while True:
    tekst = input("Podaj tekst do sprawdzenia: ")
    tablica = []
    i = 0

    while i < len(tekst):
        znak = tekst[i]
        if znak == '-':
            if i + 1 < len(tekst) and tekst[i + 1].isdigit():
                znak = '-' + tekst[i + 1]
                i += 1
        if znak not in tablica:
            tablica.append(znak)
        i += 1

    print(tablica)


    suma = 0
    slowo = ""
    ilosc = 0
    
    for znak in tablica:
        if znak.isdigit() and int(znak) > 0:
            suma += int(znak)
        elif znak.isalpha():
            slowo += znak
            ilosc += 1
    
    print("- A. Suma liczb dodatnich:", suma)
    print("- B. Słowo powstałe z liter, które zostały:", slowo)
    print("- C. Liczba tych liter:", ilosc)

    wybor = input("Czy chcesz wprowadzić kolejny tekst? (tak/nie): ")
    if wybor != 'tak':
        break