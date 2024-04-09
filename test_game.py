import pygame
import os
from index import *

def test_player_initial_position():
    player_rect = pygame.Rect((WINDOWWIDTH / 2, WINDOWHEIGHT - 50), (19, 47))
    assert player_rect.x == WINDOWWIDTH / 2
    assert player_rect.y == WINDOWHEIGHT - 50

def test_player_movement():
    player_rect = pygame.Rect((WINDOWWIDTH / 2, WINDOWHEIGHT - 50), (19, 47))

    # Test move_up function
    player_rect.move_ip(0, -PLAYERMOVERATE)
    assert player_rect.y == WINDOWHEIGHT - 50 - PLAYERMOVERATE

    # Test move_down function
    player_rect.move_ip(0, PLAYERMOVERATE)
    assert player_rect.y == WINDOWHEIGHT - 50

    # Test move_left function
    player_rect.move_ip(-PLAYERMOVERATE, 0)
    assert player_rect.x == WINDOWWIDTH / 2 - PLAYERMOVERATE

    # Test move_right function
    player_rect.move_ip(PLAYERMOVERATE, 0)
    assert player_rect.x == WINDOWWIDTH / 2

def test_baddie_creation():
    baddie = {'rect': pygame.Rect(0, 0, 20, 20), 'speed': 8, 'surface': pygame.Surface((20, 20))}
    assert baddie['surface'] is not None
    assert baddie['rect'] is not None
    assert baddie['speed'] >= BADDIEMINSPEED

def test_player_hit_baddie():
    player_rect = pygame.Rect((WINDOWWIDTH / 2, WINDOWHEIGHT - 50), (19, 47))
    baddie = {'rect': pygame.Rect(player_rect.x, player_rect.y, 20, 20)}  # Set baddie's position same as player
    assert playerHasHitBaddie(player_rect, [baddie])

def test_top_score_file_created():
    SAVE_FILE_PATH = '/Users/roshan1610/Downloads/Road Rush Game using Pygame/data/save.dat'
    assert os.path.exists(SAVE_FILE_PATH)

def test_top_score_initial_value():
    SAVE_FILE_PATH = '/Users/roshan1610/Downloads/Road Rush Game using Pygame/data/save.dat'
    with open(SAVE_FILE_PATH, 'r') as f:
        top_score = int(f.read())
    assert top_score == 0
