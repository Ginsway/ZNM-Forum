from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import ArticleForm


@login_required()
@csrf_exempt
def post_article(request):
    if request.method == 'POST':
        article_form = ArticleForm(data=request.POST)
        if article_form.is_valid():
            article_cd = article_form.cleaned_data
            try:
                new_article = article_form.save(commit=False)
                new_article.author = request.user
                new_article.save()
                return HttpResponse('1')
            except:
                return HttpResponse('2')
        else:
            return HttpResponse('3')
    else:
        article_form = ArticleForm()
        return render(request, 'article/post_article.html', {'article_form': article_form})

# Create your views here.
