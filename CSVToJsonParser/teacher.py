from CSVToJsonParser.CommonData import *

class Teacher(CommonData):
    def rendering_teacher_to_json(self, Age, Name):
        records = []
        teacher_record = []
        for sub_data in self.data:
            if sub_data["category"] == "teacher":
                result_data = CommonData.common_data(self, sub_data)
                result_data.update({
                    "empNo": sub_data["emp_no"],
                    "classTeacher": sub_data["class_teacher_of"],
                    "doj": CommonData.convert_to_date(self, sub_data["doj"]),
                    "servicePeriod": CommonData.calc_year_month(self, sub_data["doj"]),
                    "previousSchool": sub_data['previous_school'],
                    "post": sub_data["post"],
                    "salary": ("{:,.0f}".format(sub_data["salary"]))
                })
                # Appending teacher records to list
                records.append(result_data)
        for row in records:
            if (int(row["age"].split(" ")[0]) >= int(Age)) or (Name in row["fullName"]):
                teacher_record.append(row)
        return {"RecordCount": len(teacher_record), 'data': teacher_record}