from Car import Car

class WorkflowController:
    def __init__(self):
        self.__cars = []
    
    def initialize(self):
        car1 = Car(0, 0, 0, 1)
        car1.setTargetPos(0, 0, 0, 1)
        self.__cars.append(car1)
    
    def start(self):
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
            assaulted = car.isAssalted()

            if assaulted is True:
                return
            
            if 