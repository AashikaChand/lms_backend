from rest_framework import serializers
from app.models import Book, Course, Department, Semester, Student, studentBook

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', )
        depth = 10
        
class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ('id', 'name', 'symbol', )
        depth = 10
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name',  'department', 'semester',)
        depth =10
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'code', 'course', 'edition', 'semester',)
        depth = 10
        
class StudentBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentBook
        fields = ('id', 'student','book','issue_date','return_date')
        depth = 10
        
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        field = ('id','name','symbol', 'department','image','course','semester','student_book')
        
        
        