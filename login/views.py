# from forms import CommentForm,ArticleForm


from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import message
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context_processors import csrf
from django.utils import timezone

from login.forms import ArticleForm
from login.models import Articles
from loginOut import settings


@login_required
def articles(request):
    language = 'en-gb'
    session_language = 'en-gb'
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    return render_to_response('articles.html', {'articles': Articles.objects.all(), 'language': language,
                                                'session_language': session_language})


@login_required
def article(request, article_id=1):
    return render(request, 'article.html', {'article': Articles.objects.get(id=article_id)})


@login_required
def language(request, language='en-gb'):
    response = HttpResponse('setting language %s' % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    return response


@login_required
def create(request):
    if request.POST:

        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form.user_article = request.user
            form.save()
            # messages.add_message(request,message.SUCCESS,'your article was added')
            return HttpResponseRedirect('/articles/all')
    else:
        form = ArticleForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('create_article.html', args)


@login_required
def like_article(request, article_id):
    print '&&&&&&&&&&&&&&&&&&&&&'
    if article_id:
        a = Articles.objects.get(id=article_id)
        count = a.like
        a.like = count + 1


        a.save()

    return HttpResponseRedirect('/articles/get/%s' % article_id)


'''
def add_comment(request, article_id):
    a = Articles.objects.get(id=article_id)
    if request.method == 'POST':
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.article = a
            messages.success(request, "your comment was added")
            return HttpResponse('/articles/get/%s' % article_id)
    else:
        f = CommentForm()
    args = {}
    args.update(csrf(request))
    args['article'] = a
    args['form'] = f
    return render_to_response('add_comment.html', args)


def delete_comment(request, comment_id):
    c = Comment.objects.get(id=comment_id)
    article_id = c.article.id
    messages.add_message(request, settings.DETELE_MESSAGE, "Your message was deleted")
    return HttpResponseRedirect('articles/get/%s' % article_id)


def search_titles(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
        articles = Articles.objects.filter(title_contains=search_text)
        return render_to_response('ajax_search.html', {'article': articles})
'''
