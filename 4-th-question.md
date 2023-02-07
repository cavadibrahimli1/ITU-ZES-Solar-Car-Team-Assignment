# Question 4
![Logo](https://miro.medium.com/max/560/1*fDUoSfIWyLKVBH9TMcgvcw.png)

## Space Agency Simulation 



In this homework, you are going to implement a fictional space agency simulation. You will simulate a space agency that operates space missions. Each mission has an operating cost. The agency covers these costs by selling tickets to the passengers. Every mission has a probability to fail at launch, however, these failures are non-fatal incidents. The agency only reschedules failed missions to a further date. However, the agency has to pay the operation cost of the mission.
For any issues regarding the assignment, please contact Ozan C ̧ etin from
the Whatsapp group or via e-mail (ozanc1091@gmail.com).

4.1 [IMPORTANT] Implementation Notes
Following implementation details are included in grading:
1. You’re allowed to solve this problem using Python or C++.
2. Instructions and explanation below are made based on C++ Standart
Library. This should not confuse you. You can also implement this
problem using Python.



## 4.2 Implementation Details

You are expected to implement five classes; Person, Passenger, Astronaut, Mission, and Agency. You have to implement the given attributes and methods below. However, to achieve a list/array functionality you can add attributes or methods to the classes.

## 4.2.1 Person
- Private Attributes:
    
    Person has a name (e.g. Neil) and a surname (e.g. Armstrong).
Methods:
    
    • Constructor(s): the constructor should optionally take the attributes.
## 4.2.2 Passenger

Passenger class is a subclass of the Person class.
- Private Attributes:
    Passengers have cash (eg. 1250), and ticket (a boolean that shows whether a passenger has a ticket).
Methods:
    
    • Constructor(s): the constructor should optionally take the attributes. Note that cash can’t be negative. If it’s given negative then cash should be set as zero and an error message should be shown. Error message will be the following: ”Passenger cash can’t be negative. It is set to 0.”

    • buyTicket:when this method is invoked, it buys a ticket if the Passenger has enough cash to pay the ticket price. This method should take a ticket price (int) and return whether the person bought the ticket or not as a boolean.

## 4.2.3 Astronaut
Astronaut class is a subclass of the Person class.
- Private Attributes:
    Astronauts have numMissions (eg. 4) counter which shows number of successful flights that an astronaut completed.
Methods:
    
    • Constructor(s): the constructor should optionally take the attributes.
    
    • completeMission: when this method invoked, it will increment the numMissions attribute of the Astronaut by one

## 4.2.4 Mission
- Private Attributes:
    Missions have name (eg. ST-21), missionNumber (eg. 2), cost (eg.3500), faultProbability (eg. 20), completed (eg. true), passengers list/array and crew list/array. Missions also have a static numMissions variable which keeps total number of created missions

    • Mission name has a special naming convention. Each mission has an ”XX-YY” name where X is an uppercase letter and Y is a digit. If themission name does not satisfy this condition, an error message shouldbe printed and the default name (”AA-00”) should be set as mission name. You can use string::substr and string::find functions to parse the string.
    • faultProbability should be an integer between 0-100 which represents the failure probability of the mission. If 100 is given, then the mission fails at every launch.
    • completed should be a boolean that indicates the mission success. All successful missions are considered as completed, rescheduled and not executed missions are considered as not completed.

    • passengers list/array should keep passengers that added to the mission.

    • crew list/array should keep crew members that assigned to the Mission

    • numMission must be initialized once and it must be initialized to 0. This static variable should be increased by 1 at each mission object creation. After increasing the variable result should be assigned to missionNumber variable. For example first mission should increase the static variable from 0 to 1 and assign the 1 to itself.

Methods:

    • Constructor(s): the constructor should optionally take the attributes

    • addSpaceShipStaff: This method for adding a Passenger or an Astronaut to the mission passenger or crew list/array respectively. Passengers can be added only if they have a ticket. If they don’t have a ticket, error message should be shown. Astronauts are directly added to the crew list/array.

    • executeMission: this method invokes a random number generator (std::rand) and if the number is bigger than fault probability then mission will be successful. It will print whether mission is successful or not. If mission is successful it will invoke completeMission method of each astronaut in the crew list/array. Then it will print each astronaut name with number of completed missions. In order to see the behaviour of the method, please check out the provided output. Finally, it will set the completed attribute according to the result of the mission and return the result as a boolean.

    • calculateProfit: this method gets a ticket price as an argument. It checks whether the mission is completed by checking the class attribute completed. If the mission is successful, then the function multiplies the ticket price with the number of passengers on board. Cost of the mission will be subtracted from the profit whether mission is successful or not. After that the method returns net profit which can be a positive or negative integer value

## 4.2.5 Agency
- Private Attributes:

    Agency has a name (eg. NASA), cash (eg. 25000), ticketPrice (eg. 1200). completedMissions list/array and nextMissions list/array.

Methods:

    • Constructor(s): the constructor should optionally take the attribute.
    
    • addMission: this method takes a mission as an argument and adds the mission to the agency’s nextMissions list/array.
    
    • executeNextMission: this method takes the next mission from the nextMissions list/array and executes the mission. If the mission is successful, it should be added to completedMissions list/array and the profit of the mission should be added to the agency cash. Otherwise, the mission should be moved to the end of the nextMissions list/array. Failed mission profit also should be added to the agency cash.
    
    • agencyInfo: Using this methods, you should put information about the Agency to the out stream. It should contain name, current cash, ticket price, information (name, cost) of the nextMissions and com- pletedMissions. For every mission you should print mission number, mission name and mission cost.




