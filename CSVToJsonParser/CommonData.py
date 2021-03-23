import os, csv, pandas as pd
from datetime import date
from django.shortcuts import render, Http404
from django.http import HttpResponse


class CommonData:

    def __init__(self, csvfile_path):
        self.data = self.csv_df(csvfile_path)

    def csv_df(self, csvfile_path):
        # Converting csv to DataFrame to dictionary
        if not os.path.exists(csvfile_path):
            raise Http404("Csv_file_path does not existed!!")

        df = pd.read_csv(csvfile_path)
        df_columns = df.columns.values

        if self.required_columns_exist(df_columns):
            return df.to_dict("records")
        else:
            raise Http404("Csv headers are not mathed!!")

    def required_columns_exist(self, fieldnames):
        csv_headers = ['id', 'category', 'firstname', 'lastname', 'gender', 'dob', 'previous_school',
                       'doj', 'class', 'post', 'salary', 'class_teacher_of', 'roll_no', 'emp_no',
                       'total_marks', 'city', 'aadhar_number', 'contact_number', 'blood_group',
                       'subject_teaches', 'hs_stream', 'sec_percent']
        if set(fieldnames) != set(csv_headers):
            return False;
        return True;

    def calc_year_month(self, dob):
        # Calculating no.of months and years from given date
        today = date.today()
        try:
            dob_list = dob.split('/')
        except Exception:
            dob_list = dob.strftime("%m/%d/%Y").split('/')

        year = today.year - int(dob_list[2])
        month = today.month - int(dob_list[0])
        if month < 0:
            month = -month

        Years = ' Yrs'
        Months = ' Months'

        if year == 1:
            Years = ' Yr'
        if month == 1:
            Months = ' Month'
        return str(year) + Years + " " + str(month) + Months

    def convert_to_date(self, date):
        # Converting date to Day and month with leading Zeros
        # if self.validate_date(date) == False:
        #     raise Http404("date format is not correct")
        date_list = date.split('/')
        if int(date_list[0]) < 10:
            date_list[0] = '0' + date_list[0]
        if int(date_list[1]) < 10:
            date_list[1] = '0' + date_list[1]
        return '/'.join(date_list)

    def common_data(self, data):
        personnel_data = {
            "id": int(data["id"]),
            "fullName": data["firstname"].title() + " " + data["lastname"].title(),
            "gender": "Male" if data["gender"].lower() == "m" else "Female",
            "dob": self.convert_to_date(data["dob"]),
            "age": self.calc_year_month(data["dob"]),
            "aadhar": data["aadhar_number"],
            "city": data["city"].title(),
            "contactNumber": str(data["contact_number"])
        }
        return personnel_data


    def validate_date(self, date_data):

        if date_data is not None and len(date_data) > 0:
            if not self.check_date_format(date_data):
                return False

    def check_date_format(self, date_str):
        try:
            datetime.strptime(date_str, '%m/%d/%Y')
            return True
        except:
            return False