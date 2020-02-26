# Cargando librerias ##################################################
from app import app

#import numpy as np
#import pandas as pd
import base64
import sys
import os
from werkzeug.utils import secure_filename
#######################################################################

questions = {'ans_1': '¿Usted sabe que es inteligencia artificial?',
                'ans_2':'¿Cual es una rama de la Inteligencia Artificial?',
                'ans_3':'¿Cual es una rama de la Inteligencia Artificial?',
                'ans_4':'¿Cual es una rama de la Inteligencia Artificial?',
                'ans_5':'¿Cual es una rama de la Inteligencia Artificial?'
}

answers = {
    'ans_1':{'option1':'si', 'option2':'no'},
    'ans_2':{'option1':'si', 'option2':'no'},
    'ans_3':{'option1':'si', 'option2':'no'},
    'ans_4':{'option1':'si', 'option2':'no'},
    'ans_5':{'option1':'si', 'option2':'no'}
}

correct = {
    'ans_1': 'option1', 'ans_2':'option1', 'ans_3':'option1', 'ans_4':'option1', 'ans_5':'option1'
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
