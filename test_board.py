import pytest
from board import Board
from typing import List, Dict
from itertools import product

EMPTY_FIELD = {pos: 0 for pos in range(1, 10)}


@pytest.fixture
def example_test_boards():
    def in_list(x, combi):
        return "X" if x in combi else 0

    def get_winning_field_board(field_it: int, field: List[int]) -> Dict:
        """Create a board with a winning field combination at a given field.

        Arguments:
            field_it {int} -- field number the winning combination should be set
            field {List[int]} -- winning field combination like [1, 5, 9]

        Returns:
            Dict -- Board dict state
        """

        return {
            i: (field.copy() if i == field_it else EMPTY_FIELD.copy())
            for i in range(1, 10)
        }

    # all possible winning combinations at a field
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

    # transform items from win_combi into field dictionaries
    winning_field = [
        {field_id: in_list(field_id, comb) for field_id in range(1, 10)}
        for comb in win_combi
    ]

    # Create a complete boards with exactly one of the winning field combination for all
    # possible fields.
    board_list = []
    for field_it in range(1, 10):
        finished_tbl = {tbl: 0 for tbl in range(1, 10)}
        finished_tbl[field_it] = "X"
        board = [get_winning_field_board(field_it, field) for field in winning_field]
        finished_list = [finished_tbl.copy() for field in winning_field]
        board_list.extend(zip(board.copy(), finished_list.copy()))

    return board_list


def test_initboard_empty():
    """Test empty board initialization.
    """
    board_obj = Board()
    assert board_obj.insertions == []
    assert board_obj.playerA == "X"
    assert board_obj.playerB == "O"
    assert board_obj.state == {i: {j: 0 for j in range(1, 10)} for i in range(1, 10)}
    assert board_obj.insertion_order == []
    assert board_obj.finished_tables == {tbl_no: 0 for tbl_no in range(1, 10)}


def test_initboard_bystate(example_test_boards: Dict):
    """Test board initialization with board state.

    Arguments:
        example_test_boards {Dict} -- 
    """
    for (board_state, finished_tbl) in example_test_boards:

        board_obj = Board(playerA="X", playerB="O", board_dict=board_state)
        assert board_obj.state == board_state
        assert board_obj.finished_tables == finished_tbl


def test_legal_move():
    # create test for invalid insert
    empty_board = Board()
    assert empty_board.is_legal_move(1, 10) is False
    assert empty_board.is_legal_move(10, 1) is False
    assert empty_board.is_legal_move(10, 10) is False

    # create empty board for second test case
    empty_board = Board()
    for field in range(1, 10):
        for pos in range(1, 10):
            assert empty_board.is_legal_move(field, pos) is True

    # create board for third test case if a field is finished
    board_state = {i: {j: 0 for j in range(1, 10)} for i in range(1, 10)}
    board_state[1][1] = "X"
    board_state[1][5] = "X"
    board_state[1][9] = "X"
    inserted_board = Board(
        board_dict=board_state, insertion_order=[[1, 1], [1, 9], [1, 5]]
    )
    for field in range(1, 10):
        for pos in range(1, 10):
            if field is 1:
                assert inserted_board.is_legal_move(field, pos) is False
            elif field is 5:
                assert inserted_board.is_legal_move(field, pos) is True
            else:
                assert inserted_board.is_legal_move(field, pos) is False

    # create board for second test case if a field is finished
    board_state = {i: {j: 0 for j in range(1, 10)} for i in range(1, 10)}
    for field, pos in product([1, 5], [1, 5, 9]):
        board_state[field][pos] = "X"

    inserted_board = Board(
        board_dict=board_state,
        insertion_order=[[5, 1], [5, 9], [5, 5], [1, 1], [1, 9], [1, 5]],
    )
    for field in range(1, 10):
        for pos in range(1, 10):
            if field is 1:
                assert inserted_board.is_legal_move(field, pos) is False
            elif field is 5:
                assert inserted_board.is_legal_move(field, pos) is False
            else:
                assert inserted_board.is_legal_move(field, pos) is True

    # create test for inserting in a finished table position
    empty_board = Board()
    empty_board.state[9][1] = "X"
    for field in range(1, 10):
        for pos in range(1, 10):
            if (field is 9) and (pos is 1):
                assert empty_board.is_legal_move(field, pos) is False
            else:
                assert empty_board.is_legal_move(field, pos) is True
