import random #Napisz swoją pierwszą gre. 

imie = input("Podaj imie: ")    #1 Użytkownik podaje imię

dolna_granica = int(input(str(imie) + "! Podaj dolny zakres liczb z których chcesz losować "))  #2 Program prosi użytkownika o podanie zakresu liczb w jakim chce grać, zwracając się do niego po imieniu
gorna_granica = int(input(str(imie) + "! Podaj górny zakres liczb z których chcesz losować "))
    
liczba_wylosowana = random.randint(dolna_granica, gorna_granica)                                #3 Program generuje liczbę całkowitą z zakresu podanego przez użytkownika

#print(liczba_wylosowana) #linijka kodu pomagająca sprawdzić czy warunki do zgadywania dobrze działały 

ilosc_prob = 0      #Deklaracja zmiennej odpowiedzialnej za ilość prób

while True:

    liczba_zgadywana = input(str(imie) + ", podaj szacową liczbę lub wciśnij X aby się poddać! ") #4 Program prosi użytkownika o podanie liczby

    ilosc_prob += 1                                 #inkrementacja ilości wprowadzanych liczb 

    if str(liczba_zgadywana) == "x":                #Jeśli użytkownik podał 'X', program informuje o poddaniu gry przez użytkownika i kończy ją
        print("\nKoniec gry. Frajer :P ")
        break

    if not liczba_zgadywana.isdigit():              #Program sprawdza czy wprowadzona wartość zmiennej jest liczbą
        print("\nTo nie jest liczba! Spróbuj ponownie.\n ")
        continue

    liczba_zgadywana = int(liczba_zgadywana) #Konwercja wartości zmiennej na intiger 

    if liczba_zgadywana < dolna_granica or liczba_zgadywana > gorna_granica:   #Jeśli użytkownik podał liczbę spoza zakresu początkowego, program informuje o tym i prosi o podanie nowej liczby
        print("\nPodana liczba nie mieści się w zakresie! Spróbuj ponownie.\n ")
        continue

    if liczba_zgadywana < liczba_wylosowana:        #Jeśli użytkownik trafił w liczbę większą od wygenerowanej, program informuje, że podana liczba jest zbyt duża
        print("\nzgadywna liczba jest większa\n" )
        continue
        
    
    elif liczba_zgadywana > liczba_wylosowana:      #Jeśli użytkownik trafił w liczbę mniejszą od wygenerowanej, program informuje, że podana liczba jest zbyt mała
        print("\nzgadywna liczba jest mniejsza\n" )
        continue
        
    
    elif liczba_zgadywana == liczba_wylosowana:     #Jeśli użytkownik trafił - wygrywa, program wyświetla informację z gratulacjami i liczbą kroków, w których doszedł do wygranej
        print("""
    ################################################
    ## *** WOW! GRATULACJE ZA PRZEJŚCIE GRY! ***  ##
    ################################################
    ## *** TWOJE UMIEJĘTNOŚCI SĄ NIESAMOWITE! *** ##    
    ################################################
    ### *** ZASŁUŻYŁEŚ NA CHWAŁĘ I SZACUNEK! *** ###
    ################################################
    """)                                                            #Prawdziwy interface xD
        
        wynik = 1000 + 25 - (25 * ilosc_prob)       #Skoro to gra to wporwadziłem wynik w punktach
        
        print("         Twój wynik wynosi = " + str(wynik) + " punków!!!")

        if ilosc_prob == 1:
        
            print("               w zaledwie " + str(ilosc_prob) + " próbę!!\n")

        elif ilosc_prob < 1 and ilosc_prob >= 4:                                            #Niuanse języka polskiego

            print("               w zaledwie " + str(ilosc_prob) + " próby!!\n")

        else:

            print("               w zaledwie " + str(ilosc_prob) + " prób!!\n")

        break 
