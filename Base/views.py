from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student, Teacher, Staff, Marks, Attendance, Fees, Item, AddSchools
from .form import StudentForm, TeacherForm, StaffForm, ItemForm,AddSchoolsForm
from .serializers import StudentSerializer, TeacherSerializer, StaffSerializer

# ---------------------------- Home & Dashboards ----------------------------

def home(request):
    context = {
        'student_count': Student.objects.count(),
        'teacher_count': Teacher.objects.count(),
        'staff_count': Staff.objects.count(),
    }
    return render(request, 'home.html', context)

def schools(request):
     
    return render(request,'schools.html')



def schools_list(request):
    schools = AddSchools.objects.all()
    return render(request, 'schools_list.html', {'schools': schools})

def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')

def staff_dashboard(request):
    return render(request, 'staff_dashboard.html')

# ---------------------------- Students ----------------------------

def add_student(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'add_student.html', {'form': form})

def add_schools(request):
    form = AddSchoolsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('schools_list')
    return render(request, 'add_schools.html', {'form': form})

def student_info(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_info.html', {'student': student})

@login_required
def marks(request, pk):
    student = get_object_or_404(Student, pk=pk)
    marks = Marks.objects.filter(student=student)
    return render(request, 'marks.html', {'student': student, 'marks': marks})

def attendance(request, pk):
    student = get_object_or_404(Student, pk=pk)
    attendance = Attendance.objects.filter(student=student)
    return render(request, 'attendance.html', {'student': student, 'attendance': attendance})

def fees(request, pk):
    student = get_object_or_404(Student, pk=pk)
    fee = Fees.objects.filter(student=student)
    return render(request, 'fees.html', {'student': student, 'fee': fee})

# ---------------------------- Teachers ----------------------------

def add_teacher(request):
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('teacher_list')
    return render(request, 'add_teacher.html', {'form': form})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

# ---------------------------- Staff ----------------------------

def add_staff(request):
    form = StaffForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('staff_list')
    return render(request, 'add_staff.html', {'form': form})

def staff_list(request):
    staffs = Staff.objects.all()
    return render(request, 'staff_list.html', {'staffs': staffs})

# ---------------------------- Items ----------------------------

@login_required
def add_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('item_list')
    return render(request, 'add_item.html', {'form': form})

@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('item_list')
    return render(request, 'edit_item.html', {'form': form})


def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('item_list')
    return render(request, 'delete_item.html', {'item': item})

# ---------------------------- API Views ----------------------------

@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_teachers(request):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_staff(request):
    staff_members = Staff.objects.all()
    serializer = StaffSerializer(staff_members, many=True)
    return Response(serializer.data)
