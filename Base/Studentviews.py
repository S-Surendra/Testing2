from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})