from django import forms
from .models import Book, Student, Student2, Flower

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']


class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']
        widgets = {
            'addresses': forms.CheckboxSelectMultiple()
        }

class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ['name', 'genus', 'image']

