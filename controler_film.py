import biblioteca_de_filme
import class_film


# controler - gereaza obiectele


# BibliotecaNostra = BibliotecaDeFilme()
# movie1 = class_film.Movie('John Wick', 2020, 'action', 7.1 )
# BibliotecaNostra.add_movie(movie1)
# movie2 = class_film.Movie('Fast and Furious X',2022, 'Fantasy', 3.9)
# BibliotecaNostra.add_movie(movie2)
# movie3 = class_film.Movie('KonguFuPanda',2000,'horror', 8.2) <!!!!!!!!!!!!!!!!!!!!!!!!!>
# BibliotecaNostra.add_movie(movie3)
#
# BibliotecaNostra.show_all_movie()
#
# BibliotecaNostra.update_nota_for_a_movie("KonguFuPanda",1.8)  <!!!!!!!!!!!!!!!!!!!!!!!!!>
# BibliotecaNostra.show_all_movie()


def creaza_biblioteca_noastra():
    BibliotecaNostra = biblioteca_de_filme.BibliotecaDeFilme()
    return BibliotecaNostra

def adaugam_film_in_biblioteca_noastra(biblioteca, filmul):
    return biblioteca.add_movie(filmul)

# vrem sa afisam toate filmele dintro biblioteca

def aratam_biblioteca(biblioteca):
    biblioteca.show_all_movie()   #afisam filmele dintr-o biblioteca

def modificam_nota_film_specific(biblioteca, numele_film, notaNoua):
    if notaNoua <= 0:
        print(f'eroare, introduceti alta nota')
    elif notaNoua > 10:
        print(f'Nota este prea mare, reintroduceti nota')
    else:
        biblioteca.update_nota_for_a_movie(numele_film, notaNoua)

def creaza_film(name, year, category, nota):
    if nota <= 0:
        print(f'eroare, introduceti alta nota')
    elif nota > 10:
        print(f'Nota este prea mare, reintroduceti nota')
    else:
        film = class_film.Movie(name, year, category, nota)
        return film






