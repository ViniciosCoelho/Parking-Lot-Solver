from time import sleep
from tkinter import *

class PrintHandler():
    def __init__(self, spaceSize):
        self.__spaceSize = spaceSize
        self.__targetPos = []

        self.__window = Tk()
        self.__window.title('Simple Parking Lot Solver')
        self.__window.geometry('300x150')

        upperFrame = Frame(self.__window).grid()

        self.__squares = [[Button(upperFrame) for y in range (spaceSize)] for x in range(spaceSize)]
        [[self.__squares[x][y].grid(column=y + 2, row=x) for y in range (spaceSize)] for x in range(spaceSize)]

        bottomFrame = Frame(self.__window).grid()

        Button(bottomFrame, bg='red').grid(column = 0, row = 0)
        Button(bottomFrame, bg='green').grid(column = 0, row = 1)
        Button(bottomFrame, bg='blue').grid(column = 0, row = 2)
        Button(bottomFrame, bg='yellow').grid(column = 0, row = 3)

        Label(bottomFrame, text="Car 1 ").grid(column = 1, row = 0)
        Label(bottomFrame, text="Car 2 ").grid(column = 1, row = 1)
        Label(bottomFrame, text="Car 3 ").grid(column = 1, row = 2)
        Label(bottomFrame, text="Target").grid(column = 1, row = 3)

        self.__window.update()

    def print(self, printPositions):
        printableArea = [['0' for y in range(self.__spaceSize)] for x in range(self.__spaceSize)]
        aux = 0

        for x in range(5):
            for y in range(5):
                self.__squares[x][y]['bg'] = 'white'
        
        for target in self.__targetPos:
            x = target['x']
            y = target['y']
            self.__squares[x][y]['bg'] = 'yellow'


        for pos in printPositions:
            x = pos['x']
            y = pos['y']

            if aux < 2:
                printableArea[x][y] = 'X'
                self.__squares[x][y]['bg'] = 'red'

            elif aux < 4:
                printableArea[x][y] = 'Y'
                self.__squares[x][y]['bg'] = 'green'

            elif aux < 6:
                printableArea[x][y] = 'Z'
                self.__squares[x][y]['bg'] = 'blue'
            else:
                aux = 0
                continue

            aux += 1
        
        for x in range(5):
            for y in range(5):
                print(printableArea[x][y] + ' ', end='')
            print()
        print()

        self.__window.update()
        sleep(1)
    
    def setTarget(self, printPosition):
        self.__targetPos.append(printPosition)