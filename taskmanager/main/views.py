from django.shortcuts import render , redirect
from .models import Quiz
from .forms import QuizForm


def show_main(request):
    quiz = Quiz.objects.order_by('id')
    return render(request , "main/index.html" ,{'quiz' : quiz})

def show_create(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    form = QuizForm()
    return render(request ,"main/CreateFB.html", {
        "form" : form,
    })