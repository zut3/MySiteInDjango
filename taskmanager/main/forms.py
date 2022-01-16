from .models import Quiz
from django.forms import ModelForm , TextInput , Textarea

class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ["name" , "feedback"]
        widjets = {"name" : TextInput(attrs={
            'placeholder': 'Напишите отзыв',
            'class' : "form-control",

        }),
            "feedback": Textarea(attrs={
                'placeholder': 'Напишите отзыв',
                'class': "form-control",
            })
        }



