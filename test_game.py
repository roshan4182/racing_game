import unittest
import pygame
import os
from index import *

class TestGame(unittest.TestCase):
    def setUp(self):
        # Define the necessary constants and variables before each test
        self.directory_path = '/Users/roshan1610/Downloads/Road Rush Game using Pygame'
        self.SAVE_FILE_PATH = os.path.join(self.directory_path, 'data', 'save.dat')

    def test_player_initial_position(self):
        player_rect = pygame.Rect((WINDOWWIDTH / 2, WINDOWHEIGHT - 50), (19, 47))
        self.assertEqual(player_rect.x, WINDOWWIDTH / 2)
        self.assertEqual(player_rect.y, WINDOWHEIGHT - 50)

    def test_player_movement(self):
        player_rect = pygame.Rect((WINDOWWIDTH / 2, WINDOWHEIGHT - 50), (19, 47))

        # Test move_up function
        player_rect.move_ip(0, -PLAYERMOVERATE)
        self.assertEqual(player_rect.y, WINDOWHEIGHT - 50 - PLAYERMOVERATE)

        # Test move_down function
        player_rect.move_ip(0, PLAYERMOVERATE)
        self.assertEqual(player_rect.y, WINDOWHEIGHT - 50)

        # Test move_left function
        player_rect.move_ip(-PLAYERMOVERATE, 0)
        self.assertEqual(player_rect.x, WINDOWWIDTH / 2 - PLAYERMOVERATE)

        # Test move_right function
        player_rect.move_ip(PLAYERMOVERATE, 0)
        self.assertEqual(player_rect.x, WINDOWWIDTH / 2)

    def test_baddie_creation(self):
        baddie = {'rect': pygame.Rect(0, 0, 20, 20), 'speed': 8, 'surface': pygame.Surface((20, 20))}
        self.assertIsNotNone(baddie['surface'])
        self.assertIsNotNone(baddie['rect'])
        self.assertGreaterEqual(baddie['speed'], BADDIEMINSPEED)

    def test_player_hit_baddie(self):
        player_rect = pygame.Rect((WINDOWWIDTH / 2, WINDOWHEIGHT - 50), (19, 47))
        baddie = {'rect': pygame.Rect(player_rect.x, player_rect.y, 20, 20)}  # Set baddie's position same as player
        self.assertTrue(playerHasHitBaddie(player_rect, [baddie]))

    def test_top_score_file_created(self):
        self.assertTrue(os.path.exists(self.SAVE_FILE_PATH))

    def test_top_score_initial_value(self):
        with open(self.SAVE_FILE_PATH, 'r') as f:
            top_score = int(f.read())
        self.assertEqual(top_score, 0)

if __name__ == '__main__':
    unittest.main()
