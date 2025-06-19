from django import forms
from .models import Student, Teacher, Staff, Library, Marks, Attendance, Schools, AddSchools
from .models import ExamMarks

# -------- Student Form --------
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name', 'enrollment_number', 'email', 'date_of_birth', 'course',
            'adhaar_number', 'child_id', 'image', 'mobile_number', 'address',
            'classes'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].input_formats = ['%Y-%m-%d']

class AddSchoolsForm(forms.ModelForm):
    class Meta:
        model = AddSchools
        fields = ['schoolName','schoolDiceCode','schoodId']
    def __init__(self, *args, **kwargs):
        super(AddSchoolsForm, self).__init__(*args, **kwargs)

# -------- Attendance Form --------
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%Y-%m-%d']


# -------- Marks Form --------
class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'subject', 'marks_obtained', 'total_marks']
        widgets = {
            'marks_obtained': forms.NumberInput(attrs={'min': 0}),
            'total_marks': forms.NumberInput(attrs={'min': 0}),
        }


# -------- Teacher Form --------
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'subject', 'mobile_number', 'pay_scale', 'adhaar_number']


# -------- Staff Form --------
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'staff_id', 'designation']  # use 'staff_id' instead of 'id'

    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)


# -------- Library Form --------
class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['book_name', 'book_id', 'category', 'author']  # use 'book_id' instead of 'id'

    def __init__(self, *args, **kwargs):
        super(LibraryForm, self).__init__(*args, **kwargs)


# -------- Student Marksheet Form --------



class ExamMarksForm(forms.ModelForm):
    class Meta:
        model = ExamMarks
        fields = ['student', 'subject', 'exam_type', 'theory_marks', 'practical_marks']

from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
