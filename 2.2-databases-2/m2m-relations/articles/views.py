from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    context = {
        'object_list': Article.objects.all().prefetch_related('scopes')
    }

    articles = Article.objects.all()
    for article in articles:
        for scope in article.scopes.all():
            print(scope.tag.name)

    return render(request, template, context)
