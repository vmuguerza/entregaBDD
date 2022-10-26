
class Cliente:
    def __init__(self, nombre, apellido,dni, mail, depto, localidad, calle, num_puerta, apto, cod_postal, telefono):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._mail= mail
        self._telefono=telefono
        self._departamento = depto 
        self._localidad = localidad 
        self._calle = calle 
        self._num_puerta = num_puerta
        self._apto = apto
        self._cod_postal = cod_postal

    
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

    





    
    
        