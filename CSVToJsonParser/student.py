from CSVToJsonParser.CommonData import *

class Student(CommonData):

    def grade(self, total_marks):
        # grade Calculation
        if total_marks >= 800:
            grade = "A"
        elif total_marks >= 700:
            grade = "B"
        elif total_marks >= 600:
            grade = "C"
        elif total_marks >= 500:
            grade = "D"
        return grade

    def rendering_student_to_json(self, Age, Name):
        records = []
        student_record = []
        for sub_data in self.data:
            if sub_data["category"] == "student":
                result_data = CommonData.common_data(self, sub_data)
                result_data.update({
                    "rollNo": int(sub_data["roll_no"]),
                    "className": sub_data["class"],
                    "totalMarks": int(sub_data["total_marks"]),
                    "grade": self.grade(sub_data["total_marks"]),
                    "secPercent": int(sub_data["sec_percent"]),
                    "hsStream": sub_data["hs_stream"].title()
                })
                # Appending student records to list
                records.append(result_data)
        for row in records:
            if (int(row["age"].split(" ")[0]) >= int(Age)) or (Name in row["fullName"]):
                student_record.append(row)
        return {"RecordCount": len(student_record), 'data': student_record}