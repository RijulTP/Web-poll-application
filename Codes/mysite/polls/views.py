from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Choice, Question,Tags
from django.views import generic
from django.urls import reverse
from django.utils import timezone
from rest_framework import viewsets


from . import structureloader as SL

from django.views.decorators.csrf import csrf_exempt

import json

from django.forms.models import model_to_dict

from datetime import datetime

from django.core.serializers.json import DjangoJSONEncoder

from django.core.serializers import serialize

import re
#####import model as ModelClass
#from structureloader import loadquestion,dictionarymaker

#from .serializers import 

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/Detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())



class DetailPageView(generic.ListView):
    template_name = 'polls/Detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class VotePageView(generic.ListView):
    template_name = 'polls/Votepage.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class CreatePageView(generic.ListView):
    template_name = 'polls/CreatePage.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class IndexScriptView():
    template_name="polls/indexscript.js"




class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, YourCustomType):
            return str(obj)
        return super().default(obj)

@csrf_exempt 

def tagfinder(requrl):
    reqtags=requrl[requrl.find("?tags=")+6:]
    reqtaglist=reqtags.split(",")
    return reqtaglist


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
def POST(request):
    structure=json.loads(request.body)
    #structure="1234"
    strquestion=structure["Question"]
    strchoices=structure["OptionVote"]
    strtags=structure["Tags"]
    q=Question(question_text=strquestion,pub_date=timezone.now())
    q.save()
    for i in strchoices:
        c=Choice(question=q,choice_text=i,votes=strchoices.get(i))
        c.save()
    for i in strtags:
        t=Tags(question=q,tag_text=i)
        t.save()
    return render(request, 'polls/index.html')
def GET(request,id=None):
    print("Path is",request.build_absolute_uri(),"++++++++++++++++++++++++++++++++")

    reqpath=request.build_absolute_uri()
    resultlist=[]
    if id:
        print('ID')
        question_id=id
        questionobject=get_object_or_404(Question,pk=question_id)
        #questionobject=x
        question=model_to_dict(questionobject)["question_text"]
        choice=questionobject.choice_set
        #choicedict=SL.dictionarymaker()
        #resultdict=[{"Question":str(question),"OptionVote":{}}]

        optionsdict={}
        for i in questionobject.choice_set.all():
            optionsdict[str(i)]=i.votes
        tagslist=[]
        for i in questionobject.tags_set.all():
            tagslist.append(str(i))
        resultdict={
        "Question":question,
        "OptionVote": optionsdict,
        "Tags": tagslist
        }
        resultlist.append(resultdict)
        FinalResult = json.dumps(resultlist,default=str) 
        return HttpResponse(FinalResult)
    elif reqpath.find("?tags=")!=-1:
        reqtagslist=tagfinder(reqpath)
        for x in Question.objects.all():
            question_id=request.body
            questionobject=x
            question=model_to_dict(questionobject)["question_text"]
            choice=questionobject.choice_set

            optionsdict={}
            for i in questionobject.choice_set.all():
                optionsdict[str(i)]=i.votes
            tagslist=[]
            for i in questionobject.tags_set.all():
                tagslist.append(str(i))
            resultdict={
            "Question":question,
            "OptionVote": optionsdict,
            "Tags": tagslist,
            "QID": x.id
            }

            for i in tagslist:
                for j in reqtagslist:
                    if i==j:
                        for k in resultlist:
                            print(resultdict,"and",k)
                            if resultdict==k:
                                break
                        else:
                            resultlist.append(resultdict)
                            break

                        
        #FinalResult = serialize('json',resultdict,cls=LazyEncoder) 
        FinalResult = json.dumps(resultlist,default=str) 
        return HttpResponse(FinalResult)

    else:
        print("All ques")
        for x in Question.objects.all():
            question_id=request.body
            #questionobject=get_object_or_404(Question,pk=question_id)
            questionobject=x
            question=model_to_dict(questionobject)["question_text"]
            choice=questionobject.choice_set
            #choicedict=SL.dictionarymaker()
            #resultdict=[{"Question":str(question),"OptionVote":{}}]

            optionsdict={}
            for i in questionobject.choice_set.all():
                optionsdict[str(i)]=i.votes
            tagslist=[]
            for i in questionobject.tags_set.all():
                tagslist.append(str(i))
            print("Choice set is",x.id)  #------------------------
            resultdict={
            "Question":question,
            "OptionVote": optionsdict,
            "Tags": tagslist,
            "QID": x.id
            }
            resultlist.append(resultdict)
            print(resultdict)
        #FinalResult = serialize('json',resultdict,cls=LazyEncoder) 
        FinalResult = json.dumps(resultlist,default=str) 
        return HttpResponse(FinalResult)

def GET_tags(request):
    TagList=[]
    for x in Question.objects.all():
            questionobject=x
            question=model_to_dict(questionobject)["question_text"]
            choice=questionobject.choice_set
            optionsdict={}
            for i in questionobject.tags_set.all():
                TagList.append(str(i))
    FinalResult = json.dumps(TagList,default=str) 
    return HttpResponse(FinalResult)
def PUT(request,question_id):
    structure=json.loads(request.body)
    print("Structure is",structure)
    choicevote=structure["incrementOption"]
    questionobject= get_object_or_404(Question, pk=question_id)
    for i in questionobject.choice_set.all():
        if choicevote==str(i):
            i.votes += 1
            i.save()
    return HttpResponse("Successfully Voted!")






