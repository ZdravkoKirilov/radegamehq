from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from .models import Game


class GameModelTestCase(TestCase):
    def setUp(self):
        self.gameTitle = 'Example game title'
        self.game = Game(title=self.gameTitle)

    def test_model_can_create_a_game(self):
        old_count = Game.objects.count()
        self.game.save()
        new_count = Game.objects.count()
        self.assertNotEqual(old_count, new_count)


class GameViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.game_data = {'title': 'Example title'}
        self.response = self.client.post(
            reverse('create'),
            self.game_data,
            format="json"
        )

    def test_api_can_create_a_game(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_game(self):
        game = Game.objects.get()
        response = self.client.get(
            reverse('details', kwargs={'pk': game.id}), format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, game)

    def test_api_can_update_a_game(self):
        change_game = {'title': 'A new title'}
        game = Game.objects.get()
        res = self.client.put(
            reverse('details', kwargs={'pk': game.id}),
            change_game, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_game(self):
        game = Game.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': game.id}),
            format='json',
            follow=True
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
