# clasa film sa aiba nume, an = int, categoria = str, nota
# media dintre nota actuala si nota precedenta

class Movie:
    def __init__(self, name: object, year: object, category: object, nota: object) -> object:
        self.name = name
        self.year = year
        self.category = category
        self.nota = nota

    def details_movie(self):
        return f"{self.name} launched in {self.year} from category {self.category} with {self.nota}"

    def update_nota(self, new_nota):
        final_nota = float((new_nota + self.nota) / 2)
        self.nota = float(final_nota)
        return {self.nota}




