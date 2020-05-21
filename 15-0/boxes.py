from settings import *

class box:
    def __init__ (self):
        pass

    def location (selected):
        return testBoard4[selected[1]][selected[0]]

    def missed(selected):
        if selected[0]-1 >= 0:
            if testBoard4[selected[1]][(selected[0]-1)] == 0: return ((selected[0]-1), selected[1])
        if selected[0]+1 <= 3:
            if testBoard4[selected[1]][(selected[0]+1)] == 0: return ((selected[0]+1), selected[1])
        if selected[1]-1 >= 0:
            if testBoard4[(selected[1]-1)][selected[0]] == 0: return (selected[0], (selected[1]-1))
        if selected[1]+1 <= 3:
            if testBoard4[(selected[1]+1)][selected[0]] == 0: return (selected[0], (selected[1]+1))

    def replacing(selected, missed):
        global testBoard4
        a = selected[1]
        b = selected[0]
        c = missed[1]
        d = missed[0]
        testBoard4[a][b], testBoard4[c][d] = testBoard4[c][d], testBoard4[a][b]