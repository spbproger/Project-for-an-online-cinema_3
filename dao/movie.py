from dao.model.movie import Movie

#Слой связи с БД для Фильма
class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        """Информация о жанре по id"""
        return self.session.query(Movie).get(bid)

    def get_all(self):
        """Информация о всех фильмах"""
        return self.session.query(Movie).all()

    def create(self, movie_d):
        """Создать новый ффильм"""
        entity = Movie(**movie_d)
        self.session.add(entity)
        self.session.commit()
        return entity

    def delete(self, rid):
        """УДалить фильм по id"""
        movie = self.get_one(rid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_d):
        """Обновить информацию о фильме"""
        movie = self.get_one(movie_d.get("id"))
        movie.title = movie_d.get("title")
        movie.description = movie_d.get("description")
        movie.trailer = movie_d.get("trailer")
        movie.year = movie_d.get("year")
        movie.rating = movie_d.get("rating")
        movie.genre_id = movie_d.get("genre_id")
        movie.director_id = movie_d.get("director_id")

        self.session.add(movie)
        self.session.commit()
