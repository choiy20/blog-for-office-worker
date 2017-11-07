from django.shortcuts import render
from .models import Article, Comment, HashTag
# Create your views here.
def index(request):
    article_list = Article.objects.all() #전체 아티클 리스트 가져오기
    hashtag_list = HashTag.objects.all()
    ctx = {
        "article_list" : article_list,
        "hashtag_list" : hashtag_list,
    }
    return render(request, "index.html", ctx)
    # pass라고 끝내면 index에 해당하는 부분을 구현하지 않겠다 (의도적으로 비워두었다라고 말해주는거)

def detail(request):
    pass

# def about(request):
#     pass
