import pytest
from board import Board


@pytest.fixture
def create_test_boards():
    def in_list(x, combi):
        return "X" if x in combi else 0

    init_field = {pos: 0 for pos in range(1, 10)}

    win_combi = [
        [1, 2, 3],
        [1, 5, 9],
        [1, 4, 7],
        [4, 5, 6],
        [7, 8, 9],
        [2, 5, 8],
        [3, 6, 9],
        [3, 5, 7],
    ]
    winning_field = [
        {field_id: in_list(field_id, comb) for field_id in range(1, 10)}
        for comb in win_combi
    ]

    # todo: comments (ugly looping)
    board_list = []
    for field_it in range(1, 10):
        board = [
            {
                i: (field.copy() if i == field_it else init_field.copy())
                for i in range(1, 10)
            }
            for field in winning_field
        ]
        board_list.extend(board.copy())


def test_initboard_empty():
    """Test empty board initialization.
    """
    board_obj = Board("X", "O")
    assert board_obj.insertions == []
    assert board_obj.playerA == "X"
    assert board_obj.playerB == "O"
    assert board_obj.state == {i: {j: 0 for j in range(1, 10)} for i in range(1, 10)}
    assert board_obj.insertion_order == []
    assert board_obj.finished_tables == {tbl_no: 0 for tbl_no in range(1, 10)}


def test_initboard_bystate():
    for filled_field in range(1, 10):
        state_dict[filled_field] = {j: "X" for j in range(1, 10)}
        state_dict = {i: 0 for i in range(1, 10)}
        finished_tables = {tbl_no: 0 for tbl_no in range(1, 10)}

        board_obj = Board(playerA="X", playerB="O", board_dict=state_dict)
