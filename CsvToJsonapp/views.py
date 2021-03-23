from django.shortcuts import render
from .forms import UserInput
from django.contrib import messages

import pandas as pd
from datetime import date
import json, os
import sys
from CSVToJsonParser.student import *
from CSVToJsonParser.CommonData import *
from CSVToJsonParser.teacher import *

csv_file_path = "D:\\ADMIN\\Desktop\\CSV2JSON-Inheritence\\csv\\input.csv"
# csv_file_path = "D:\\ADMIN\\Desktop\\CSV2JSON-Inheritence\\csv\\input_wrong_headers.csv"
# csv_file_path = "D:\\ADMIN\\Desktop\\CSV2JSON-Inheritence\\csv\\input_wrong_date_value.csv"

def HomePage(request):
    form = UserInput()
    return render(request, 'data-search.html', {"form":form})

def SearchPage(request):
    category = request.GET.get("category")
    age = request.GET.get("age")
    name = request.GET.get("name")
    result_data = search_data(category, age, name)
    result_data.update({'category':category})
    return render(request, 'result.html', result_data)

def search_data(category, age, name):
    if category == "student":
        student = Student(csv_file_path)
        return student.rendering_student_to_json(age, name)
    if category == "teacher":
        teacher = Teacher(csv_file_path)
        return teacher.rendering_teacher_to_json(age, name)
