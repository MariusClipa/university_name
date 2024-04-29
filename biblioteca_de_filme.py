import class_film


class BibliotecaDeFilme :
    def __init__(self):
        self.movie = []

    def add_movie(self, new_movie):
        film = self.movie.append(new_movie)
        return film

    def show_all_movie(self):
        for movie in self.movie:
            print(movie.details_movie())

    def update_nota_for_a_movie(self, name, notaToUpdate):
        global to_update_movie
        for movie in self.movie:
            if movie.name == name:
                to_update_movie = movie
                to_update_movie.update_nota(notaToUpdate)
                print(f"am udatat nota")
            else:
                to_update_movie = None
                print(f"error")



# carti






