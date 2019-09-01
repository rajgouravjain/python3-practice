from sqlalchemy import Table, Column, Integer, MetaData, String, ForeignKey
from sqlalchemy import insert, select, update
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
engine = create_engine('mysql://rjain:pass@123@localhost:3306/learning', poolclass= QueuePool, pool_size = 5, max_overflow=0, pool_recycle=3600, echo=True)

metadata = MetaData()

users = Table('users', metadata,
             Column('id', Integer, primary_key=True),
             Column('name',String(20)),
             Column('age',Integer)
             )

addresses = Table('addresses',metadata,
                 Column('id', Integer, primary_key=True),
                 Column('user_id', None , ForeignKey('users.id'),nullable=False),
                 Column('email',String(50),nullable=False)
                 )

#metadata.clear()
#metadata.drop_all(engine)
#users.drop(engine)
#addresses.drop(engine)
metadata.create_all(engine)

conn = engine.connect()
##connection = engine.contextual_connect()
def call_operation1():
    ins = users.insert()
    ins_rajgourav = ins.values( name="Rajgourav1", age=32)
    result = conn.execute(ins_rajgourav)


def call_operation2():
    ins = addresses.insert().values(id=0, user_id=1, email="rajgourav1@gmail.com")
    result = conn.execute(ins)


tran = conn.begin()
try:
    call_operation1()
    call_operation2()
    tran.commit()
except:
    tran.rollback()



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
##connection.close()
