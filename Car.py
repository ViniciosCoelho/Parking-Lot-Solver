class Car:
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
        self.__horizontal = isHorizontal(x1, x2)

    def isHorizontal(self, x1, x2):
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
        
        # Wrong target position given
        if self.__horizontal is not self.isHorizontal(x1, x2):
            exit

    def isSatisfied(self):
        satisfied = False

        if self.__position['firstPos'] is self.__targetPosition['firstPos']
            and self.__position['secondPos'] is self.__targetPosition['secondPos']:
            satisfied = True
        
        return satisfied
    
    def setAssault(self, assault, limitation):
        self.__assaulted = assault
        self.__limitation = limitation

    def isAssaulted(self):
        return self.__assaulted