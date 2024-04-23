class Film:
    def __init__(self, judul, rilis, director):
        self.judul = judul
        self.rilis = rilis
        self.director = director

films = [
    Film("avengers end game", 2019, "Anthony Russo"),
    Film("batman dark knight", 2008, "Christopher Nolan"),
    Film("interstellar", 2014, "Christopher Nolan"),
    Film("Aquaman", 2018, "James Wan"),
    Film("spiderman no way home", 2021, "Jon Watts")
]

print("-----Elkom 2-----")

for i, film in enumerate(films, start=1):
    print(f"Film favorit ke-{i}:")
    print(f"Judul: {film.judul}")
    print(f"Rilis: {film.rilis}")
    print(f"Director: {film.director}")
    if i < len(films):
        print("=" * 20)
