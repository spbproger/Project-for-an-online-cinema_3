from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name="John")
    d2 = Director(id=2, name="Bill")
    d3 = Director(id=3, name="Alex")

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2])
    director_dao.create = MagicMock(return_value=d3)
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()
    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        users = self.director_service.get_all()
        assert len(users) > 0

    def test_create(self):
        director = {"name": "New Name"}
        new_director = self.director_service.create(director)
        assert new_director is not None

    def test_update(self):
        director = self.director_service.update(1)

    def test_delete(self):
        res = self.director_service.delete(1)
        assert res is None
