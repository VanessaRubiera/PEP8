# PEP8 Guia de estilos para Python
# Clases con denotacion CamelCase
# https://www.pythonchecker.com/
# Terminar script con salto de linea

class UserAdmin():

    # Identacion: 4 espacios (no tabs)
    # Parametros: separados por , y 1 espacio
    # Dos lineas despues de la definicion de una funcion


    def __init__(self, username, password = ''):
        self.username = username #self es como el this en JS
        self.password = password


        def set_password(self):
            pass

# Variables con denotacion snake_case 
# Espacios entre operadores


cody_user = UserAdmin('Cody')
