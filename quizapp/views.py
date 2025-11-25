from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import QuizQuestion

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        if not username:
            return render(request, 'index.html', {'error': 'Username cannot be empty'})
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'index.html', {'error': 'Username already exists'})
        else:
            my_user = User.objects.create_user(username)
            my_user.save()
            return render(request,'nextpage.html', {'user': username})
    return render(request, 'index.html')
def nextpage(request):
    return render(request, 'nextpage.html')

def quizplay(request):
    # If session question index does not exist, start with the first question
    if 'q_index' not in request.session or request.session['q_index'] >= QuizQuestion.objects.count():
        request.session['q_index'] = 0

    q_index = request.session['q_index']
    questions = QuizQuestion.objects.all()

    # If all questions finished
    if q_index >= len(questions):
        return render(request, 'quizplay.html', {"error" : "End Game"})

    current_question = questions[q_index]
    error1 = ""

    if request.method == "POST":
        selected = request.POST.get("answer")
        if selected == current_question.correct_answer:
            # correct → next question
            request.session['q_index'] += 1
            return redirect('quizplay')
        else:
            # wrong → stay on same question
            error1 = "❌ Incorrect! Try again."
    return render(request, 'quizplay.html', {
        "q": current_question,
        "errormsg": error1
    })