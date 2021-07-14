
from rest_framework import serializers
from django.contrib.auth import get_user_model


from MainApp.models import Question, Comment

User = get_user_model()
base_read_only_field = 'author'


# 계정 가입
class SignupSerializer(serializers.ModelSerializer):
    # write only for not showing password on return
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['pk','username','password']


# 댓글
class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ([base_read_only_field,'post'])


# 질문게시판
class QuestionSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    is_like_user = serializers.SerializerMethodField()
    get_likes = serializers.SerializerMethodField()
    Comment = CommentSerializer(many=True, read_only=True)

    def get_is_like_user(self, instance):
        return instance.is_like_user(self.context['request'].user)

    def get_get_likes(self, instance):
        return instance.get_likes()

    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ([base_read_only_field,'like_user_set'])
