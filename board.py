from typing import Any, Dict, List


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
positions-->| 4   5   6 |   table2  |    table3 |
            |   +   +   +   +   +   +   +   +   |
            | 7   8   9 |           |           |
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

            Every board is built on a given state dictionary or
            will be initialized with zero values and the player will be
            filling the board respecting the gaming rules.

    Raises:
    
    Returns:
        Board -- Ultimate Tic-Tac-Toe Bord instance that represents 
                 the current state
    """

    def __init__(self, board_dict: Dict = None, insertion_order_ls: List = None):
        """Create a Board object by a given board_dict or initial 
            with  zeros
        
        Keyword Arguments:
            board_dict {Dict} -- Dict which represents a Board with keys 
                                 representing the table numbers (1 to 9)
                                 and values as Dicts representing the 
                                 positions and their value (default: {None})
                                 Example:
                                    board_dict = = {
                                        1: {1: "X", 
                                            2: 0, 
                                            3: 0, 
                                            4: 0, 
                                            5: "X", 
                                            6: 0, 
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
            insertion_order_ls {List} -- Contains information about the order
                                         the values were inserted by the players.
                                         One insertion contains lists 
                                            [table no, table pos, value] 
                                         (default: {None})
        """
        self.insertions = []

        # initialize the board with 0 values if no board_dict is given
        if board_dict is None:
            self.state = {i: {j: 0 for j in range(1, 10)} for i in range(1, 10)}
        else:
            # TODO: add exception for invalid board_dicts
            self.state = board_dict

        if insertion_order_ls is None:
            # TODO: add exception for invalid order actions
            self.insertion_order = []
        else:
            self.insertion_order = insertion_order_ls

    @classmethod
    def set_board(cls, board_dict: Dict):
        return cls(board_dict=board_dict)

    def print_board(self):
        x = self.state
        # x[1][1] = '1'
        # x[2][2] = '2'
        # x[3][3] = '3'
        # x[4][4] = '4'
        # x[5][5] = '5'
        # x[6][6] = '6'
        # x[7][7] = '7'
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

    def is_legal_move(self, tbl_no: int, pos_no: int, val: str):
        # board is already filled
        if self.insertion_order:
            # table number is equal to last move position number
            if self.insertion_order[-1][1] == tbl_no:
                return True
            else:
                return False
        # board is empty
        else:
            return True

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


if __name__ == "__main__":
    brd = Board()
    # brd.print_board()
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
        8: {i: 0 for i in range(1, 10)},
        9: {1: "X", 2: 0, 3: 0, 4: 0, 5: "X", 6: 0, 7: 0, 8: 0, 9: "X"},
    }
    brd = Board.set_board(board_setting)
    brd.print_board()
    brd.player_won_on_table(9, "X")
