from django.conf import settings
from django.db import models


#질문 게시판 모델
class Question(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=20)
    context = models.TextField()
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,
                                           related_name='like_user_set')

    class Meta:
        ordering = ['-created_at']

    # 로그인된 유저가 게시물에 추천을 누른 유저인지 여부
    def is_like_user(self, user):
        return self.like_user_set.filter(pk=user.pk).exists()
    # 게시물의 총 추천 개수
    def get_likes(self):
        return self.like_user_set.all().count()

# 댓글 모델
class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='Comment')
    context = models.TextField()

    class Meta:
        ordering = ['-created_at']