from django.shortcuts import render

# Create your views here.


from firstapp.models import People, Article

def index(request):
    context = {}
    article_list = Article.objects.all()
    context['article_list'] = article_list
    index_page = render(request, 'first_web.html', context)
    return index_page