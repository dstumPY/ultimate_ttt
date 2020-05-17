from typing import Any, Dict, List
from copy import deepcopy


class Board:
    """ This Board class defines the data structure for the game 
        Ultimate Tic-Tac-Toe. A Board is separated in 9 tables. Every
        single table is build as a normal tic-tac-toe field, which consists
        of the positions 1 to 9. The positions were arranged as 3 rows with 
        3 postitions one below the other. See this example:

            +---+---+---+---+---+---+---+---+---+
            |           |           |           |
            |   +   +   +   +   +   +   +   +   |
            |   table1  |   table2  |    table3 |
            |   +   +   +   +   +   +   +   +   |
            |           |           |           |
            +---+---+---+---+---+---+---+---+---+
            |           |           |           |
            |   +   +   +   +   +   +   +   +   |
            |   table4  |   table5  |    table6 |
            |   +   +   +   +   +   +   +   +   |
            |           |           |           |
            +---+---+---+---+---+---+---+---+---+
            |           |           |           |
            |   +   +   +   +   +   +   +   +   |
            |   table7  |   table8  |    table9 |
            |   +   +   +   +   +   +   +   +   |
            |           |           |           |
            +---+---+---+---+---+---+---+---+---+
                  
            Similar to the complete board table1
            themselve is defined by 9 positions

            +---+---+---+---+---+---+---+---+---+
            | 1   2   3 |           |           |
            |   +   +   +   +   +   +   +   +   |
positions-->| 4   5   6 |   table2  |   table3  |
            |   +   +   +   +   +   +   +   +   |
            | 7   8   9 |           |           |
            +---+---+---+---+---+---+---+---+---+
            |           |           |           |
            |   +   +   +   +   +   +   +   +   |
            |   table4  |   table5  |   table6  |
            |   +   +   +   +   +   +   +   +   |
            |           |           |           |
            +---+---+---+---+---+---+---+---+---+
            |           |           |           |
            |   +   +   +   +   +   +   +   +   |
            |   table7  |   table8  |   table9  |
            |   +   +   +   +   +   +   +   +   |
            |           |           |           |
            +---+---+---+---+---+---+---+---+---+

            Every board is built on a given state dictionary or
            will be initialized with zero values and the player will be
            filling the board respecting the gaming rules.

    Raises:
    
    Returns:
        Board -- Ultimate Tic-Tac-Toe Bord instance that represents 
                 the current state
    """

    def __init__(
        self,
        playerA: str,
        playerB: str,
        board_dict: Dict = None,
        insertion_order: List = None,
    ):
        """Create a Board object. This initializer provides the function
            to set up an empty board filled with zeros. In that case only
            playerA and playerB as parameter input is required. It's
            also possible to set up a given board. This requires a
            non-empty insertion-order list.
        
            Keyword Arguments:
            playerA {str} -- player encoding for boards
            playerB {str} -- player encoding for boards
        
            board_dict {Dict}       -- Dict which represents a Board with keys 
                                        representing the table numbers (1 to 9)
                                        and values as Dicts representing the 
                                        positions and their value (default: {None})
                                        Example:
                                            board_dict = = {
                                                1: {1: "X", 
                                                    2: 0, 
                                                    3: "O", 
                                                    4: 0, 
                                                    5: "X", 
                                                    6: "O", 
                                                    7: 0, 
                                                    8: 0, 
                                                    9: "X"
                                                },
                                                2: {i: 0 for i in range(1, 10)},
                                                3: {i: 0 for i in range(1, 10)},
                                                4: {i: 0 for i in range(1, 10)},
                                                5: {i: 0 for i in range(1, 10)},
                                                6: {i: 0 for i in range(1, 10)},
                                                7: {i: 0 for i in range(1, 10)},
                                                8: {i: 0 for i in range(1, 10)},
                                                9: {i: 0 for i in range(1, 10)},
                                            }
                insertion_order {List} -- Contains information about the order
                                        the values were inserted by the players.
                                        One insertion contains lists 
                                        [table no, table pos, value] 
                                        (default: {None})
        """
        self.insertions = []
        self.playerA = playerA
        self.playerB = playerB

        # initialize the board with 0 values if no board_dict is given
        if board_dict is None:
            self.state = {i: {j: 0 for j in range(1, 10)} for i in range(1, 10)}
            self.insertion_order = []
            self.finished_tables = {tbl_no: 0 for tbl_no in range(1, 10)}
        else:
            # TODO: add exception for invalid board_dicts
            self.state = board_dict
            self.insertion_order = insertion_order
            self.finished_tables = {tbl_no: 0 for tbl_no in range(1, 10)}
            # update finished_tables
            for tbl_no in range(1, 10):
                if self.player_won_on_table(tbl_no, self.playerA):
                    self.finished_tables[tbl_no] = self.playerA
                    for tbl_pos in range(1, 10):
                        self.state[tbl_no][tbl_pos] = self.playerA
                elif self.player_won_on_table(tbl_no, self.playerB):
                    self.finished_tables[tbl_no] = self.playerB
                    for tbl_pos in range(1, 10):
                        self.state[tbl_no][tbl_pos] = self.playerB

            # modify finished_tables
            # tmp_dic = {tbl_no: }

    @classmethod
    def set_board(cls, playerA: str, playerB: str, board_dict: Dict, insertion_order):
        return cls(
            playerA=playerA,
            playerB=playerB,
            board_dict=board_dict,
            insertion_order=insertion_order,
        )

    def print_board(self):
        """ Print out the current board state
        """
        x = deepcopy(self.state)
        # x[1][1] = '1'
        # x[2][2] = '2'
        # x[3][3] = '3'
        # x[4][4] = '4'
        # x[5][5] = '5'
        # x[6][6] = '6'
        # x[7][7] = '7'
        # x[1][1] = '1'
        # x[8][8] = '8'
        # x[9][9] = '9'
        for i in range(1, 10):
            for j in range(1, 10):
                if x[i][j] == 0:
                    x[i][j] = " "
                else:
                    continue

        # table top
        print("+" + "---+" * 8 + "---+")
        for counter in range(0, 10):
            # table bottom
            if counter == 9:
                print("-" * 37)
            # print 3x3 small tables row-wise
            elif counter in [0, 3, 6]:
                print(
                    (
                        "".join(
                            [
                                "|" + f" {x[j][1]}   {x[j][2]}   {x[j][3]} "
                                for j in range(counter + 1, counter + 4)
                            ]
                            + ["|"]
                        )
                    )
                )
                print("|" + "   +" * 8 + "   |")
                print(
                    (
                        "".join(
                            [
                                "|" + f" {x[j][4]}   {x[j][5]}   {x[j][6]} "
                                for j in range(counter + 1, counter + 4)
                            ]
                            + ["|"]
                        )
                    )
                )
                print("|" + "   +" * 8 + "   |")
                print(
                    (
                        "".join(
                            [
                                "|" + f" {x[j][7]}   {x[j][8]}   {x[j][9]} "
                                for j in range(counter + 1, counter + 4)
                            ]
                            + ["|"]
                        )
                    )
                )
                print("+" + "---+" * 8 + "---+")

    def is_legal_move(self, tbl_no: int, pos_no: int):
        # init condition if board is empty
        if not self.insertion_order:
            return True

        # False when you try to insert in a finished table
        if self.finished_tables[tbl_no] != 0:
            return False

        # True if the tbl_no you shall insert is already finished
        # but the insertion is in general possible
        last_pos = self.insertion_order[-1][1]
        if self.finished_tables[last_pos] != 0:
            if self.state[tbl_no][tbl_pos] == 0:
                return True
            else:
                return False

        # if field is already used
        if self.is_used_field(tbl_no, pos_no):
            return False

        if self.last_field_eq_table(tbl_no):

            # insert in finished tbl
            if self.is_finished_tbl(tbl_no):
                return False
            else:
                return True

        # when the current tbl_no is not equal to the field from last move it migth be
        # a legal move if the required tbl to insert is already finished
        else:
            # must insert in finished tbl
            if self.force_insert_in_finished_table():

                # insert in finished tbl
                if self.is_finished_tbl(tbl_no):
                    return False
                else:
                    return True

            else:
                return False

    def force_insert_in_finished_table(self) -> bool:
        """Returns True if the last move forces user to do the next move into 
            an already used tbl_no.
        """
        next_tbl = self.insertions[-1][1]
        return self.finished_tables[next_tbl] is 1

    def last_field_eq_table(self, tbl_no: int) -> bool:
        return self.insertion_order[-1][1] is tbl_no

    def is_finished_tbl(self, tbl_no: int) -> bool:
        """ Returns True if the table is already fineshed, else False

        Arguments:
            tbl_no {int} -- table number to test

        Returns:
            bool -- Return value if the test table is already finished
        """
        if self.finished_tables[tbl_no] is 1:
            return True
        else:
            return False

    def is_used_field(self, tbl_no: int, tbl_pos: int) -> bool:
        return self.state[tbl_no][tbl_pos] is not 0

    def insert_at_pos(self, tbl_no: int, pos_no: int, val: str):
        if tbl_no not in range(1, 10):
            raise ValueError(f"Table number ({tbl_no}) is out of range or no integer.")
        elif pos_no not in range(1, 10):
            raise ValueError(
                f"Position number ({pos_no}) is out of range or no integer."
            )
        elif not self.is_legal_move(tbl_no, pos_no, val):
            raise ValueError(
                f"Your input ({tbl_no}) violates the condition from the previous move."
            )
        self.state[tbl_no][pos_no] = val
        self.insertion_order.append([tbl_no, pos_no, val])

    def player_won_on_table(self, table_no: int, player: Any) -> bool:
        if table_no not in range(1, 10):
            raise ValueError

        # get current state for selected talble
        tbl_dict: dict = self.state[table_no]
        # get all table positions that were assigned to a players 'X'
        tbl_pos: List = [key for key, value in tbl_dict.items() if value == player]

        # all possible cases to win in a table
        win_chances = [
            [1, 5, 9],
            [3, 5, 7],
            [2, 5, 8],
            [4, 5, 6],
            [1, 2, 3],
            [1, 4, 7],
            [3, 6, 9],
            [7, 8, 9],
        ]
        for chance in win_chances:
            if all(map(lambda pos: tbl_dict[pos] == player, chance)):
                return True
        return False

    def test_legal_move(self, tbl_no: int, tbl_pos: int):
        print(f"Table no.: {tbl_no} \t - Table_pos: {tbl_pos}")
        print(f"Is legale move: {self.is_legal_move(tbl_no, tbl_pos)}")

    def player_won_game(self) -> str:
        pass


if __name__ == "__main__":
    # brd = Board(playerA="X", playerB="Y")
    # brd.print_board()brd.test_legal_move(1, 1)
    # brd.insert_at_pos(6, 1, "X")
    # brd.print_board()
    # brd.insert_at_pos(6, 9, "X")
    # brd.print_board()
    # brd.insert_at_pos(6, 5, "X")
    # brd.print_board()

    board_setting = {
        1: {i: 0 for i in range(1, 10)},
        2: {i: 0 for i in range(1, 10)},
        3: {i: 0 for i in range(1, 10)},
        4: {i: 0 for i in range(1, 10)},
        5: {i: 0 for i in range(1, 10)},
        6: {i: 0 for i in range(1, 10)},
        7: {i: 0 for i in range(1, 10)},
        8: {1: "X", 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: "X"},
        9: {1: "X", 2: 0, 3: 0, 4: 0, 5: "X", 6: 0, 7: 0, 8: 0, 9: "X"},
    }
    brd = Board.set_board(
        playerA="X", playerB="Y", board_dict=board_setting, insertion_order=[[9, 9]]
    )
    brd.print_board()
    for tbl_no in range(1, 10):
        for tbl_pos in range(1, 10):
            brd.test_legal_move(tbl_no, tbl_pos)

    brd.player_won_on_table(9, "X")
