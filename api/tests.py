from django.contrib.auth.models import User
from django.test import TestCase


class OurTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='iamtest', password='test1')

    def test_create_board(self):
        user = User.objects.get(id=1)
        response = self.client.post(
            '/boards/', {'title': 'test board', 'owner': user.id})
        self.assertEqual(response.status_code, 201)

    def test_get_boards(self):
        self.test_create_board()
        response = self.client.get(
            '/boards/', {})
        self.assertEqual(response.status_code, 200)

    def test_create_list(self):
        user = User.objects.get(id=1)
        self.test_create_board()
        response = self.client.post(
            '/lists/', {'title': 'test list',
                        'owner': user.id,
                        'position': '1',
                        'board': '1'})
        self.assertEqual(response.status_code, 201)

    def test_get_lists(self):
        self.test_create_board()
        response = self.client.get(
            '/boards/', {})
        self.assertEqual(response.status_code, 200)

    def test_create_card(self):
        user = User.objects.get(id=1)
        self.test_create_board()
        self.test_create_list()
        response = self.client.post(
            '/cards/', {'title': 'test card',
                        'owner': user.id,
                        'position': '1',
                        'list': '1',
                        'assignee': '1'})
        self.assertEqual(response.status_code, 201)

    def test_get_cards(self):
        self.test_create_board()
        self.test_create_list()
        self.test_create_card()
        response = self.client.get(
            '/cards/', {})
        self.assertEqual(response.status_code, 200)

    def test_create_label(self):
        user = User.objects.get(id=1)
        self.test_create_board()
        response = self.client.post(
            '/labels/', {'title': 'test card',
                         'owner': user.id,
                         'board': '1'})
        self.assertEqual(response.status_code, 201)

    def test_get_labels(self):
        self.test_create_board()
        self.test_create_label()
        response = self.client.get(
            '/labels/', {})
        self.assertEqual(response.status_code, 200)
