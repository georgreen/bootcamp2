#simple simulation of ppl walking
#applies enscapulation i.e using classes to supress and manage details
#of each classes
class Location(object):
    def __init__(self, x, y):
        '''input  x and y are numbers'''
        self.x = x
        self.y = y

    def move(self, x, y):
        return Location(self.x + x, self.y + y)

    def distFrom(self, other):
        ox = other.x
        oy = other.y

        diffx = self.x - ox
        diffy = self.y - oy

        return (diffx **2 + diffy **2) **0.5


class Field(object):
    def __init__(self):
        self.person = {}

    def addPeopleToField(self, person, loc):
        self.person[person] = loc

    def removePeople(self, person):
        del self.person[person]

    def getLocationOfPerson(self, person):
        return self.person[person]

    def updateLocation(self, person):
        x, y = person.move()
        current_loc = self.person[person]
        self.person[person] = current_loc.move(x, y)


#Simulate two individual druk and one not so drunk
#appplies inheritance from Person

class Person(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Name: %s',(self.name)


import random

class NormalPerson(Person):
    def move(self):
        '''
        moves very stable i.e forward or backwards
        '''
        steps = [(0.0, 0.0),(0.0, 1.0), (1.0, 0.0), (0.0, 0.0)]
        return random.choice(steps)

class DrunkPerson(Person):
    def move(self):
        '''
        moves randomly i.e right or left or forward or backwards
        '''
        steps = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(steps)

#simulate walking
#applies Polymorphism i.e walk applies to poth DrunkPerson and NormalPerson
def walk(field, person, numsteps):
    '''
    simulates walking
    '''
    startPostion = field.getLocationOfPerson(person)
    for step in range(0, numsteps):
        field.updateLocation(person)
    return startPostion.distFrom(field.getLocationOfPerson(person))

def simulateWalking(trials, numberSteps, person):
    '''
    uses walk to give illusion of movement
    input:
    trial -> int number of trials
    numberSteps -> int stop after this steps
    person -> the person being tested how far thy can walk
    output:
    A list containing the distance walked per trial
    '''
    origin = Location(0, 0)
    distances_covered = []
    for trial in range(0, trials):
        f = Field()
        f.addPeopleToField(person, origin)
        distances_covered.append(walk(f, person, numberSteps))
    return distances_covered


normal_guy = NormalPerson("Morty")
drunk_guy = DrunkPerson("Rick")

distance_by_normal = simulateWalking(100, 300, normal_guy)
distance_by_drunk = simulateWalking(100, 300, drunk_guy)

#Display results

import pylab


pylab.plot(distance_by_normal, label = 'Normal Person')
pylab.plot(distance_by_drunk, label = "Drunk person")
pylab.title("Distance comparison Between Drunk and Normal person")
pylab.xlabel('steps takken')
pylab.ylabel('Steps from Origin')
pylab.show()
