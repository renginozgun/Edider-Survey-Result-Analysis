from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
import mysql.connector


User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customers": 10})

def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        mydb = mysql.connector.connect(
        host="",
        user="",
        password="",
        database="",
        )
        answers=[]
        mycursor = mydb.cursor()
        mycursor.execute("SELECT COUNT(S1) FROM Q1 WHERE S1='Lisansli Üretim'")
        myresult = mycursor.fetchone()
        answers.append(myresult[0])
        mycursor.execute("SELECT COUNT(S2) FROM Q1 WHERE S2='Iletim Hizmetleri'")
        myresult = mycursor.fetchone()
        answers.append(myresult[0])
        mycursor.execute("SELECT COUNT(S3) FROM Q1 WHERE S3='Dağitim Hizmetleri'")
        myresult = mycursor.fetchone()
        answers.append(myresult[0])
        mycursor.execute("SELECT COUNT(S4) FROM Q1 WHERE S4='Tedarik'")
        myresult = mycursor.fetchone()
        answers.append(myresult[0])
        mycursor.execute("SELECT COUNT(S5) FROM Q1 WHERE S5='Dağitik Enerji Kaynaklari'")
        myresult = mycursor.fetchone()
        answers.append(myresult[0])
        mycursor.execute("SELECT COUNT(S6) FROM Q1 WHERE S6='Tüketici'")
        myresult = mycursor.fetchone()
        answers.append(myresult[0])



        labels=["Lisanslı Üretim,","İletim Hizmetleri","Dağıtım Hizmetleri,","Tedarik Hizmetleri","Dağıtık Enerji Kaynakları","Tüketici Hizmetleri"]
        
        data = {
                "labels": labels,
                "default": answers,
        }
        return Response(data)

