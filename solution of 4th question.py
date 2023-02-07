class Person:
    def __init__(self, name=None, surname=None):
        self.__name = name
        self.__surname = surname

    def set_name(self, name):
        self.__name = name

    def set_surname(self, surname):
        self.__surname = surname

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

class Passenger(Person):
    def __init__(self, cash=0, ticket=False, name=None, surname=None):
        super().__init__(name, surname)
        if cash < 0:
            print("Passenger cash can't be negative. It is set to 0.")
            cash = 0
        self.__cash = cash
        self.__ticket = ticket

    def buyTicket(self, price):
        if self.__cash >= price:
            self.__ticket = True
            self.__cash -= price
            return True
        else:
            return False

class Astronaut(Person):
    def __init__(self, numMissions=0, name=None, surname=None):
        super().__init__(name, surname)
        self.__numMissions = numMissions

    def completeMission(self):
        self.__numMissions += 1
    def get_numMissions(self):
        return self.__numMissions

import random
class Mission:
    numMissions = 0
    def __init__(self, name=None, cost=0, faultProbability=0, completed=False):
        self.__name = name
        self.__missionNumber = 0
        self.__cost = cost
        self.__faultProbability = faultProbability
        self.__completed = completed
        self.__passengers = []
        self.__crew = []
        Mission.numMissions += 1
        self.__missionNumber = Mission.numMissions
        self.__validate_name()
    
    def __validate_name(self):
        if not (self.__name and (self.__name[2] == '-' and self.__name[0].isalpha() and self.__name[1].isalpha() and self.__name[3].isdigit())):
            print("Invalid Mission name, default name (AA-00) is set.")
            self.__name = "AA-00"

    def addSpaceShipStaff(self, staff):
        if isinstance(staff, Passenger):
            if staff.ticket:
                self.__passengers.append(staff)
            else:
                print("Passenger doesn't have a ticket, can't add to the mission.")
        elif isinstance(staff, Astronaut):
            self.__crew.append(staff)
    
    def executeMission(self):
        rand_num = random.randint(0, 100)
        if rand_num > self.__faultProbability:
            print("Mission Successful")
            self.__completed = True
            for astronaut in self.__crew:
                astronaut.completeMission()
                print(f'Astronaut {astronaut.get_name()} {astronaut.get_surname()} has completed {astronaut.get_numMissions()} missions.')
        else:
            print("Mission Failed")
            self.__completed = False
        return self.__completed
    
    def calculateProfit(self, ticket_price):
        profit = 0
        if self.__completed:
            profit = (len(self.__passengers) * ticket_price) - self.__cost
        else:
            profit = -self.__cost
        return profit

class Agency:
    def __init__(self, name=None, cash=0, ticketPrice=0):
        self.__name = name
        self.__cash = cash
        self.__ticketPrice = ticketPrice
        self.__completedMissions = []
        self.__nextMissions = []
    
    def addMission(self, mission):
        self.__nextMissions.append(mission)

    def executeNextMission(self):
        if self.__nextMissions:
            current_mission = self.__nextMissions.pop(0)
            result = current_mission.executeMission()
            if result:
                self.__completedMissions.append(current_mission)
                self.__cash += current_mission.calculateProfit(self.__ticketPrice)
            else:
                self.__nextMissions.append(current_mission)
                self.__cash += current_mission.calculateProfit(self.__ticketPrice)
        else:
            print("No more missions to execute.")
    
    def agencyInfo(self):
        print(f'Agency Name: {self.__name}')
        print(f'Current Cash: {self.__cash}')
        print(f'Ticket Price: {self.__ticketPrice}')
        print("Next Missions:")
        for mission in self.__nextMissions:
            print(f'Mission Number: {mission.__missionNumber} Mission Name: {mission.__name} Mission Cost: {mission.__cost}')
        print("Completed Missions:")
        for mission in self.__completedMissions:
            print(f'Mission Number: {mission.__missionNumber} Mission Name: {mission.__name} Mission Cost: {mission.__cost}')


