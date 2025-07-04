# Generated by Django 5.2.1 on 2025-05-28 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('enrollment_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('course', models.CharField(max_length=50)),
                ('adhaar_number', models.CharField(max_length=12)),
                ('child_id', models.CharField(default='0', max_length=9)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('mobile_number', models.CharField(max_length=10)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('classes', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ExamMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('exam_type', models.CharField(choices=[('monthly', 'Monthly Test'), ('quarterly', 'Quarterly Exam'), ('half_yearly', 'Half Yearly Exam'), ('annual', 'Annual Exam')], max_length=20)),
                ('theory_marks', models.IntegerField()),
                ('practical_marks', models.IntegerField()),
                ('total_marks', models.IntegerField(blank=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.student')),
            ],
        ),
        migrations.DeleteModel(
            name='Marksheet',
        ),
    ]
