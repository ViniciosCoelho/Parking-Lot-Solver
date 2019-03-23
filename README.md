# Parking-Lot-Solver

This is a basic parking lot game solver based on "ECO-Resolution" concept. This is just a prototype, so limitations can be found.

New cars can be set inside "initialize" function. Remeber to always set them like the following example:

Y Y -> Car 1 (Vertical)
X X -> Car 2 (Horizontal)

      0 0 Y 0 0
      0 0 Y 0 0
      0 0 0 X X
      0 0 0 0 0
      0 0 0 0 0

Within the "initialize" function, define them as follows:
      car1 = Car(0, 2, 1, 2) # x1, y1, x2, y2. Vertical cars, top position always first.
      car1.setTargetPos(3, 2, 4, 2) # To set a target position for this kind of car, follow the same rules as the line above.
      self.__cars.append(ca1)

      car2 = Car(2, 3, 2, 4) # x1, y1, x2, y2. Horizontal cars, left position always first.
      car2.setTargetPos(2, 0, 2, 1) # To set a target position for this kind of car, follow the same rules as the line above.
      self.__cars.append(car2)

      car3 = Car(3, 0, 3, 4) # If target is not set, then this car is already satisfied.
      self.__cars.append(car2)