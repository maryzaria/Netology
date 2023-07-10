import os
import json
from dotenv import load_dotenv
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_

from HW5_sqlalchemy_models import *


def load_data_to_db(session, filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    models = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale
    }

    for line in data:
        model = models[line.get('model')]
        example = model(id=line.get('pk'), **line['fields'])
        session.add(example)
    session.commit()


if __name__ == '__main__':
    load_dotenv()
    db = os.getenv('DB')
    user_name = os.getenv('USER_NAME')
    user_password = os.getenv('USER_PASSWORD')
    host = 'localhost:5432'
    db_name = 'booksale_db'
    DSN = f'{db}://{user_name}:{user_password}@{host}/{db_name}'
    engine = sq.create_engine(DSN)
    create_table(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    load_data_to_db(session, 'tests_data.json')

    # publisher = 'O’Reilly'
    publisher = input('Введите имя или идентификатор автора: ')
    try:
        publisher_id = int(publisher)
    except ValueError:
        publisher_id = -1

    query = session.query(Book, Stock, Sale, Shop).\
        select_from(Publisher).join(Book).join(Stock).join(Sale).join(Shop).\
        filter(or_(Publisher.id == publisher_id, Publisher.name.like(f'{publisher}'))).all()

    max_title = len(max(query, key=lambda x: len(x[0].title))[0].title)
    max_shop = len(max(query, key=lambda x: len(x[3].name))[3].name)

    for book, stock, sale, shop in query:
        print(f'{book.title.ljust(max_title, " ")} | {shop.name.ljust(max_shop, " ")} | {str(sale.price).ljust(5, " ")} | {sale.date_sale}')

    session.commit()
    session.close()
