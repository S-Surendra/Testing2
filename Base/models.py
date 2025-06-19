from django.db import models

class Schools(models.Model):
    name = models.CharField(max_length=120)
    school_id = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.name} ({self.school_id})"
    
class AddSchools(models.Model):
    schoolName=models.CharField(max_length=100)
    schoolDiceCode=models.CharField(max_length=12)
    schoodId= models.CharField(max_length=10)
    def __str__(self):
        return f"{self.schoolName} ({self.schoolDiceCode})" 
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    enrollment_number = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    course = models.CharField(max_length=50)
    adhaar_number = models.CharField(max_length=12)
    child_id = models.CharField(max_length=9, default='0')
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    mobile_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100, blank=True)
    classes = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name} ({self.enrollment_number})"

class Item(models.Model):
    name = models.CharField(max_length=100)
    enrollment_number = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    course = models.CharField(max_length=50)
    adhaar_number = models.CharField(max_length=12)
    child_id = models.CharField(max_length=9, default='0')
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    mobile_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100, blank=True)
    classes = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name} ({self.enrollment_number})"
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, related_name='attendances', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[('Present', 'Present'), ('Absent', 'Absent')],
        default='Absent'
    )

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"


class Marks(models.Model):
    SUBJECT_CHOICES = [
        ('Hindi', 'Hindi'),
        ('English', 'English'),
        ('Mathematics', 'Mathematics'),
        ('Science', 'Science'),
        ('Social Science', 'Social Science'),
    ]
    student = models.ForeignKey(Student, related_name='marks', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    marks_obtained = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject} - {self.marks_obtained}/{self.total_marks}"


class Teacher(models.Model):
    user = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    adhaar_number = models.CharField(max_length=12)
    pay_scale = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user} ({self.subject})"


class Staff(models.Model):
    staff_id = models.CharField(max_length=5, default='')
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=30,default='staff')

    def __str__(self):
        return f"{self.name} ({self.staff_id})"


class Library(models.Model):
    book_id = models.CharField(max_length=5,default='')
    book_name = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    author = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.book_name} ({self.category})"


class Fees(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    month_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student.name} ({self.month_name})"


# Marksheet model



class ExamMarks(models.Model):
    EXAM_TYPES = [
        ('monthly', 'Monthly Test'),
        ('quarterly', 'Quarterly Exam'),
        ('half_yearly', 'Half Yearly Exam'),
        ('annual', 'Annual Exam'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPES)
    theory_marks = models.IntegerField()
    practical_marks = models.IntegerField()
    total_marks = models.IntegerField(blank=True)

    def save(self, *args, **kwargs):
        self.total_marks = self.theory_marks + self.practical_marks
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - {self.subject} ({self.exam_type})"