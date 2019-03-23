from Car import Car
from PrintHandler import PrintHandler

class WorkflowController():
    def __init__(self, spaceSize):
        self.__cars = []
        self.__spaceSize = spaceSize
        self.__printHandler = PrintHandler(spaceSize)

    def initialize(self):
        '''
        Assuming here that the first position is the left one
        or the above one depending on the orientation.
        '''
        car = Car(2, 0, 2, 1)
        car.setTargetPos(2, 3, 2, 4)
        self.__cars.append(car)

        self.__printHandler.setTarget(car.getTargetPos()['firstPos'])
        self.__printHandler.setTarget(car.getTargetPos()['secondPos'])

        car = Car(1, 2, 2, 2)
        self.__cars.append(car)

        car = Car(0, 2, 0, 3)
        self.__cars.append(car)
    
    def start(self):
        print('Beginning...\n')
        self.printMoves()

        while self.problemSolved() is False:
            self.processStep()
    
    def problemSolved(self):
        solved = True

        for car in self.__cars:
            solved = car.isSatisfied()

            if solved is False:
                break
        
        return solved
    
    def processStep(self):
        for car in self.__cars:
            assaulted = car.isAssaulted()

            if assaulted is True:
                self.processAssault(car)
            
            elif car.isSatisfied() is True:
                continue

            else:
                self.processSatisfy(car)    
    
    def processAssault(self, car):
        horizontal = car.isHorizontal()
        xStep = 0
        yStep = 0

        pos = car.getPosition()
        x1 = pos['firstPos']['x']
        y1 = pos['firstPos']['y']
        x2 = pos['secondPos']['x']
        y2 = pos['secondPos']['y']
        limitation = car.getLimitation()

        if horizontal is True:
            yStep += 1

            if y2 is limitation['y']:
                yStep *= -1
            
            if y2 + yStep >= self.__spaceSize or y1 + yStep < 0:
                yStep *= -1
        else:
            xStep += 1

            if x2 is limitation['x']:
                xStep *= -1

            if x2 + xStep >= self.__spaceSize or x1 + xStep < 0:
                xStep *= -1

        blockedPositions = self.findBlockedPositions(car)

        if self.stepEnabled(pos, blockedPositions, xStep, yStep):
            pos['firstPos']['x'] += xStep
            pos['firstPos']['y'] += yStep
            pos['secondPos']['x'] += xStep
            pos['secondPos']['y'] += yStep

            self.printMoves()
        else:
            limitations = {
                'firstPos': {
                    'x': pos['firstPos']['x'] + xStep,
                    'y': pos['firstPos']['y'] + yStep
                },
                'secondPos': {
                    'x': pos['secondPos']['x'] + xStep,
                    'y': pos['secondPos']['y'] + yStep
                }
            }

            self.createAssault(car, limitations)

    def findBlockedPositions(self, car):
        blockedPositions = []

        for elem in self.__cars:
            if car is not elem:
                pos = elem.getPosition()
                blockedPositions.append(pos['firstPos'])
                blockedPositions.append(pos['secondPos'])
        
        return blockedPositions

    def stepEnabled(self, pos, blockedPositions, xStep, yStep):
        enabled = True

        x1 = pos['firstPos']['x']
        y1 = pos['firstPos']['y']
        x2 = pos['secondPos']['x']
        y2 = pos['secondPos']['y']

        for elem in blockedPositions:
            xBlocked = elem['x']
            yBlocked = elem['y']

            if x1 + xStep is xBlocked and y1 + yStep is yBlocked or x2 + xStep is xBlocked and y2 + yStep is yBlocked:
                enabled = False
        
        return enabled
    
    def createAssault(self, car, limitations):
        limitation1 = limitations['firstPos']
        limitation2 = limitations['secondPos']

        for elem in self.__cars:
            if car is elem:
                continue

            positions = elem.getPosition()

            for pos in positions.values():
                if pos['x'] is limitation1['x'] and pos['y'] is limitation1['y']:
                    elem.setAssault(limitation1)
                    return

                elif pos['x'] is limitation2['x'] and pos['y'] is limitation2['y']:
                    elem.setAssault(limitation2)
                    return

    def processSatisfy(self, car):
        horizontal = car.isHorizontal()
        xStep = 0
        yStep = 0

        pos = car.getPosition()
        x1 = pos['firstPos']['x']
        y1 = pos['firstPos']['y']
        x2 = pos['secondPos']['x']
        y2 = pos['secondPos']['y']
        targetPos = car.getTargetPos()

        if horizontal is True:
            yStep += 1
            
            if abs(y1 + yStep - targetPos['firstPos']['y']) > abs(y1 - targetPos['firstPos']['y']):
                yStep *= -1
        else:
            xStep += 1

            if abs(x1 + xStep - targetPos['firstPos']['x']) > abs(x1 - targetPos['firstPos']['x']):
                xStep *= -1

        stepBlocked = False
        blockedPositions = self.findBlockedPositions(car)

        while stepBlocked is not True:
            if self.stepEnabled(pos, blockedPositions, xStep, yStep):
                pos['firstPos']['x'] += xStep
                pos['firstPos']['y'] += yStep
                pos['secondPos']['x'] += xStep
                pos['secondPos']['y'] += yStep

                if car.isSatisfied():
                    stepBlocked = True
                
                self.printMoves()
            else:
                limitations = {
                    'firstPos': {
                        'x': pos['firstPos']['x'] + xStep,
                        'y': pos['firstPos']['y'] + yStep
                    },
                    'secondPos': {
                        'x': pos['secondPos']['x'] + xStep,
                        'y': pos['secondPos']['y'] + yStep
                    }
                }

                self.createAssault(car, limitations)
                stepBlocked = True

    def printMoves(self):
        printPositions = self.findPrintPositions()
        self.__printHandler.print(printPositions)

    def findPrintPositions(self):
        positions = []

        for elem in self.__cars:
            pos = elem.getPosition()
            positions.append(pos['firstPos'])
            positions.append(pos['secondPos'])

        return positions