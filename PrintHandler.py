from time import sleep

class PrintHandler():
    def __init__(self, spaceSize):
        self.__spaceSize = spaceSize

    def print(self, printPositions):
        printableArea = [['0' for y in range(self.__spaceSize)] for x in range(self.__spaceSize)]

        aux = 1

        for pos in printPositions:
            printableArea[pos['x']][pos['y']] = 'X'
            aux += 1
        
        for x in range(5):
            for y in range(5):
                print(printableArea[x][y] + ' ', end='')
            print()
        print()

        sleep(1)