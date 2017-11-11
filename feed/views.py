from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Article, Comment, HashTag
# Create your views here.
def index(request):

    # GET & POST
    category = request.GET.get("category")
    hashtag = request.GET.get("hashtag")
    hashtag_list = HashTag.objects.all()

    if not category and not hashtag:
        article_list = Article.objects.all()
    elif category:
        article_list = Article.objects.filter(category=category)

    else:
        article_list = Article.objects.filter(hashtag__name=hashtag)

    # category_list = set([])
    # for article in article_list:
    #     category_list.add(article.get_category_display())
    # print(category_list)

    # category_list = set([
    #     article.get_category_display()
    #     for article in article_list
    # ])

    category_list = set([
        (article.category, article.get_category_display())
        for article in article_list
    ])

    print(request.GET)

    ctx = {
        "article_list" : article_list,
        "hashtag_list" : hashtag_list,
        "category_list" : category_list,
    }
    return render(request, "index.html", ctx)
    # pass라고 끝내면 index에 해당하는 부분을 구현하지 않겠다 (의도적으로 비워두었다라고 말해주는거)

def detail(request, article_id):
    # GET & POST

    article = Article.objects.get(id=article_id)
    # comment_list = Comment.objects.filter(article__id=article_id)
    # comment_list = article.article_comments.all()
    hashtag_list = HashTag.objects.all()
    ctx = {
        "article" : article,
        # "comment_list": comment_list,
        "hashtag_list" : hashtag_list,
    }

    if request.method == "GET":
        pass
    elif request.method =="POST":
        username = request.POST.get("username")
        content = request.POST.get("content")
        # print(username)
        # print(content)
        Comment.objects.create(
            article=article,
            username=username,
            content=content,
        )

        return HttpResponseRedirect("/{}/".format(article_id))

    return render(request, "detail.html", ctx)

# def about(request):
#     pass
