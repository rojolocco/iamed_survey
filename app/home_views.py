
# Cargando librerias ##################################################
from app import app

import requests
import pyrebase
import uuid
from datetime import date

from flask import render_template, request, session
from app.utils import questions, answers, correct
######################################################################


# Configurando Firebase ##############################################
config = {
    "apiKey" : "AIzaSyB_XEX-0Xfbvb6g3A7QhvjvkxwDMGxDtQQ",
    "authDomain" : "survey-3f464.firebaseapp.com",
    "databaseURL" : "https://survey-3f464.firebaseio.com",
    "projectId" : "survey-3f464",
    "storageBucket" : "survey-3f464.appspot.com",
    "messagingSenderId" : "711424620768",
    "appId" : "1:711424620768:web:248cb1f27a62da4ef57885",
    "measurementId" : "G-LH7W7T1WL0"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
today = date.today()
######################################################################


# Pagina Principal - Home ############################################
@app.route('/', methods=['GET', 'POST'])
def index():
    inicio = True
    if request.method == 'POST':
        sexo = request.form['sexo']
        industria = request.form['industria']
        estudios = request.form['estudios']
        print((sexo,industria,estudios))
        k = str(uuid.uuid4())
        session["SURVEY"] = k
        session["QUESTION"] = 1
        email = 'info@datapulse-opt.com'
        password = 'datapulse'
        response = auth.sign_in_with_email_and_password(email, password)
        id_user = response['localId']
        data = {"survey_code" : k,
                "ans_1": "None",
                "ans_2": "None",
                "ans_3": "None",
                "ans_4": "None",
                "ans_5": "None",
                "ans_6": "None",
                "ans_7": "None",
                "ans_8": "None",
                "sexo": sexo,
                "industria": industria,
                "estudios": estudios
                }
        db.child("results").child(today).child(k).set(data)
        return render_template('/home/index_home.html')
    return render_template('/home/index_home.html', inicio=inicio)
######################################################################


# Pagina Encuesta - Home ############################################
@app.route('/survey', methods=['GET', 'POST'])
def survey():
    n_question = session["QUESTION"]
    que = questions[f'ans_{n_question}']
    ans = answers[f'ans_{n_question}']
    print(f'Pregunta {n_question} : {que}\nRespustas:{ans}')
    
    if request.method == 'POST':
        #answered = session["QUESTION"]
        k = session["SURVEY"]
        answer = request.form['customRadio']
        data = {f"ans_{n_question}" : answer}
        db.child("results").child(today).child(k).update(data)
        
        if n_question < 8:
            session["QUESTION"] += 1
            n_question = session["QUESTION"]
            que = questions[f'ans_{n_question}']
            ans = answers[f'ans_{n_question}']
            return render_template('/home/survey_home.html', n_question=n_question, que=que, ans=ans)
    return render_template('/home/survey_home.html', n_question=n_question, que=que, ans=ans)
######################################################################


# Pagina de Encuesta - Final ##########################################
@app.route('/final_home', methods=['GET', 'POST'])
def final_home():
    k = session["SURVEY"]
    if request.method == 'POST':
        n_question = session["QUESTION"]
        answer = request.form['customRadio']
        data = {f"ans_{n_question}" : answer}
        db.child("results").child(today).child(k).update(data)
        
    respuestas = db.child("results").child(today).get().val()[k]
    respuestas.pop('survey_code', None)
    respuestas.pop('sexo', None)
    respuestas.pop('industria', None)
    print(respuestas.pop('estudios', None))
    return render_template('/home/final_home.html', respuestas=respuestas, 
    questions=questions, answers=answers, correct=correct)

######################################################################

# Pagina de Acceso - LogIn01##########################################
@app.route('/login_home', methods=['GET', 'POST'])
def login_home():
    unsuccessful = True
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            response = auth.sign_in_with_email_and_password(email, password)
            if response['registered']:
                session["USERNAME"] = email
                return render_template('/dashboard/index_dashboard.html')
        except requests.exceptions.HTTPError:
            return render_template('/home/login_home.html', un=unsuccessful)
    return render_template('/home/login_home.html')
######################################################################
