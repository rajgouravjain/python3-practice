from sqlalchemy import Table, Column, Integer, MetaData, String, ForeignKey
from sqlalchemy import insert, select

from sqlalchemy import create_engine

engine = create_engine('sqlite:///sqlitedb.db',echo=True)
metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name',String),
              Column('age',Integer)
              )

addresses = Table('addresses',metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', None , ForeignKey('users.id'),nullable=False),
                  Column('email',String(50),nullable=False)
                  )

ins = users.insert()
ins_rajgourav = ins.values(id=1,name="Rajgourav1",age=32)


conn = engine.connect()
result = conn.execute(ins_rajgourav)

ins = addresses.insert().values(id=1,user_id=1, email="rajgourav1@gmail.com")

result = conn.execute(ins)


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

