from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from course.models import Lesson
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
    {'title': 'test_create1', 'image': None, 'description': 'test_create1', 'url': None, 'course': None, 'owner': None}
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

    def test_destroy_lesson(self):

        Lesson.objects.create(
            title='del_test',
            description='del_test'
        )
        response = self.client.delete(
            '/lesson/delete/8/',
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

