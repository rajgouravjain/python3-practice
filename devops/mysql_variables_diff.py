import sqlalchemy
import pymysql

engine = sqlalchemy.create_engine(
"mysql+pymysql://rj4595@10.0.1.253/mysql",
                isolation_level="READ UNCOMMITTED"
            )

connection = engine.connect()
result = connection.execute("show global variables")

s_set= set()

#print(result)
for r in result:
    s_set.add(tuple(r))
#print(s_set)
result.close()


engine = sqlalchemy.create_engine(
"mysql+pymysql://rj4595@10.0.1.85/mysql",
                isolation_level="READ UNCOMMITTED"
            )

connection = engine.connect()
result = connection.execute("show global variables")

d_set= set()
for r in result:
    d_set.add(tuple(r))
#print(d_set)
result.close()


diff=s_set - d_set
print("=========central-db variables===========")
for i in diff:
    print(i)

rdiff=d_set-s_set
print
print("=========mysql-dump-db  variables===========")
for i in rdiff:
    print(i)
