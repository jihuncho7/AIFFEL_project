import json
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.test import TestCase,Client
from rest_framework_simplejwt.tokens import RefreshToken
from MainApp.models import Comment, Question


class SignUp(TestCase):
    client = Client()

    def test_signup_success(self):
        data = {
            'username': 'test9',
            'password': 'test9',
        }

        response = self.client.post('/signup/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)



class CRUDS(TestCase):

    def api_client(self):
        user = User.objects.create_user(username='john', password='js.sj')
        client = APIClient()
        refresh = RefreshToken.for_user(user)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

        return client

    def setUp(self):
        User.objects.create(username="user1",password='user1')
        User.objects.create(username="user2",password='user2')
        Comment.objects.create(context='cont', post_id=1, author=User.objects.first(), author_id=1)
        """
        
        qofmonth test를 위한 포스트 생성
       
        """

        for i in range(1,13):
            b =Question.objects.create(title=f'{i}',context='aef',author=User.objects.first(),author_id=1)
            Question.objects.filter(pk=b.pk).update(created_at=f"2021-{i}-13T20:35:00.221560Z")
            a = Question.objects.create(title=f'{i}',context='aef',author=User.objects.first(),author_id=1)
            Question.objects.filter(pk=a.pk).update(created_at=f"2021-{i}-13T20:35:00.221560Z")
            a.like_user_set.add(1,2)



    '''
    Question CRUD + Like func
    '''

    def test_post_question_success(self):
        data = {
            'title': 'title test',
            'context': 'context test',
        }

        response = self.api_client().post('/question/', data,format='json')
        self.assertEqual(response.status_code, 201)

    def test_post_question_invalid_error(self):
        data = {
            'titleggaeg': 'title test',
            'context': 'context test',
        }

        response = self.api_client().post('/question/', data,format='json')
        self.assertEqual(response.status_code, 400)

    def test_put_question_success(self):
        data = {
            'title': 'title test fixed',
            'context': 'context test fixed',
        }

        response = self.api_client().put('/question/1', data,format='json')
        self.assertEqual(response.status_code, 301)

    def test_delete_question_success(self):

        response = self.api_client().delete('/question/1',format='json')
        self.assertEqual(response.status_code, 301)

    def test_post_question_like_success(self):

        response = self.api_client().post('/question/1/like/',format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete_question_unlike_success(self):

        response = self.api_client().delete('/question/1/like/',format='json')
        self.assertEqual(response.status_code, 200)

    def test_get_search_question_success(self):

        response = self.api_client().get('/question/?search=aef',format='json')
        self.assertEqual(response.status_code, 200)

    def test_qofmonth_success(self):

            response = self.api_client().get('/qofmonth/', format='json')
            output_dict = [x for x in response.data if x['get_likes']!=2]
            output_json = json.dumps(output_dict)
            self.assertEqual(output_json, '[]')

    '''
    comment CRUD
    '''

    def test_post_comment_success(self):
        data = {
            'context': 'context test',
        }

        response = self.api_client().post('/question/1/comment/', data,format='json')
        self.assertEqual(response.status_code, 201)

    def test_put_comment_success(self):
        data = {
            'context': 'context test fixed',
        }

        response = self.api_client().put('/question/1/comment/1', data,format='json')
        self.assertEqual(response.status_code, 301)

    def test_delete_comment_success(self):
        data = {
            'context': 'context test fixed',
        }

        response = self.api_client().delete('/question/1/comment/1', data,format='json')
        self.assertEqual(response.status_code, 301)



