# Configuracion del modulo log, con esto conseguimos que la impresion de cada registro sea justo como queremos

import logging as log

log.basicConfig(level=log.INFO,  # Nivel en el que queremos que sea un debug
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',  # Formato de la impresion de los registros
                datefmt='%I:%M:%S %p', # Formato de la fecha
                handlers=[
                    log.FileHandler('capa_datos.log'), # Archivo creado para guardar los registros
                    log.StreamHandler() # Método para que sea impreso en la consola
                ])
