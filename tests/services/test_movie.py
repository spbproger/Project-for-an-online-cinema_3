from unittest.mock import MagicMock

import pytest

from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    m1 = Movie(id=1, title="Йеллоустоун", description="", year=2010, rating=2)
    m2 = Movie(id=2, title="Омерзительная восьмерка", year=2020, rating=2, trailer="....")
    m3 = Movie(id=3, title="Семеро козлят", year=2020, rating=5.5, trailer="hsj")

    movie_dao.get_one = MagicMock(return_value=m1)
    movie_dao.get_all = MagicMock(return_value=[m1, m2])
    movie_dao.create = MagicMock(return_value=m3)
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()
    return movie_dao


class TestmovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie.id is not None
        assert movie.title == 'Йеллоустоун'

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie = {"name": "New Name"}
        new_movie = self.movie_service.create(movie)
        assert new_movie.id is not None
        assert new_movie.title == "Семеро козлят"
        assert new_movie.rating == 5.5

    def test_update(self):
        movie = self.movie_service.update(1)

    def test_delete(self):
        res = self.movie_service.delete(1)
        assert res is None
