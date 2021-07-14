from django.contrib.auth import get_user_model
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Question, Comment
from .serializers import SignupSerializer, QuestionSerializer, CommentSerializer
from rest_framework_simplejwt.tokens import RefreshToken
import numpy as np


class SignupView(CreateAPIView):
    model = get_user_model()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

    # 계정 생성과 동시에 토큰 발급을 위한 로직
    def create(self, request, *args, **kwargs):
        def get_tokens_for_user(user):
            refresh = RefreshToken.for_user(user)

            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        return Response(get_tokens_for_user(self.request.user))



class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'context']

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)

    # 추천 기능
    @action(detail=True, methods=['POST'])
    def like(self, request,pk):
        post = self.get_object()
        post.like_user_set.add(self.request.user.pk)
        return Response(status.HTTP_201_CREATED)

    @like.mapping.delete
    def unlike(self,request,pk):
        post = self.get_object()
        post.like_user_set.remove(self.request.user.pk)
        return Response(status.HTTP_204_NO_CONTENT)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(post=self.kwargs['q_id'])
        return qs

    def perform_create(self, serializer):
        author = self.request.user
        post = Question.objects.get(pk=self.kwargs['q_id'])
        serializer.save(author=author, post=post)

# 질문 작성일 기준 각 월별 전체 질문 중에서 가장 좋아요가 많은
# 질문을 출력하는 API
class QOfMonth(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        arr = []
        result_pk = []
        for o in qs:
            arr.append([o.get_likes(), o.pk, o.created_at.strftime("%b")])

        arr.sort(reverse=True)
        arr = np.array(arr)
        for i in range(12):
            try:
                result_pk.append(arr[0][1].tolist())
                rows, cols = np.where(arr == arr[0][2])
                arr = np.delete(arr, rows, axis=0)
            except:
                break
        qs = qs.filter(pk__in=result_pk)
        qs = qs.order_by('created_at')
        return qs