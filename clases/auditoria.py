import socket
from datetime import datetime
from flask import session
import pytz

class Auditoria:
    def __init__(self, usuario):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        self.Maquina_graba = s.getsockname()[0]
        # Obtener la fecha y hora en la zona horaria de Colombia
        colombia_tz = pytz.timezone('America/Bogota')
        Fecha = datetime.now(colombia_tz)

        self.Fecha_graba = Fecha.strftime('%Y-%m-%d %H:%M:%S')
        self.Usuario_graba = usuario

class OtraClase:
    def __init__(self, auditoria):
        self.auditoria = auditoria

    def mostrar_fecha(self):
        # Acceder al atributo Fecha_graba de la instancia de Auditoria
        return self.auditoria.Fecha_graba