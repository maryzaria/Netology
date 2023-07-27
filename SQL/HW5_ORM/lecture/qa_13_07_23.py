

from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import datetime as dt
from sqlalchemy import or_
engine = sq.create_engine('postgresql://postgres:admin@localhost:5432/netology_bd')


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    
    id = sq.Column(sq.BigInteger, primary_key=True)
    username = sq.Column(sq.String(50), unique=True)
    
    favourite_notes = relationship('Note', secondary='favourites', back_populates='favourite_users')
    
    def __str__(self):
        return f'User: {self.username}'
    

class Note(Base):
    __tablename__ = 'notes'
    
    id = sq.Column(sq.BigInteger, primary_key=True)
    text = sq.Column(sq.UnicodeText, nullable=False)
    public = sq.Column(sq.Boolean, default=False)
    created_at = sq.Column(sq.DateTime, default=dt.datetime.now)
    author_id = sq.Column(sq.BigInteger, sq.ForeignKey('users.id', ondelete='CASCADE'))
    
    author = relationship('User', backref='notes')
    
    favourite_users = relationship('User', secondary='favourites', back_populates='favourite_notes')
    
    def __str__(self):
        return f'Note: {self.text}'
    

favourites = sq.Table(
    'favourites', Base.metadata,
    sq.Column('user_id', sq.BigInteger, sq.ForeignKey('users.id', ondelete='CASCADE')),
    sq.Column('note_id', sq.BigInteger, sq.ForeignKey('notes.id', ondelete='CASCADE'))
)   


class Service:
    def __init__(self, session):
        self.session = session
        
    def create_user(self, username):
        user = User(username=username)
        self.session.add(user)
        self.session.commit()
        
        return user
    
    def create_note(self, author, text, public=False):
        note = Note(text=text, author_id=author.id, public=public)
        self.session.add(note)
        self.session.commit()
        
        return note    
    
    def list_notes(self, user):
        return self.session.query(Note).join(User).filter(
        or_(Note.public==True, User.id==user.id)).all()
        
        
def create_tables(session, engine):
    with engine.connect() as con:
        con.execute('DROP TABLE IF EXISTS notes CASCADE')
        con.execute('DROP TABLE IF EXISTS users CASCADE')
        con.execute('DROP TABLE IF EXISTS favourites CASCADE')
    Base.metadata.create_all(engine)
    
Session = sessionmaker(bind=engine)

with Session() as session:
    create_tables(session, engine)
    service = Service(session)
    user1 = service.create_user('user1')
    user2 = service.create_user('user2')
    
    note1 = service.create_note(user1, 'some public note1', True)
    note2 = service.create_note(user2, 'some public note2', True)
    note3 = service.create_note(user2, 'some private note2', False)
    
    for n in service.list_notes(user1):
        print(n)
        
    print('----------------')
    
    for n in service.list_notes(user2):
        print(n)
        








# In[18]:


import pandas as pd

engine = sq.create_engine('postgresql://postgres:admin@localhost:5432/netology_bd')
con = engine.connect()

data = pd.read_csv('diabetes.csv')
# data


# In[19]:


data.to_sql(name='diabets', con=con, index=False, if_exists='replace')



# In[20]:


df = pd.read_sql('select * from diabetes', con)

# df



pd.DataFrame()

