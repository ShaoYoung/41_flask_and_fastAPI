import databases
import sqlalchemy
from settings import settings

db = databases.Database(settings.DATABASE_URL)
metadata = sqlalchemy.MetaData()
users = sqlalchemy.Table('users', metadata,
                         sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column('username', sqlalchemy.String(32)),
                         sqlalchemy.Column('surname', sqlalchemy.String(32)),
                         sqlalchemy.Column('email', sqlalchemy.String(128)),
                         sqlalchemy.Column('password', sqlalchemy.String(128)),
                         )

products = sqlalchemy.Table('products', metadata,
                            sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
                            sqlalchemy.Column('product_name', sqlalchemy.String(128)),
                            sqlalchemy.Column('description', sqlalchemy.String(256)),
                            sqlalchemy.Column('price', sqlalchemy.Integer),
                            )

orders = sqlalchemy.Table('orders', metadata,
                          sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
                          sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'),
                                            nullable=False),
                          sqlalchemy.Column('product_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('products.id'),
                                            nullable=False),
                          sqlalchemy.Column('order_date', sqlalchemy.Date, nullable=False),
                          sqlalchemy.Column('status', sqlalchemy.String(32)),
                          )

# движок
engine = sqlalchemy.create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False})
# создание таблиц
metadata.create_all(engine)
