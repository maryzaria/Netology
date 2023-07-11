import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship


# Модель - спец. класс, который является наследником базового класса Base,
# который создается с помощью функции declarative_base()
# он умеет регистрировать всех своих наследников и может создать в БД соотв. таблицы
Base = declarative_base()


class Course(Base):
    __tablename__ = "course"  # название таблицы, которая будет создана в postgres
    # далее перечислены атрибуты, колонки в таблице
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)
    # связи между таблицами:
    # homeworks = relationship("Homework", back_populates="course")

    def __str__(self):
        return f'Course{self.id}: {self.name}'


class Homework(Base):
    __tablename__ = "homework"

    id = sq.Column(sq.Integer, primary_key=True)
    number = sq.Column(sq.Integer, nullable=False)
    description = sq.Column(sq.Text, nullable=False)
    # sq.ForeignKey("course.id") - ограничение внешнего ключа
    course_id = sq.Column(sq.Integer, sq.ForeignKey("course.id"), nullable=False)

    # course = relationship(Course, back_populates="homeworks")
    # relationship описывает, с какой таблицей мы хотим связаться (Course)
    # back_populates - обратное свойство (по которому связываем), необходио указать в обеих связываемых таблицах - неудобно
    # backref - автоматически создает свойство в связываемой таблице
    course = relationship(Course, backref="homeworks")

    def __str__(self):
        return f'Homework{self.id}: ({self.description}, {self.course_id})'


def create_table(engine):
    Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)
    # не создает повторно таблицы
    # drop_all - удаление всех существующих таблиц