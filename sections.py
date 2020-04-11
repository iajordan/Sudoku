import pandas as pd

class Sec:
    def __init__(self):
        self.total = []
    def s_in (self, num):
        self.total.append(num)
    def print(self):
        print(self.total)

class Board:
    def __init__(self):
        self.sec = []

    def insert(self, num):
        count = 1
        flag = True
        count_rows = 1
        rows_flag = True

        for i in range(len(num)):
            if flag and rows_flag:
                new_sec = Sec()
                self.sec.append(new_sec)
                flag = False
                rows_flag = False
                print(count)
                print(count_rows)

            self.sec[count-1].s_in(num[i])

            if ((i+1) % 3  == 0):
                count +=1
                flag = True
                if count > 3:
                    count = 1

            if count == 3:
                count_rows += 1
                if count_rows % 3  == 0:
                    rows_flag = True
    def print(self):
        for i in self.sec:
            i.print()



# class Board:
#     def __init__(self):
#         self.board = []
#
#     def insert(self, num):
#         sec = [Sec()] * 3
#         count = 0
#         for i in range(len(num)):
#             self.board.append(num[i])
#             if ((i) %  == 0):
#                 count +=1
#
#             sec[count-1].s_in(num[i-1])
#         for i in sec:
#             i.print()
#
#     def print(self):
#         print("|".join(self.board))
#
#     def sec(self):
#         for i in range(len(self.board)):
#             print(i+1)


def main():
    numbers = []
    f = open("board.txt", "r")
    num = str(f.readline(2))
    while num != "":
        numbers.append(num)
        num = str(f.readline(2))
    f.close()
    b = Board()
    b.insert(numbers)
    b.print()



if __name__ == '__main__':
    main()
