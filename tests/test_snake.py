
import pytest

from src.entyties import Snake








def test_stat_len_snake():
    snake = Snake()
    assert len(snake.body) == 1


def test_choose_head_direction():
    snake = Snake()
    snake.head.get_direction() == "right":
    snake.set_delta_x(self.get_speed())
    snake.set_delta_y(0)

def test_add_chain():


