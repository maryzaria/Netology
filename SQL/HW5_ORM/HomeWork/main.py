import json
import os

from dotenv import load_dotenv
from sqlalchemy import or_, create_engine
from sqlalchemy.orm import sessionmaker

from models import *

load_dotenv()
db = os.getenv('DB')
user_name = os.getenv('USER_NAME')
user_password = os.getenv('USER_PASSWORD')
host = 'localhost:5432'
db_name = 'booksale_db'
DSN = f'{db}://{user_name}:{user_password}@{host}/{db_name}'
engine = create_engine(DSN)
create_table(engine)
Session = sessionmaker(bind=engine)


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


def num_of_spaces(query):
    max_title = len(max(query, key=lambda x: len(x[0].title))[0].title)
    max_shop = len(max(query, key=lambda x: len(x[1].name))[1].name)
    max_price = len(str(max(query, key=lambda x: len(str(x[2].price)))[2].price))
    return max_title, max_shop, max_price


def main():
    session = Session()
    if not session.query(Publisher).first():
        load_data_to_db(session, 'tests_data.json')

    # publisher = 'O’Reilly'
    publisher = input('Введите имя или идентификатор автора: ')

    try:
        publisher_id = int(publisher)
    except ValueError:
        publisher_id = -1

    query = session.query(Book, Shop, Sale). \
        select_from(Publisher).join(Book).join(Stock).join(Sale).join(Shop). \
        filter(or_(Publisher.id == publisher_id, Publisher.name.like(f'{publisher}'))).all()

    t, s, p = num_of_spaces(query)

    for book, shop, sale in query:
        print(
            f'{book.title.ljust(t, " ")} | {shop.name.ljust(s, " ")} | {str(sale.price).ljust(p, " ")} | {sale.date_sale}')

    session.commit()
    session.close()


if __name__ == '__main__':
    main()

