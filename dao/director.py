from dao.model.director import Director


#Слой связи с БД для Режиссера
class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        """Информация об режиссере по id"""
        return self.session.query(Director).get(bid)

    def get_all(self):
        """Информация о всех режиссерах"""
        return self.session.query(Director).all()

    def create(self, director_d):
        """Создание нового режиссера"""
        entity = Director(**director_d)
        self.session.add(entity)
        self.session.commit()
        return entity

    def delete(self, rid):
        """Удалить режиссера по id"""
        director = self.get_one(rid)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_d):
        """Обновить режиссера"""
        director = self.get_one(director_d.get("id"))
        director.name = director_d.get("name")
        self.session.add(director)
        self.session.commit()
