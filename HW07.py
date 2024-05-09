## NOTES:

# CS 2316 - Spring 2024 - HW07 OOP and Comprehensions
# HW07: This homework is due by Wednesday, March 27th @ 11:59PM.

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype if a return is required
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW07.py - Your submission should be named exactly HW07.py
#   - Print your variables as you code in order to see what values they have


class Ride:

    def __init__(self, name, category, popularity, operational = True):
        self.name=name 
        self.category=category
        self.popularity=popularity
        if(operational):
            self.operational="operational"
        else: 
            self.operational="non-operational"

        """
        Question 1.1
            Complete the __init__ method for the Ride class. Attributes are as follows:
            name (str)              It is passed as a parameter (name). Represents the ride name
            category (str)          It is passed as a parameter (category). Represents the ride type
            popularity (int)        It is passed as a parameter (popularity). Represents how popular the ride is
            
            operational (str)       Derived Attribute - Derived from a parameter (operational) - 
                                    "operational" if True, otherwise "non-operational" if False

            Example:
                >>> ride1 = Ride('Falcon's Fury', 'Drop Tower', 100, False)
                >>> print(ride1.name, ride1.category)
                ['Falcon's Fury', 'Drop Tower']

                >>> ride2 = Ride('Kali River Rapids', 'Whitewater Rafting', 49)
                >>> print(ride2.popularity, ride2.operational)
                [49, "operational"]
        """
        

    def __repr__(self):
        return f"{self.name} - a {self.category} ride that is currently {self.operational}."
        """
        Question 1.2
            Complete the __repr__ method. Calling or printing a Ride object
            should be represented as the following string:

            '{name} - a {category} ride that is currently {operational}.'

            THIS SHOULD BE DONE IN ONE LINE

            Example:
                >>> ride1 = Ride('Falcon's Fury', 'Drop Tower', 100, False)
                >>> print(ride1)
                Falcon's Fury - a Drop Tower ride that is currently non-operational.

                >>> ride2 = Ride('Kali River Rapids', 'Whitewater Rafting', 49)
                >>> print(ride2)
                Kali River Rapids - a Whitewater Rafting ride that is currently operational.
        """
        

    def __lt__(self, other):
        return self.popularity<other.popularity
        """
        Question 1.3
            Complete the __lt__ method. An Ride object is less than another if it has a lower popularity score.

            THIS SHOULD BE DONE IN ONE LINE

            Example:
                >>> ride1 = Ride('Falcon's Fury', 'Drop Tower', 100, False)
                >>> ride2 = Ride('Kali River Rapids', 'Whitewater Rafting', 49)

                >>> ride1 < ride2
                False

                >>> ride2 < ride1
                True
        """
        

    def broken_rides(self, isBroken):
        # if(isBroken):
        #     self.operational="non-operational"
        # elif(isBroken==False):
        #     self.operational="operational"

        # self.operational="non-operational" if isBroken else self.operational="operational"

        self.operational="non-operational" if isBroken else "operational"
        """
        Question 2
            Some rides break over time. Complete the broken_rides method to update
            a ride's operational status, given a boolean whether the ride is currently
            broken.
            If a ride is newly broken, change the status to "non-operational".
            If the ride is not broken, the status should be "operational".

            You should have no returns on this function.

            THIS SHOULD BE DONE IN ONE LINE

            Example:
                >>> ride2 = Ride('Kali River Rapids', 'Whitewater Rafting', 49)
                >>> ride3 = Ride('Skull Mountain', 'Roller Coaster', 78, False)

                >>> ride2.broken_rides(True)
                >>> ride3.broken_rides(False)

                >>> print(ride2.operational)
                'non-operational'
                >>> print(ride3.operational)
                'operational'
        """
        

    def popularity_change(self, percent_change):
        # print(percent_change)
        self.popularity=round(self.popularity+(self.popularity*(percent_change/100)),2)
        """
        Question 3
            Rides' popularities change over time. Given the parameter percent_change (a float), change the popularity
            by that percentage and round to 2 decimal places (ex: if popularity was 25, and percent_change is 5%, new popularity is 26.25).

            You should have no returns on this function.

            THIS SHOULD BE DONE IN ONE LINE

            Example:
                >>> ride4 = Ride('Expedition Everest', 'Roller Coaster', 66)
                >>> ride4.popularity_change(10)

                >>> print(ride4.popularity)
                72.6
        """
        

class AmusementPark:

    def __init__(self, name, opening_date, acres, state, is_open = False):
        self.name= name 
        self.opening_date=opening_date
        self.acres=acres
        self.state=state
        self.is_open=is_open
        self.rides=[]
        self.num_rides=len(self.rides)
        """
        Question 4.1
            Complete the __init__ method for the AmusementPark class. Attributes are as follows:
            name (str):             It is passed as a parameter (name). Represents the park's name.
                                    E.g. 'Disney’s Animal Kingdom'
            opening_date (str):     It is passed as a parameter (opening_date). Represents the park's opening date.
                                    E.g. 'April 22, 1998'
            acres (int):            It is passed in as paramater (acres). It is an int representing the size in acres.
                                    E.g. 580
            state (str):            It is passed in as paramater (state). Represents the state the park is in.
                                    E.g. 'Florida'
            is_open (bool)          It CAN be passed in as a parameter (is_open). This is an optional parameter that represents 
                                    if a park is a open or not
                                    E.g. False
            rides (list)            It is not passed in as a parameter. This is an empty list that represents all the rides found in
                                    the amusement park

            num_rides (int)         Derived Attribute - number of rides in the AmusementPark rides list

            Examples:
                >>> park1 = AmusementPark('Disney’s Animal Kingdom', 'April 22, 1998', 580, 'Florida', True)
                >>> print(park1.name, park1.acres, park1.is_open)
                ('Disney’s Animal Kingdom', 580, True)

                >>> park2 = AmusementPark('Six Flags Great Adventure', 'July 1, 1974', 510, 'New Jersey')
                >>> print(park2.name, park2.acres, park2.is_open)
                ('Six Flags Great Adventure', 4.78, False)
        """
        

    def __eq__(self, other):
        return (self.name==other.name) & (self.state==other.state)
        """
        Question 4.2
            Complete the __eq__ method. Two AmusementPark objects are equal if and only
            they have the same name and state.

            THIS SHOULD BE DONE IN ONE LINE

            Example:
                >>> park1 = AmusementPark('Disney’s Animal Kingdom', 'April 22, 1998', 580, 'Florida', True)
                >>> park2 = AmusementPark('Six Flags Great Adventure', 'July 1, 1974', 510, 'New Jersey')
                >>> park3 = AmusementPark('Busch Gardens', 'May 16, 1975', 422. 'Virginia')
                >>> park4 = AmusementPark('Disney’s Animal Kingdom', 'April 22, 1998', 580, 'Florida')

                >>> park2 == park3
                False
                >>> park1 == park4
                True
        """
        

    def __lt__(self, other):
        return self.acres<other.acres
        """
        Question 4.3
            Complete the __lt__ method. An AmusementPark object is less than another if its acreage is 
            smaller than another object's acreage

            THIS SHOULD BE DONE IN ONE LINE

            Example:
                >>> park1 = AmusementPark('Disney’s Animal Kingdom', 'April 22, 1998', 580, 'Florida', True)
                >>> park2 = AmusementPark('Six Flags Great Adventure', 'July 1, 1974', 510, 'New Jersey')

                >>> park1 < park2
                False

                >>> park2 < park1
                True
        """
        

    def __repr__(self):
        return f"{self.name}, a {self.acres}-acre amusement park located in {self.state} opened on {self.opening_date}."
        """
        Question 4.4
            Complete the __repr__ method. Calling or printing a Song object
            should be represented as the following string:

                '{names}, a {acres}-acre amusement park located in {state} opened on {opening_date}.'

            THIS SHOULD BE DONE IN ONE LINE

            Example:
                >>> park3 = AmusementPark('Busch Gardens', 'May 16, 1975', 422. 'Virginia')
                >>> print(park3)
                Busch Gardens, a 422-acre amusement park located in Virginia opened on May 16, 1975.

                >>> park2 = AmusementPark('Six Flags Great Adventure', 'July 1, 1974', 510, 'New Jersey')
                >>> print(park2)
                Six Flags Great Adventure, a 510-acre amusement park located in New Jersey opened on July 1, 1974.
        """
        

    def add_ride(self, ride):
        self.rides.append((ride))
        self.num_rides=len(self.rides)

        """
        Question 5.1
            Add a new ride to the amusement park. Make sure to pass in the object rather
            than simply an attribute name of the object.
            Update everything that needs to be updated and make sure that the ride
            is in the same amusement park.

            Assume that the ride is not already in the amusement park.

            You should have no returns on this function.

            Example:
                >>> park1 = AmusementPark('Disney’s Animal Kingdom', 'April 22, 1998', 580, 'Florida', True)

                >>> park1.add_ride(ride1)
                >>> print(park1.rides)
                [ "Falcon's Fury - a Drop Tower ride that is currently non-operational." ]
                >>> print(park1.num_rides)
                1

                >>> park1.add_ride(ride2)
                >>> print(park1.rides)
                [ "Falcon's Fury - a Drop Tower ride that is currently non-operational.", "Kali River Rapids - a Whitewater Rafting ride that is currently operational." ]
                >>> print(park1.num_rides)
                2
        """
        

    def remove_ride(self, ride_name):
        # print("Lol")
        tempRide=Ride(ride_name,"tempy", 4)
        # print(tempRide)
        # print(self.rides)
        for i in self.rides:
            # print(tempRide)
            # print("spacespacespacespace")
            # print(tempRide.name)
            # print("------- i below")
            # print(i.name)
            if i.name==tempRide.name:
                # print("lol i got here")
                self.rides.remove(i)
        self.num_rides=len(self.rides)


        """
        Question 5.2
            Remove a ride from the park. You will be given the ride name
            you should remove the corresponding ride object.
            Update everything that needs to be updated.

            Assume that the ride is in the park.

            You should have no returns on this function.

            Example:
                >>> park1 = AmusementPark('Disney’s Animal Kingdom', 'April 22, 1998', 580, 'Florida', True)

                >>> park1.remove_ride("Falcon's Fury")
                >>> print(park1.rides)
                [ "Kali River Rapids - a Whitewater Rafting ride that is currently operational." ]
                >>> print(park1.num_rides)
                1
        """
        

    def sort_rides(self):
        # print(type(self))
        # print(type(self.rides))
        # self.rides.sort()
        # print("Sorted")
        # print(self.rides)
        # self.rides.sort()
        tempylist=[]
        for i in self.rides:
            if "currently operational" in str(i): 
                tempylist.append(i)
        finallist = sorted(tempylist, key=lambda y: (-y.popularity, y.name))
        # print(type(self.rides))
        self.rides=finallist
        # print(finallist)
        # print("-----")
        # print(tempylist)



        """
        Question 6
            Sort the park's ride_list based on popularity from most popular to least popular.
            After sorting by popularity you should sort by name alphabetically. Non-operational
            rides should not be included.

            You should have no returns on this function.

            Example:

                >>> park1 = AmusementPark('Disney’s Animal Kingdom', 'April 22, 1998', 580, 'Florida', True)

                >>> park1.add_ride(ride2)
                >>> park1.add_ride(ride3)
                >>> park1.add_ride(ride5)
                >>> park1.sort_rides()
                >>> print(park1.rides)
                [ "Goliath - a Roller Coaster ride that is currently operational.", "Kali River Rapids - a Whitewater Rafting ride that is currently operational." ]
                
        """
        


if __name__ == "__main__" :

    # All of the test questions below should be tested INDEPENDENTLY

    # # Ride objects - MUST COMPLETE Q1.1 TO RUN PROPERLY
    ride1 = Ride("Falcon's Fury", 'Drop Tower', 100, False)
    ride2 = Ride('Kali River Rapids', 'Whitewater Rafting', 49)
    ride3 = Ride('Skull Mountain', 'Roller Coaster', 78, False)
    ride4 = Ride('Expedition Everest', 'Roller Coaster', 66)
    ride5 = Ride('Goliath', 'Roller Coaster', 49)

    # # AmusementPark objects - MUST COMPLETE Q4.1 TO RUN PROPERLY
    park1 = AmusementPark('Disney’s Animal Kingdom', 'April 22, 1998', 580, 'Florida', True)
    park2 = AmusementPark('Six Flags Great Adventure', 'July 1, 1974', 510, 'New Jersey')
    park3 = AmusementPark('Busch Gardens', 'May 16, 1975', 422, 'Virginia')
    park4 = AmusementPark('Disney’s Animal Kingdom', 'April 22, 1998', 580, 'Florida')


    # # Q1.1 Ride init
    # print([ride1.name, ride1.category])
    # print([ride2.popularity, ride2.operational])
    # print([ride3.name, ride3.popularity])
    # print([ride4.category, ride4.operational])

    # # Q1.2 Ride repr
    # print(ride1)
    # print(ride2)

    # # Q1.3 Ride lt
    # print(ride1 < ride2)
    # print(ride4 < ride5)
    # print(ride3 < ride2)
    # print(ride4 < ride1)


    # # Q2
    # ride2.broken_rides(True)
    # ride3.broken_rides(False)
    # ride4.broken_rides(False)
    # ride5.broken_rides(True)
    # print([ride2.operational, ride3.operational, ride4.operational, ride5.operational])


    # # Q3
    # ride1.popularity_change(100)
    # ride2.popularity_change(25)
    # ride3.popularity_change(50)
    # ride4.popularity_change(10)
    # print([ride1.popularity, ride2.popularity, ride3.popularity, ride4.popularity])


    # # Q4.1 AmusementPark init
    # print([park1.name, park1.acres, park1.is_open])
    # print([park2.name, park2.opening_date, park2.state])
    # print([park3.name, park3.is_open, park3.num_rides])
    # print([park4.name, park4.acres, park4.is_open])

    # # Q4.2 AmusementPark eq
    # print(park1 == park1)
    # print(park1 == park4)
    # print(park3 == park4)
    # print(park2 == park3)

    # # Q4.3 AmusementPark lt
    # print(park1 < park2)
    # print(park2 < park1)

    # # Q4.4 AmusementPark repr
    # print(park3)
    # print(park2)
    # print(park1)
    # print(park4)


    # Q5.1
    # park4.add_ride(ride5)
    # park4.add_ride(ride4)
    # park4.add_ride(ride1)
    # print(park4.rides)
    # print(park4.num_rides)

    # park2.add_ride(ride2)
    # park2.add_ride(ride3)
    # print(park2.rides)
    # print(park2.num_rides)

    # # # Q5.2 - MUST UNCOMMENT Q5.1 TO RUN PROPERLY
    # park4.remove_ride('Goliath')
    # park4.remove_ride('Expedition Everest')
    # print(park4.rides)
    # print(park4.num_rides)

    # park2.remove_ride('Kali River Rapids')
    # park2.remove_ride('Skull Mountain')
    # print(park2.rides)
    # print(park2.num_rides)


    # # Q6
    park1.add_ride(ride2)
    park1.add_ride(ride3)
    park1.add_ride(ride4)
    park1.add_ride(ride5)
    park1.sort_rides()
    print(park1.rides)

    # park3.add_ride(ride1)
    # park3.add_ride(ride2)
    # park3.add_ride(ride4)
    # park3.sort_rides()
    # print(park3.rides)


    pass