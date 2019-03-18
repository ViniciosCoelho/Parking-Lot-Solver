class Car():
    def __init__(self, x1, y1, x2, y2):
        self.__position = {
            'firstPos': {
                'x': x1,
                'y': y1
            },
            'secondPos': {
                'x': x2,
                'y': y2
            }
        }

        self.__targetPosition = None
        self.__assaulted = False
        self.__limitation = None
        self.__horizontal = self.defineOrientation(x1, x2)

    def defineOrientation(self, x1, x2):
        horizontal = None

        if x1 is x2:
            horizontal = True
        else:
            horizontal = False

        return horizontal
    
    def setTargetPos(self, x1, y1, x2, y2):
        self.__targetPosition = {
            'firstPos': {
                'x': x1,
                'y': y1
            },
            'secondPos': {
                'x': x2,
                'y': y2
            }
        }

        x1Pos = self.__position['firstPos']['x']
        y1Pos = self.__position['firstPos']['y']
        x2Pos = self.__position['secondPos']['x']
        y2Pos = self.__position['secondPos']['y']
        
        # Wrong target position given
        if x1Pos is x1 and x2Pos is x2 or y1Pos is y1 and y2 is y2:
            print('Target position well placed.')
        else:
            print('Bad target position.')
            exit()

    def getTargetPos(self):
        return self.__targetPosition

    def isSatisfied(self):
        satisfied = False

        x1 = self.__position['firstPos']['x']
        y1 = self.__position['firstPos']['y']
        x2 = self.__position['secondPos']['x']
        y2 = self.__position['secondPos']['y']

        x1Target = self.__targetPosition['firstPos']['x']
        y1Target = self.__targetPosition['firstPos']['y']
        x2Target = self.__targetPosition['secondPos']['x']
        y2Target = self.__targetPosition['secondPos']['y']

        if x1 is x1Target and x2 is x2Target and y1 is y1Target and y2 is y2Target:
            satisfied = True
        
        return satisfied
    
    def setAssault(self, assault, limitation):
        self.__assaulted = assault
        if self.__limitation is None:
            self.__limitation = limitation

    def isAssaulted(self):
        return self.__assaulted

    def getPosition(self):
        return self.__position

    def isHorizontal(self):
        return self.__horizontal
    
    def getLimitation(self):
        return self.__limitation