from django.contrib.auth.models import User
from django.test import TestCase

from .models import Boards, Lists, Cards


class OurTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='iamtest', password='test1')

    def test_create_board(self):
        user = User.objects.get(id=1)
        response = self.client.post(
            '/boards/', {'title': 'test board', 'owner': user.id})
        print(response.data)
        self.assertEqual(response.status_code, 201)

    def test_create_list(self):
        user = User.objects.get(id=1)
        response = self.client.post(
            '/lists/', {'title': 'test list', 'owner': user.pk, 'board': '1'})
        print(response.data)
        self.assertEqual(response.status_code, 201)

    # def test_list_boards(self):
    #     response = self.client.get('/boards/')
    #     output = response.data[0]
    #     # check that its a valid endpoint
    #     self.assertEqual(response.status_code, 200)
    #     # check that theres atleast one board
    #     self.assertEqual(output['pk'],1)
    #     return output

    # def test_list_lists(self):
    #     board_pk = test_list_boards()
    #     self.test_list_boards()
    #     response = self.client.get('/lists/')
    #     self.assertEqual(response.status_code,200)

    # def test_list_cards(self):
    #     response = self.client.get('/cards/')
    #     self.assertEqual(response.status_code,200)


# from django.test import TestCase
# from django.contrib.auth.models import User
# from .models import Boards, Lists, Cards

# # Create your tests here.
# class setUpTestData(TestCase):
#     @classmethod # what is this?
#     def setUpTestData(cls): # what is CLS?

#         testuser = User.objects.create_user(username='iamtest', password='test1')
#         testuser.save()

#         # create a board
#         test_board = Boards.objects.create(title='Test Board', owner=testuser)
#         test_board.save()
#         print(dir(test_board))

#         # # create a list
#         test_list = Lists.objects.create(title='Test List', owner=testuser, board=test_board.id)
#         test_list.save()

#     def test_check_board(self):
#         board = Boards.objects.get(id=1)
#         expected_title = f'{board.title}' # WHAT DOES THIS DO?
#         expected_owner = f'{board.owner_id}' # WHAT DOES THIS DO?

#         self.assertEqual(expected_title, 'Test Board')
#         self.assertEqual(expected_owner, '1')

#     def test_list(self):
#         list = Lists.objects.get(id=1)
#         expected_title = f'{list.title}'
#         expected_board = f'{list.board}'
#         print(expected_board)

#         self.assertEqual(expected_title, 'Test List')
#         self.assertEqual(expected_board, '1')
