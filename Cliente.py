
from peewee import *
from database import *

class Cliente (BaseModel):
    nombre = CharField(max_length=15, null=False, primary_key=True) #hacer esto en todas
    apellido = CharField()
    dni = IntegerField()
    mail= CharField()
    telefono= IntegerField()
    departamento = CharField() 
    localidad = CharField() 
    calle = CharField() 
    nro_puerta = IntegerField()
    aptartamento = CharField()
    cod_postal = IntegerField()

    class Meta:
        database = db_pg

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo):
        self._nombre = nuevo

    def get_apellido(self):
        return self._apellido

    def set_apellido(self, nuevo):
        self._apellido = nuevo

    def get_dni(self):
        return self._dni

    def get_mail(self):
        return self._mail

    def set_mail(self, nuevo):
        self._mail = nuevo

    def get_telefono(self):
        return self._telefono

    def set_telefono(self, nuevo):
        self._telefono = nuevo

    def get_depto(self):
        return self._depto

    def set_depto(self, nuevo):
        self._depto = nuevo

    def get_localidad(self):
        return self._localidad

    def set_localidad(self, nuevo):
        self._localidad = nuevo

    def get_calle(self):
        return self._calle

    def set_calle(self, nuevo):
        self._calle = nuevo

    def get_num_puerta(self):
        return self._num_puerta

    def set_num_puerta(self, nuevo):
        self._num_puerta = nuevo

    def get_apto(self):
        return self._apto

    def set_apto(self, nuevo):
        self._apto = nuevo

    def get_cod_postal(self):
        return self._cod_postal

    def set_cod_postal(self, nuevo):
        self._cod_postal = nuevo