import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, PrimaryKeyConstraint, ForeignKey
from sqlalchemy import insert , select
from sqlalchemy import create_engine

print(sqlalchemy.__version__)


engine = create_engine('sqlite:///sqlitedb.db', echo=True)

metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name',String),
              Column('age',Integer )
              )
addresses = Table('addresses',metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', None ,ForeignKey('users.id'), nullable=False),
                  Column('email',String(50),nullable=False)
                  )
#metadata.clear()
#metadata.drop_all(engine)
#users.drop(engine)
addresses.drop(engine)
metadata.create_all(engine)



conn = engine.connect()

conn.execute(addresses.delete())
conn.execute(users.delete())


s = select([users])
result = conn.execute(s)
for row in result:
    print(row)

a = select([addresses])
result = conn.execute(a)
for row in result:
    print(row)


for row in conn.execute(select([users,addresses])):
    print(row)

for row in conn.execute(select([users,addresses]).where(users.c.id == addresses.c.user_id)):
    print(row)
result.close()
