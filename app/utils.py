# Cargando librerias ##################################################
from app import app

#import numpy as np
#import pandas as pd
import base64
import sys
import os
from werkzeug.utils import secure_filename
#######################################################################

questions = {'ans_1': '¿Qué es inteligencia artificial?',
                'ans_2':'¿Cuáles son ramas de la inteligencia artificial?',
                'ans_3':'¿En que tipo de industrias se puede crear aplicaciones de Inteligencia artificial?',
                'ans_4':'¿Los asistentes virtuales de voz como Siri, Alexa o Cortana Utilizan técnicas de IA?',
                'ans_5':'¿Cuál es la única aplicación de inteligencia artificial en medicina?',
                'ans_6':'¿Dónde se ha utilizado el Machine Learning en medicina?',
                'ans_7':'¿Cuál de las siguientes opciones NO utiliza IA en medicina?',
                'ans_8':'¿Hace cuantos años se celebró la primera conferencia de IA en medicina?'
}


answers = {
    'ans_1':{'option1':'Es el subcampo de las ciencias de la computación, cuyo objetivo es desarrollar técnicas que permitan que las computadoras aprendan', 
                'option2':'Es la combinación de algoritmos planteados con el propósito de crear máquinas que presenten las mismas capacidades que el ser humano',
                'option3':'Es la rama de la ingeniería que se ocupa del diseño, construcción, operación, estructura, manufactura, y aplicación de los robots',
                'option4':'Ninguna de las anteriores'
            },
    'ans_2':{'option1':'Computer Vision (CV)', 
                'option2':'Procesamiento de Lenguaje Natural (NLP)',
                'option3':'Machine Learning (ML)',
                'option4':'Todas las anteriores'
            },
    'ans_3':{'option1':'Solo en industrias relacionadas con ingeniería', 
                'option2':'Solo en industrias relacionadas con robótica',
                'option3':'En todo tipo de industrias',
                'option4':'Solo en industrias de tecnología e innovación'
            },
    'ans_4':{'option1':'No, son programas que usan otro tipo de tecnología', 
                'option2':'Si, usan Procesamiento de Lenguaje Natural (NLP)',
                'option3':'No, solo son programados con preguntas y respuestas determinadas',
                'option4':'Si, son robots programados para hacer conversaciones'
            },
    'ans_5':{'option1':'Las cirugías asistidas por robots', 
                'option2':'No hay aplicaciones de IA en medicina',
                'option3':'Hay muchas aplicaciones de IA, no solo una',
                'option4':'Telemedicina'
            },
    'ans_6':{'option1':'Esta tecnología no se usa en medicina', 
                'option2':'Predicción de Hospitalización de pacientes de urgencia',
                'option3':'Soporte de diagnóstico en lectura de radiografías',
                'option4':'Son correctas la b y c'
            },
    'ans_7':{'option1':'Análisis de imágenes biomédicas (Xray, CT, MRI, ETC)', 
                'option2':'Predicción de arritmias con ECG',
                'option3':'En la cirugía asistidas por robots',
                'option4':'Agendamiento automático de citas medicas'
            },
    'ans_8':{'option1':'Hace 15 años', 
                'option2':'Hace 25 años',
                'option3':'Hace 35 años',
                'option4':'Hace 45 años'
            }
}



correct = {
    'ans_1': 'option2', 
    'ans_2':'option4', 
    'ans_3':'option3', 
    'ans_4':'option2', 
    'ans_5':'option3',
    'ans_6':'option4',
    'ans_7':'option4',
    'ans_8':'option3'
}

# Codificaciones de Redis #############################################
def base64_encode_image(a):
    return base64.b64encode(a).decode("utf-8")


def base64_decode_image(a, dtype, shape):

    # if this is Python 3, we need the extra step of encoding the
    # serialized NumPy string as a byte object
    if sys.version_info.major == 3:
        a = bytes(a, encoding="utf-8")

    a = np.frombuffer(base64.decodestring(a), dtype=dtype)
    a = a.reshape(shape)

    # return the decoded image
    return a
#######################################################################
