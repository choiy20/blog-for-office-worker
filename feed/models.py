from django.db import models

# Create your models here.
class Article(models.Model):
    DEVELOPMENT = "dv" #대문자로 써주는건 이후에 우리가 변경하지 않는다라는 걸 의미.
    PERSONAL = "ps"
    CATEGORY_CHOICES = (
        (DEVELOPMENT, "development"),
        (PERSONAL, "personal"),
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(
        max_length=2,
        choices = CATEGORY_CHOICES,
        default = DEVELOPMENT,
    )

    def __str__(self):
        return self.title #title로 아티클 구분을 해주겠다라는 뜻
# self를 쓰는 이유는 클래스안에 변수에 접근하기 위해서이다.

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # CASCADE -> Article이 지워지면 코멘트도 따라서 지워지는 기능
    username = models.CharField(max_length=50)
    content = models.CharField(max_length=200)

    def __str__(self):
        return "{} commented in ''{}'': {}".format(self.username, self.article.title, self.content)

class HashTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
