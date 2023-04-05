class Garage():
    '''
    Creates a parking garage with given number of spots.  
    Required input: Integer for spots, float for price
    '''

    def __init__(self, parkingSpaces, price):
        self.tickets = parkingSpaces
        self.parkingSpaces = parkingSpaces
        self.currentTicket = {}
        for spot in range(1, self.tickets + 1):
            self.currentTicket[spot] = "Empty"
        self.pay = 0
        self.cost = price

    ######################## ------------------------- #########################
    
    def takeTicket(self):
        print("")
        if self.parkingSpaces < 1:
            print('\nNo spaces available. Please come back later!')
        else:
            self.tickets -= 1
            lookingForParking = True
            while lookingForParking:
                for key, value in self.currentTicket.items():
                    if value == "Empty":
                        print("Found a spot.")
                        lookingForParking = False
                        self.currentTicket[key] = "Full"
                        self.parkingSpaces -= 1
                        print(f'your ticket number is: {key}')
                        break
                    elif value == "Full":
                        # print("Still looking")
                        continue
                    elif value == "Paid":
                        print(f"Car with ticket {key} has paid but not exited yet.")
                        return None
                    else:
                        print("Error 17")
                        continue
            
        
    
    ################# ----------payForParking--------------- ###################

    def payForParking(self):
        '''
        Displays an input that waits for an amount from the user.
        If the payment is more than the ticket price ($5), displays a message
        that their ticket has been paid and they have 15mins to leave.
        Updates the "currentTicket" dictionary key to "Paid"
        '''
        print("")
        if "Full" not in self.currentTicket.values():
             print("No one in garage yet, try taking a ticket.")
             return None
             
        ticketNum = input("Please enter ticket number: ")
        while ticketNum.lower() != "q":
            if ticketNum.lower() == "q":
                return None
            try:
                ticketNum = int(ticketNum)
                break
            except:
                print(f"Input must be integer between 1 and {self.tickets}")
                ticketNum = input("Please enter ticket number.: ")
                continue
        
        try:
            if self.currentTicket[ticketNum] == "Empty":
                while self.currentTicket[ticketNum] == "Empty" or self.currentTicket[ticketNum] == "Paid":
                    try:
                        ticketNum = int(input("Are you sure you entered the right number? Try again: "))
                    except:
                        print(f"Input must be integer between 1 and {self.tickets}")
                        ticketNum = input("Please enter ticket number: ")
                    if ticketNum == "q":
                        return None
                    else:
                        ticketNum = int(ticketNum)
        except:
            return None
          
        try:
            self.pay = float(input("Kiosk: Please insert $5: "))
        except:
            while self.pay.lower() != "q":
                self.pay = input("Input must be a number: ")
                if self.pay.lower() == "q":
                    break
                else:
                    try:
                        self.pay = float(self.pay)
                        break
                    except:
                        continue

        while self.pay < self.cost:
                try:
                    morePay = float(input("Insufficient funds. Parking costs $5 total. "))
                except:
                    while morePay.lower() != "q":
                        morePay = input("Input must be a number: ")
                        if morePay.lower() == "q":
                            break
                        else:
                            try:
                                morePay = float(morePay)
                                break
                            except:
                                continue
                self.pay = morePay + self.pay
        
        if self.pay > self.cost:
            print(f"Here is your change: ${self.pay - self.cost}")
            print("You have 15 minutes to exit.")
            self.currentTicket[ticketNum] = "Paid"
            self.tickets += 1
            print(f'{ticketNum} has been paid and is set to {self.currentTicket[ticketNum]}.')
        elif self.pay == self.cost:
            print("You have 15 minutes to exit.")
            self.currentTicket[ticketNum] = "Paid"
            self.tickets += 1
            print(f'{ticketNum} has been paid and is set to {self.currentTicket[ticketNum]}.')
        else:
             print("Error1")
        self.pay = 0
            
    ################### ----------leaveGarage--------------- ###################

    def leaveGarage(self):
         '''
            If the ticket has been paid, displays a message of "Thank You, have a nice day"
            If the ticket has not been paid, display an input prompt for payment
            Once paid, displays message "Thank you, have a nice day!"
            Updates parkingSpaces list to increase by 1
            Updates tickets list to increase by 1
         '''
         print("")
         if "Full" not in self.currentTicket.values():
             print("No one in garage yet, try taking a ticket.")
             return None
             
         ticketNum = input("Please enter ticket number: 'q' to exit. ")
         while ticketNum.lower() != "q":
            if ticketNum.lower() == "q":
                return None
            try:
                ticketNum = int(ticketNum)
                break
            except:
                print(f"Input must be integer between 1 and {self.tickets}")
                ticketNum = input("Please enter ticket number: ")
                continue
         
         try:
            if ticketNum not in self.currentTicket:
                while ticketNum not in self.currentTicket:
                    print(f"input must be a number between 1 and {self.tickets}")
                    ticketNum = input("Are you sure you entered the right number? Try again: ")
                    if ticketNum == "q":
                        return None
                    else:
                        try:
                            ticketNum = int(ticketNum)
                            break
                        except:
                            continue
            elif self.currentTicket[ticketNum] == "Paid":
                print("\nTicketbooth: Paid at kiosk. Thank You, have a nice day\n")
                self.parkingSpaces += 1
                self.currentTicket[ticketNum] = "Empty"
            elif self.currentTicket[ticketNum] == "Full":
                print("")
                self.pay = float(input(f"Ticketbooth: Please insert ${self.cost}: "))
                while self.pay < self.cost:
                    morePay = float(input(f"Insufficient funds. Parking costs ${self.cost} total. "))
                    self.pay = morePay + self.pay
                if self.pay > self.cost:
                    print(f"Here is your change: ${self.pay - self.cost}")
                    print("Ticketbooth: Thank You, have a nice day\n")
                    self.currentTicket[ticketNum] = "Empty"
                    self.tickets += 1
                    self.parkingSpaces += 1
                    print(f'{ticketNum} has been paid and is set to {self.currentTicket[ticketNum]}.')
                    self.currentTicket[ticketNum] = "Empty"
                    print(f'{ticketNum} set to {self.currentTicket[ticketNum]}.')
                elif self.pay == self.cost:
                    print("\nTicketbooth: Thank You, have a nice day\n")
                    self.currentTicket[ticketNum]  = "Empty"
                    self.tickets += 1
                    self.parkingSpaces += 1
                    print(f'{ticketNum} has been paid and is set to {self.currentTicket[ticketNum]}.')
                    self.currentTicket[ticketNum] = "Empty"
            elif self.currentTicket[ticketNum] == "Empty":
                while self.currentTicket[ticketNum] == "Empty":
                    ticketNum = input("Are you sure you entered the right number? Try again: ")
                    if ticketNum == "q":
                        break
                    else:
                        ticketNum = int(ticketNum)
            else:
                print("Error in parsing ticket while leaving garage.")

         except:
             return None
            
    #################### ---------dispInfo---------------- #####################

    def dispInfo(self):
        '''
        Displays current capacity, current price, # of tickets available, and
        the state of each spot in the garage.
        '''
        print(f"\nCurrent capacity: {self.parkingSpaces}")
        print(f"Price: ${self.cost}")
        print(f"Tickets: {self.tickets}")
        for spot, state in self.currentTicket.items():
            print(f'Spot {spot} is currently set to {state}')
        print("")



garageSize = 20
price = 5
print(f"\nBuilding garage with {garageSize} spots for ${price}.")
Huntington_and_Rosemead = Garage(garageSize, price)

user = ""
while user != "q" or user != "quit":
    
    user = input("Please (T)ake a ticket, (P)ay for parking, or (L)eave the garage: ")
    user = user.lower()

    if user == "t" or user == "take":
        Huntington_and_Rosemead.takeTicket()
    elif user == "p" or user == "pay":
        Huntington_and_Rosemead.payForParking()
    elif user == "l" or user == "leave":
        Huntington_and_Rosemead.leaveGarage()
    elif user == "i" or user == "info":
        Huntington_and_Rosemead.dispInfo()
    elif user == "q" or user == "quit":
        print("Quitting")
        break
    else:
        print("Invalid input, please try again.")


