from django.http.response import Http404
from django.shortcuts import get_object_or_404, render, HttpResponse,HttpResponseRedirect
from polls.models import *
from django.urls import reverse

# Create your views here.
def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    context={
        'latest_question_list':latest_question_list
    }
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('La pregunta no existe')

    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    return HttpResponse('Estas viendo los resultados de la pregunta %s.'%question_id)

def vote(request,question_id):
    
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])

    except (KeyError,Choice.DoesNotExist):
        #se vuelve a mostrar la pagina para votar
        return render(request,'polls/detail.html',{
            'question': question,
            'error_message':'Todavia no has votado por nadie', 
        })
    
    else:
        selected_choice.votes+=1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:resultados', args=(question.id,)))
