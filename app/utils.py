# Cargando librerias ##################################################
from app import app

#import numpy as np
#import pandas as pd
import base64
import sys
import os
from datetime import date
import pandas as pd
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

# Calculo deResultados #############################################
def calculo_resultados(resultados):
    #print(resultados)
    fecha = date.today()
    n_pruebas = len(resultados.keys())

    ans_1_list = []
    ans_2_list = []
    ans_3_list = []
    ans_4_list = []
    ans_5_list = []
    ans_6_list = []
    ans_7_list = []
    ans_8_list = []
    sexo_list = []
    industria_list = []
    estudios_list = []

    for k_outer,v_outer in resultados.items():
        for k_inner,v_inner in v_outer.items():
            if k_inner == 'ans_1':
                ans_1_list.append(v_inner)
            if k_inner == 'ans_2':
                ans_2_list.append(v_inner)
            if k_inner == 'ans_3':
                ans_3_list.append(v_inner)
            if k_inner == 'ans_4':
                ans_4_list.append(v_inner)
            if k_inner == 'ans_5':
                ans_5_list.append(v_inner)
            if k_inner == 'ans_6':
                ans_6_list.append(v_inner)
            if k_inner == 'ans_7':
                ans_7_list.append(v_inner)
            if k_inner == 'ans_8':
                ans_8_list.append(v_inner)
            if k_inner == 'sexo':
                sexo_list.append(v_inner)
            if k_inner == 'industria':
                industria_list.append(v_inner)
            if k_inner == 'estudios':
                estudios_list.append(v_inner)

    dict_df = {'ans_1': ans_1_list,
                'ans_2': ans_2_list,
                'ans_3': ans_3_list,
                'ans_4': ans_4_list,
                'ans_5': ans_5_list,
                'ans_6': ans_6_list,
                'ans_7': ans_7_list,
                'ans_8': ans_8_list,
                'sexo':sexo_list,
                'industria':industria_list,
                'estudios':estudios_list
    }

    df = pd.DataFrame.from_dict(dict_df)
    print(df)

    sexo_values = df['sexo'].value_counts(dropna=False).keys().tolist()
    sexo_counts = df['sexo'].value_counts(dropna=False).tolist()
    sexo_dict = dict(zip(sexo_values, sexo_counts))
    #print(sexo_dict)

    industria_values = df['industria'].value_counts(dropna=False).keys().tolist()
    industria_counts = df['industria'].value_counts(dropna=False).tolist()
    industria_dict = dict(zip(industria_values, industria_counts))
    #print(industria_dict)

    estudios_values = df['estudios'].value_counts(dropna=False).keys().tolist()
    estudios_counts = df['estudios'].value_counts(dropna=False).tolist()
    estudios_dict = dict(zip(estudios_values, estudios_counts))
    #print(estudios_dict)

    ans_1_values = df['ans_1'].value_counts(dropna=False).keys().tolist()
    ans_1_counts = df['ans_1'].value_counts(dropna=False).tolist()
    ans_1_dict = dict(zip(ans_1_values, ans_1_counts))
    #print(ans_1_dict)

    ans_2_values = df['ans_2'].value_counts(dropna=False).keys().tolist()
    ans_2_counts = df['ans_2'].value_counts(dropna=False).tolist()
    ans_2_dict = dict(zip(ans_2_values, ans_2_counts))
    #print(ans_1_dict)

    ans_3_values = df['ans_3'].value_counts(dropna=False).keys().tolist()
    ans_3_counts = df['ans_3'].value_counts(dropna=False).tolist()
    ans_3_dict = dict(zip(ans_3_values, ans_3_counts))
    #print(ans_3_dict)

    ans_4_values = df['ans_4'].value_counts(dropna=False).keys().tolist()
    ans_4_counts = df['ans_4'].value_counts(dropna=False).tolist()
    ans_4_dict = dict(zip(ans_4_values, ans_4_counts))
    #print(ans_4_dict)

    ans_5_values = df['ans_5'].value_counts(dropna=False).keys().tolist()
    ans_5_counts = df['ans_5'].value_counts(dropna=False).tolist()
    ans_5_dict = dict(zip(ans_5_values, ans_5_counts))
    #print(ans_5_dict)

    ans_6_values = df['ans_6'].value_counts(dropna=False).keys().tolist()
    ans_6_counts = df['ans_6'].value_counts(dropna=False).tolist()
    ans_6_dict = dict(zip(ans_6_values, ans_6_counts))
    #print(ans_6_dict)

    ans_7_values = df['ans_7'].value_counts(dropna=False).keys().tolist()
    ans_7_counts = df['ans_7'].value_counts(dropna=False).tolist()
    ans_7_dict = dict(zip(ans_7_values, ans_7_counts))
    #print(ans_7_dict)

    ans_8_values = df['ans_8'].value_counts(dropna=False).keys().tolist()
    ans_8_counts = df['ans_8'].value_counts(dropna=False).tolist()
    ans_8_dict = dict(zip(ans_8_values, ans_8_counts))
    #print(ans_8_dict)

    correct_dict = {f'ans_{i}':(df[f'ans_{i}'] == correct[f'ans_{i}']).sum() for i in range(1,9)}
    #print(correct_dict)

    value_correct = 0
    perc_correct = sum(correct_dict.values())*100/(n_pruebas*8)
    #print(perc_correct)

    result_dict = {
        'fecha':fecha,
        'n_pruebas':n_pruebas,
        'perc_correct':perc_correct,
        'sexo':sexo_dict,
        'estudios':estudios_dict,
        'ans_1':ans_1_dict,
        'ans_2':ans_2_dict,
        'ans_3':ans_3_dict,
        'ans_4':ans_4_dict,
        'ans_5':ans_5_dict,
        'ans_6':ans_6_dict,
        'ans_7':ans_7_dict,
        'ans_8':ans_8_dict
    }

    return result_dict
#######################################################################
