
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

    @property
    def get_nombre(self):
        return self._nombre
    @property
    def set_nombre(self, nuevo):
        self._nombre = nuevo

    @property
    def get_apellido(self):
        return self._apellido

    @property
    def set_apellido(self, nuevo):
        self._apellido = nuevo

    @property
    def get_dni(self):
        return self._dni

    @property
    def get_mail(self):
        return self._mail

    @property
    def set_mail(self, nuevo):
        self._mail = nuevo

    @property
    def get_telefono(self):
        return self._telefono
    
    @property
    def set_telefono(self, nuevo):
        self._telefono = nuevo

    @property
    def get_depto(self):
        return self._depto

    @property
    def set_depto(self, nuevo):
        self._depto = nuevo

    @property
    def get_localidad(self):
        return self._localidad

    @property
    def set_localidad(self, nuevo):
        self._localidad = nuevo

    @property
    def get_calle(self):
        return self._calle

    @property
    def set_calle(self, nuevo):
        self._calle = nuevo

    @property
    def get_num_puerta(self):
        return self._num_puerta

    @property
    def set_num_puerta(self, nuevo):
        self._num_puerta = nuevo

    @property
    def get_apto(self):
        return self._apto

    @property
    def set_apto(self, nuevo):
        self._apto = nuevo

    @property
    def get_cod_postal(self):
        return self._cod_postal

    @property
    def set_cod_postal(self, nuevo):
        self._cod_postal = nuevo

    





    
    
        