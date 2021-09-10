class Movies:
    def __init__(self, title: str, genre: str, mainLanguage: str, director: str, releaseYear: int) -> None:
        self.title = title
        self.genre = genre
        self.mainLanguage = mainLanguage
        self.director = director
        self.releaseYear = releaseYear
    
    def __str__(self) -> str:
        return "Title = %s, genre = %s, main_language = %s, director = %s, release_year = %s" % (self.title, self.genre,
        self.mainLanguage, self.director, self.releaseYear);
    
    def setGenre(self, newGenre: str) -> None:
        allowedGenres = {'Romance', 'Action', 'Drama', 'Thriller', 'Horror'}
        if newGenre not in allowedGenres:
            print('Invalid new genre. Please try a different genre!')
            return
        self.genre = newGenre
    
    def getGenre(self) -> str:
        return self.genre
    
    def recommendMovies(self) -> str:
        if self.genre == 'Action': return 'Mutant'
        if self.genre == 'Romance': return 'First Date'
        if self.genre == 'Thriller': return 'Mr. K'
        if self.genre == 'Drama': return 'The Awakening'
        
        return 'A walk down Dowson Stree'

movie = Movies('And so it begins', '', 'English', 'Robert Joe', 2019)

print(movie)

# movie.setGenre('Fantasy')
movie.setGenre('Romance')
print(movie)
print(movie.recommendMovies())