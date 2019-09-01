import asyncio
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy import MetaData

from aiomysql.sa import create_engine


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
loop = asyncio.get_event_loop()

@asyncio.coroutine
def go():
    engine = yield from create_engine(minsize=1,
                                      maxsize=30,
                                      user='rjain',
                                      db='learning',
                                      host='localhost',
                                      password='pass@123',
                                      loop=loop)

    with (yield from engine) as conn:
        trans = yield from conn.begin()
        try:
            yield from conn.execute(users.insert().values(name='abc',age=33))
            res = yield from conn.execute(users.select())

        except Exception:
            yield from trans.rollback()
        else:
            yield from trans.commit()

        if res:
             for row in res:
                print(row.id, row.name, row.age)
        print(engine.freesize)
#asyncio.get_event_loop().run_until_complete(go())
loop.run_until_complete(go())
