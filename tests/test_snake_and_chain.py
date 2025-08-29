import os
import sys


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)
os.chdir(PROJECT_ROOT)


import pytest
import pygame

from src.entyties import Snake, Chain
from unittest.mock import Mock

from src.texts_images_sounds import main_sound


@pytest.fixture()
def create_snake():

    screen = pygame.display.set_mode((500, 500))
    snake = Snake(screen)
    return snake

@pytest.fixture()
def create_chain():
    chain = Chain(None, None, None)
    return chain



def test_stat_len_snake(create_snake):
    assert len(create_snake.body) == 1


def test_add_chain(create_snake, create_chain):
    test_snake = create_snake
    test_snake.add_chain()
    assert len(test_snake.body)==2



def test_choose_head_direction(create_snake):
    test_snake = create_snake
    delta_x1 = test_snake.get_delta_x()
    test_snake.choose_head_direction()
    delta_x2 = test_snake.get_delta_x()
    assert delta_x1 + 5 == delta_x2

def test_choose_head_direction2(create_snake):
    test_snake = create_snake
    delta_y1 = test_snake.get_delta_y()
    test_snake.head.set_direction("down")
    test_snake.choose_head_direction()
    delta_y2 = test_snake.get_delta_y()
    assert delta_y1 + 5 == delta_y2