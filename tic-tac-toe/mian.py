import pygames

define loopCheck(Tablica : Array(int) -> bool :
    i = 0
    for Tablica[i]:
        if Tablica[i] == 0:
            wyswietl(x)
        else:
            wyswietl(y)
    if i%0 == 1 :
        print"ruch lrzyżyka"
    else:
        print"ruch kółka"
    i = i+1




define wyswietl(a char) -> None
    #funckja ma wyświetlać odpowiednio