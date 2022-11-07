from peewee import * 

db_pg = PostgresqlDatabase('dbd2', host='localhost', port=8888, user='dbd2g1', password = 'dbd2#G1')

class BaseModel (Model):
    
    class Meta: 
        database= db_pg