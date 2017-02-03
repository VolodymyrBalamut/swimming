from django.shortcuts import render,render_to_response,get_object_or_404,redirect,HttpResponseRedirect, get_list_or_404
from django.contrib import auth
from django.db.models import Q
from article.models import *
from article.forms import CommentForm
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    context = {
        'username': auth.get_user(request).username
    }
    return render_to_response('home.html',context)
def history(request):
    context = {
        'username': auth.get_user(request).username
    }
    return render_to_response('history.html',context)
def technique(request):
    styles = Style.objects.all()
    context = {
        'styles': styles,
        'username': auth.get_user(request).username
    }
    return render_to_response('technique.html', context)
#@csrf_protect
def record(request):
    gender = request.GET.get("gender")
    men = True
    women = True
    male = Record.objects.filter(swimmer__male=True).order_by('style__style')
    female = Record.objects.filter(swimmer__male=False).order_by('style__style')
    if gender != "all":
        if gender == "men":
            men = True
            women = False
        elif gender == "women":
            men = False
            women = True
    filter = request.GET.get("filter")
    if filter:
        if men:
            male = Record.objects.filter(swimmer__male=True).order_by('style__style').filter(
                Q(swimmer__name__icontains = filter)|
                Q(swimmer__nationality__country_name__contains=filter)|
                Q(style__style__contains=filter)
            )
        if women:
            female = Record.objects.filter(swimmer__male=False).order_by('style__style').filter(
                Q(swimmer__name__icontains= filter)|
                Q(swimmer__nationality__country_name__contains=filter)|
                Q(style__style__contains=filter)
            )
    context = {
        'male': male,
        'female': female,
        'filter':filter,
        'gender':gender,
        'men':men,
        'women':women,
        'username': auth.get_user(request).username
    }
    return render_to_response('record.html',context)
def articles(request,page_number=1):
    articles = Article.objects.all()
    current_page = Paginator(articles,2)
    context = {
        'articles':current_page.page(page_number),
        'username':auth.get_user(request).username
    }
    return render_to_response('articles.html', context)
@csrf_protect
def article(request,id=None):
    article = get_object_or_404(Article,id = id)
    comments = Comments.objects.filter(comments_article=id)
    form = CommentForm
    context = {
        'article': article,
        'comments':comments,
        'form':form,
        'username': auth.get_user(request).username
    }
    return render(request,'article.html',context)
def addlike(request,id = None):
    article = get_object_or_404(Article, id=id)
    article.article_like += 1
    article.save()
    return redirect('/articles/%s/'%id)

def addcomment(request,id=None):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.comments_article = get_object_or_404(Article,id = id)
        comment.save()
    return redirect('/articles/%s/'%id)

def swimmer(request,id=None):
    swimmer =get_object_or_404(Swimmer,id = id)
    context = {
        'swimmer':swimmer,
        'username': auth.get_user(request).username
    }
    return render(request, 'swimmer.html', context)
def country(request,id=None):
    country =get_object_or_404(Country,id = id)
    context = {
        'country':country,
        'username': auth.get_user(request).username
    }
    return render(request, 'country.html', context)




    # female = get_list_or_404(Record,swimmer__male=False).order_by('style__style')
    # male = get_list_or_404(Record,swimmer__male=True).order_by(style__style)
#'freestyle_female': get_list_or_404(female, style__style='Freestyle'),
        #'butterfly_male': get_list_or_404(male, style__style='Butterfly'),
        #'butterfly_female': get_list_or_404(female, style__style='Butterfly'),
        #'breaststroke_male': get_list_or_404(male, style__style='Breaststroke'),
        #'breaststroke_female': get_list_or_404(female, style__style='Breaststroke'),
        #'backstroke_male': get_list_or_404(male, style__style='Backstroke'),
        #'backstroke_female': get_list_or_404(female, style__style='Backstroke'),
        #'medley_male': get_list_or_404(male, style__style='Medley'),
        #'medley_female': get_list_or_404(female, style__style='Medley'),