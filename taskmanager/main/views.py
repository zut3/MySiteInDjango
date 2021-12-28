from django.shortcuts import render , redirect , HttpResponse
from .models import Quiz
from .forms import QuizForm
# Create your views here.


def show(request):
    quiz = Quiz.objects.order_by('id')
    return render(request , "main/index.html" ,{'quiz' : quiz})

def show_secret(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    form = QuizForm()
    return render(request ,"main/CreateFB.html", {
        "form" : form,
    })