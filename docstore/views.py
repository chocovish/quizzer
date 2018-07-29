from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import addForm
from .utility import choice_maker

from .models import questions
# Create your views here.

def home(request):
    return render(request,'docstore/master.html')


def play(request):
    if request.method=='POST':
        if request.POST['choice']==questions.objects.get(pk=request.POST['qpk']).answer:
            request.session['score'] = request.session['score'] + 1

        q = questions.objects.filter(pk__lt=request.POST['qpk']).last()
        if q == None:
            return HttpResponseRedirect(reverse('completed'))
        request.session['played'] = q.pk

        choice = q.choice.split(",")
        return render(request, 'docstore/index.html',{'q':q, 'choice':choice, 'score':request.session['score']})


# ... First request starts frome here.....
    if not request.session.get("played", False):
        request.session.set_expiry(604800)
        request.session['played'] = questions.objects.last().pk
    if questions.objects.get(pk=request.session['played']) == questions.objects.first():
        request.session['played'] = questions.objects.last().pk
    q = questions.objects.get(pk=request.session['played'])
    choice = q.choice.split(",")
    request.session['score'] = 0
    
    return render(request, 'docstore/index.html', {'q':q, 'choice':choice})


def completed(request):
    return render(request,'docstore/index.html', {'completed':True, 'score':request.session['score']})


def add(request):
    if request.method=='POST':
        form = addForm(request.POST)
        if form.is_valid():
            print("*********", form.cleaned_data)
            cleaned_choice = choice_maker(form.cleaned_data['choice'])
            questions(question=form.cleaned_data['question'].capitalize(), choice=cleaned_choice,answer=form.cleaned_data['answer'].capitalize()).save()
    return render(request, 'docstore/form.html')