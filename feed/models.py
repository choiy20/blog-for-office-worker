from django.db import models

class HashTag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Article(models.Model):
    DEVELOPMENT = "dv" #대문자로 써주는건 이후에 우리가 변경하지 않는다라는 걸 의미.
    PERSONAL = "ps"
    CATEGORY_CHOICES = (
        (DEVELOPMENT, "development"),
        (PERSONAL, "personal"),
    )
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=400)
    content = models.TextField()
    category = models.CharField(
        max_length=2,
        choices = CATEGORY_CHOICES,
        default = DEVELOPMENT,
    )

    hashtag = models.ManyToManyField(HashTag)

    def __str__(self):
        return self.title #title로 아티클 구분을 해주겠다라는 뜻
# self를 쓰는 이유는 클래스안에 변수에 접근하기 위해서이다.


class Comment(models.Model):
    APPROVED = "ap"
    NOTAPPROVED = "na"
    COMMENT_CHOICES = (
        (APPROVED, "approved"),
        (NOTAPPROVED, "not approved"),
    )
    article = models.ForeignKey(
        Article,
        related_name="article_comments",
        on_delete=models.CASCADE,
    )
    # CASCADE -> Article이 지워지면 코멘트도 따라서 지워지는 기능
    username = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    # created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.CharField(
        max_length=2,
        choices = COMMENT_CHOICES,
        default=NOTAPPROVED,
    )

    def __str__(self):
        return "{} commented in ''{}'': {}".format(self.username, self.article.title, self.content)

# class Heading(models.Model):
#     heading = models.CharField(max_length=500)
#     def __str__(self):
#         return self.heading
#
# class Subeading(models.Model):
#     subheading = models.CharField(max_length=500)
#     def __str__(self):
#         return self.subheading
