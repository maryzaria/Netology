import os
from dotenv import load_dotenv
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker

from models import create_table, Course, Homework


load_dotenv()
user_name = os.getenv('USER_NAME')
user_password = os.getenv('USER_PASSWORD')
DNS = f'postgresql://{user_name}:{user_password}@localhost:5432/netology_db'

# абстракция для подключения к БД, движок
engine = sq.create_engine(DNS)

create_table(engine)

# Сессия - способ подключения к БД (аналог курсора)

Session = sessionmaker(bind=engine)  # класс
session = Session()
# сессия хочет работать с моделями
# создание данных
course1 = Course(name='Python')

session.add(course1)
session.commit()
# print(course1)
hw1 = Homework(number=1, description="первое задание (простое)", course=course1)
hw2 = Homework(number=2, description="второе задание (сложное)", course=course1)
session.add_all([hw1, hw2])
session.commit()

# извлечение данных
# for c in session.query(Homework).all():
#     print(c)
#
# фильтруем данные
# for c in session.query(Homework).filter(Homework.number > 1).all():
    # print(c)
# фильтруем данные
# for c in session.query(Homework).filter(Homework.description.like('%прост%')).all():
#     print(c)

# объединение таблиц
# for c in session.query(Course).join(Homework.course).filter(Homework.number == 2).all():
#     print(c)

# вложенные подзапросы
course2 = Course(name='Java')
session.add(course2)
session.commit()

# подзапрос, результаты подзапроса хранятся в атрибуте c (subq.c)
subq = session.query(Homework).filter(Homework.description.like('%сложн%')).subquery()
# for c in session.query(Course).join(subq, Course.id == subq.c.course_id):  # таблица и условие объединения
    # print(c)

# обновление и удаление объектов
session.query(Course).filter(Course.name == 'Java').update({'name': 'JavaScript'})
session.commit()

# for c in session.query(Course).all():
#     print(c)

session.query(Course).filter(Course.name == 'JavaScript').delete()
session.commit()

# for c in session.query(Course).all():
#     print(c)

session.close()