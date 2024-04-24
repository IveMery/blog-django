from django.test import TestCase

from .models import Board

from .views import *
from django.urls import resolve
from django.urls import reverse

# Create your tests here.

#home
class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
      
        url = reverse('home')
       # print("Board created with ID:", self.board.pk)
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, boardsView)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))

#topics
class BoardTopicsTests(TestCase):
    def setUp(self):
       self.board = Board.objects.create(name='Django', description='This is a board about Django.')

    def test_board_topics_view_success_status_code(self):
       
        url = reverse('board_topics', kwargs={'pk':self.board.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve(reverse('board_topics', kwargs={'pk': self.board.pk}))
        self.assertEqual(view.func, board_topicsView)
