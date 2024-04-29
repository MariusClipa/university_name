####
###

import controler_film


#cream o biblioteca
Biblioteca1 = controler_film.creaza_biblioteca_noastra()




#key : 1/2/3


while True:
    print(f"Bine ai venit, apasa \n 1. daca vrei sa vezi lista de filme dintr-o biblioteca \n"
          f"2. Daca vrei sa creezi film \n"
          f"3. daca vrei sa notezi un film cu o nota de la 0 la 10")
    key = int(input())
    if key == 1:
        controler_film.aratam_biblioteca(Biblioteca1)
        print("1")
    elif key == 2:
        numefilme = input("Da un nume la film")
        anFilm = input("Da anul de lansare a filmului")
        categoriaFilmului = input('Din ce categorie este filmul?')
        notaFilmului = float(input('Ce nota dai filmului?'))
        film = controler_film.creaza_film(numefilme, anFilm, categoriaFilmului, notaFilmului)
        controler_film.adaugam_film_in_biblioteca_noastra(Biblioteca1, film)
    elif key == 3:
        numeFilm = input('Numele filmului : ')
        notaNoua = float(input('Nota Noua a filmului : '))
        controler_film.modificam_nota_film_specific(Biblioteca1, numeFilm, notaNoua)
    else:
        break
