from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from course.models import Lesson, Course
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create(email="test@mail.ru", is_superuser=True, is_staff=True)
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        data = {
            "title": "test_create1",
            "description": "test_create1"
        }
        response = self.client.post(
            '/lesson/create/',
            data=data,
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'title': 'test_create1', 'image': None, 'description': 'test_create1', 'url': None, 'course': None,
             'owner': None}
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_list_lesson(self):
        response = self.client.get(
            '/lesson/',
        )
        print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """Тестирование удаления урока"""

        lesson = Lesson.objects.create(
            title='Test_lesson',
            description='Test_lesson',
            owner=self.user
        )

        response = self.client.delete(
            f'/lesson/delete/{lesson.id}/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email="test@gmail.com", is_superuser=True, is_staff=True)
        self.client.force_authenticate(user=self.user)
        Course.objects.create(title='test')

    def test_subscribe_to_course(self):

        data = {
            "course_id": 1,
            "user": 1
        }

        response = self.client.post(
            '/subscription/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'message': 'Subscription create'}
        )