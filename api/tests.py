from django.contrib.auth.models import User
from django.test import TestCase


class OurTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='iamtest', password='test1')

    def create_board(self):
        user = User.objects.get(id=1)
        response = self.client.post(
            '/boards/', {'title': 'test board', 'owner': user.id})
        return response.data['id']

    def create_list(self, board_id):
        user = User.objects.get(id=1)
        response = self.client.post(
            '/lists/', {'title': 'test list',
                        'owner': user.id,
                        'position': '1',
                        'board': board_id})
        return response.data['id']

    def create_card(self, list_id):
        user = User.objects.get(id=1)
        response = self.client.post(
            '/cards/', {'title': 'test card',
                        'owner': user.id,
                        'position': '1',
                        'list': list_id,
                        'assignee': '1'})
        return response.data['id']

    def create_labels(self, board_id):
        user = User.objects.get(id=1)
        response = self.client.post(
            '/labels/', {'title': 'test card',
                         'owner': user.id,
                         'board': board_id})
        return response.data['id']

    def test_create_board(self):
        user = User.objects.get(id=1)
        response = self.client.post(
            '/boards/', {'title': 'test board', 'owner': user.id})
        self.assertEqual(response.status_code, 201)

    def test_get_boards(self):
        self.create_board()
        response = self.client.get(
            '/boards/', {})
        self.assertEqual(response.status_code, 200)

    def test_create_list(self):
        user = User.objects.get(id=1)
        id = self.create_board()
        response = self.client.post(
            '/lists/', {'title': 'test list',
                        'owner': user.id,
                        'position': '1',
                        'board': id})
        self.assertEqual(response.status_code, 201)

    def test_get_lists(self):
        board_id = self.create_board()
        self.create_list(board_id)
        response = self.client.get(
            '/lists/', {})
        self.assertEqual(response.status_code, 200)

    def test_create_card(self):
        user = User.objects.get(id=1)
        board_id = self.create_board()
        list_id = self.create_list(board_id)
        response = self.client.post(
            '/cards/', {'title': 'test card',
                        'owner': user.id,
                        'position': '1',
                        'list': list_id,
                        'assignee': '1'})
        self.assertEqual(response.status_code, 201)

    def test_get_cards(self):
        board_id = self.create_board()
        list_id = self.create_list(board_id)
        self.create_card(list_id)
        response = self.client.get(
            '/cards/', {})
        self.assertEqual(response.status_code, 200)

    def test_create_label(self):
        user = User.objects.get(id=1)
        board_id = self.create_board()
        response = self.client.post(
            '/labels/', {'title': 'test card',
                         'owner': user.id,
                         'board': board_id})
        self.assertEqual(response.status_code, 201)

    def test_get_labels(self):
        board_id = self.create_board()
        self.create_labels(board_id)
        response = self.client.get(
            '/labels/', {})
        self.assertEqual(response.status_code, 200)
