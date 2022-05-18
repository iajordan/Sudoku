
class Board:

    def __init__(self):
        board_in = open("sudoku3.txt", "r")
        board_in_copy = open("sudoku3.txt", "r")

        self.size = (len(board_in_copy.readline())-1)
        self.goal = self.size * self.size
        self.numbers = []
        self.count = 0
        self.board = [[0 for x in range(self.size)] for y in range(self.size)]
        
        self.rows = {}
        self.cols = {}
        self.quad = {}

        self.diff = []

        y =0
        for line in board_in:
            x = 0
            for i in line:
                if i != "0" and i != '\n':
                    self.count += 1
                if x < self.size:
                    # print(i)
                    self.board[x][y] = int(i)
                x += 1
            y += 1
        self.all_numbers()
        self.make_dicts()
        self.quadrants()

        

    def all_numbers(self):
        for i in range(self.size):
            self.numbers.append(i+1)
    
    def make_dicts(self):
        for i in range(self.size):
            self.rows[i] = []
            self.cols[i] = []
            self.quad[i] = []


    def quadrants(self):
        self.quad[0] = [self.board[0][:3], self.board[1][:3], self.board[2][:3]]
        self.quad[1] = [self.board[3][:3], self.board[4][:3], self.board[5][:3]] 
        self.quad[2] = [self.board[6][:3], self.board[7][:3], self.board[8][:3]]

        self.quad[3] = [self.board[0][3:6], self.board[1][3:6], self.board[2][3:6]]
        self.quad[4] = [self.board[3][3:6], self.board[4][3:6], self.board[5][3:6]] 
        self.quad[5] = [self.board[6][3:6], self.board[7][3:6], self.board[8][3:6]]

        self.quad[6] = [self.board[0][6:], self.board[1][6:], self.board[2][6:]]
        self.quad[7] = [self.board[3][6:], self.board[4][6:], self.board[5][6:]] 
        self.quad[8] = [self.board[6][6:], self.board[7][6:], self.board[8][6:]]

        for i in self.quad:
            # print(self.quad[i])
            self.quad[i] = list(set(self.quad[i][0] + self.quad[i][1] + self.quad[i][2]))
            self.quad[i].remove(0)

    def print_board(self):
        string = ""
        for y in range(self.size ):
            row = ""
            for x in range(self.size ):
                if self.board[x][y] == 0:
                    row += "*"
                else:
                    row +=  str(self.board[x][y])
            string +=row
            # print("ROW", y + 1, ":" ,row)
        return string

    def update(self):
        for y in range(self.size ):
            for x in range(self.size ):
                # print("test", self.board[x][y])
                if (self.board[x][y] not in self.rows[y]) and (self.board[x][y]!= 0):
                    self.rows[y].append(self.board[x][y])
                if (self.board[x][y] not in self.cols[x]) and (self.board[x][y]!= 0):
                    self.cols[x].append(self.board[x][y])

    def clean_up(self):
        for y in range(self.size ):
            for x in range(self.size ):
                if self.board[x][y] == 0:
                    q_num = switch(x,y)
                    # print("\nQUAD", x + 1 , ",", y + 1)
                    merged = list(set(self.rows[y] + self.cols[x]+ self.quad[q_num] ))
                    # merged = list(set(merged + self.quad[q_num]))
                    self.diff = Diff(self.numbers, merged)
                    
                    # print("DIFF", self.diff, "LENGTH", len(self.diff))
                    if (len(self.diff) == 1) and (self.board[x][y] == 0 ):
                        # print("DIFF", self.diff, "LENGTH", len(self.diff))
                        self.board[x][y] = self.diff[0]
                        self.rows[y].append(self.diff[0])
                        self.cols[x].append(self.diff[0])
                        self.quad[q_num].append(self.diff[0])
                        self.count += 1
                

    def check_diff(self):
        if len(self.diff < 1):
            return False
        else:
            return True

    def get_diff(self):
        return self.diff
    
    def get_count(self):
        return self.count

def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))

def switch(x, y):
        if x < 3 and y < 3:
            return 0
        elif (x >= 3 and x < 6) and y < 3:
            return 1
        elif x >= 6 and y < 3:
            return 2
        elif x < 3 and (y >= 3 and y < 6):
            return 3
        elif (x >= 3 and x < 6) and (y >= 3 and y < 6):
            return 4
        elif x >= 6 and (y >= 3 and y < 6):
            return 5
        elif x < 3 and y >=6:
            return 6
        elif (x >= 3 and x < 6) and y >= 6:
            return 7
        else:
            return 8

B = Board()
# B.print_board()
B.update()
# print()
# print(B.rows)
# print(B.cols)
# print(B.quad)

# B.clean_up()
# B.print_board()

it = 0

while(B.count != B.goal):
    B.clean_up()
    # print()
    # B.print_board()
    it += 1
result = B.print_board()
# print(it)
print(result)


