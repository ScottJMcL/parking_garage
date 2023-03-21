# Parking Garage Project


class Garage():
    '''
    TO DO: Fill out documentation
    '''

    def __init__(self, tickets, parkingSpaces):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = {}
        for spot in range(1, self.tickets + 1):
            self.currentTicket[spot] = None
        self.pay = 0
        self.cost = 5
    
    def takeTicket(self):
        if self.tickets < 1:
            print('\nNo spaces available. Please come back later!')
        else:
            self.tickets -= 1
            self.parkingSpaces -= 1
            lookingForParking = True
            while lookingForParking:
                for key, value in self.currentTicket.items():
                    if value == None:
                        print("Found a spot.")
                        lookingForParking = False
                        self.currentTicket[key] = False
                        print(f'your ticket number is: {key}')
                        break
                    elif value == False:
                        # print("Still looking")
                        continue
                    elif value == True:
                        print("Waiting")
                        print("Found a spot.")
                        lookingForParking = False
                        self.currentTicket[key] = False
                        print(f'your ticket number is: {key}')
                        break
    
            
    
    def payForParking(self, ticketNum):
        '''
        Displays an input that waits for an amount from the user.
        If the payment is more than the ticket price ($5), displays a message
        that their ticket has been paid and they have 15mins to leave.
        Updates the "currentTicket" dictionary key "paid" to True
        '''
        print("")
        self.pay = int(input("Kiosk: Please insert $5: "))
        while self.pay < self.cost:
                morePay = int(input("Insufficient funds. Parking costs $5 total."))
                self.pay = morePay + self.pay
        if self.pay > self.cost:
            print(f"Here is your change: ${self.pay - self.cost}")
            print("You have 15 minutes to exit.")
            self.currentTicket[ticketNum] = True
            self.tickets += 1
            # print(f'{ticketNum} has been paid and is set to {self.currentTicket[ticketNum]}.')
        elif self.pay == self.cost:
            print("You have 15 minutes to exit.")
            self.currentTicket[ticketNum] = True
            self.tickets += 1
            # print(f'{ticketNum} has been paid and is set to {self.currentTicket[ticketNum]}.')
        else:
             print("Error1")
        self.pay = 0
            
    def leaveGarage(self, ticketNum):
         '''
            If the ticket has been paid, displays a message of "Thank You, have a nice day"
            If the ticket has not been paid, display an input prompt for payment
            Once paid, displays message "Thank you, have a nice day!"
            Updates parkingSpaces list to increase by 1
            Updates tickets list to increase by 1
         '''

         try:
            if self.currentTicket[ticketNum] == True:
                print("\nTicketbooth: Paid at kiosk. Thank You, have a nice day\n")
                self.parkingSpaces += 1
                self.currentTicket[ticketNum] = None
            elif self.currentTicket[ticketNum] == False:
                print("")
                self.pay = int(input("Ticketbooth: Please insert $5: "))
                while self.pay < self.cost:
                    morePay = int(input("Insufficient funds. Parking costs $5 total."))
                    self.pay = morePay + self.pay
                if self.pay > self.cost:
                    print(f"Here is your change: ${self.pay - self.cost}")
                    print("Ticketbooth: Thank You, have a nice day\n")
                    self.currentTicket[ticketNum]: True
                    self.tickets += 1
                    self.parkingSpaces += 1
                    # print(f'{ticketNum} has been paid and is set to {self.currentTicket[ticketNum]}.')
                    self.currentTicket[ticketNum] = None
                    print(f'{ticketNum} set to {self.currentTicket[ticketNum]}.')
                elif self.pay == self.cost:
                    print("\nTicketbooth: Thank You, have a nice day\n")
                    self.currentTicket[ticketNum]: True
                    self.tickets += 1
                    self.parkingSpaces += 1
                    # print(f'{ticketNum} has been paid and is set to {self.currentTicket[ticketNum]}.')
                    self.currentTicket[ticketNum] = None
                    # print(f'{ticketNum} set to {self.currentTicket[ticketNum]}.')
                else:
                    print("Error2")
         except:
             print("\n'ow'd you git in 'ere?? Pay me $20 and git!")
             print("")
             self.pay = int(input("Owner: Insert $20: "))
             while self.pay < 20:
                morePay = int(input("Insufficient funds. Overnight parking costs $20 total."))
                self.pay = morePay + self.pay
             if self.pay > 20:
                print(f"Here is your change: ${self.pay - 20}")
                print("Owner: Thank You, now Git!\n")
             elif self.pay == 20:
                print("Owner: Thank You, now Git!\n")
             else:
                print("Error3")
             self.pay = 0
         


         
         
         
    
    def dispInfo(self):
        '''
        Displays current capacity, current price, # of tickets available, and
        the state of each spot in the garage.
        '''
        print(f"\nCurrent capacity: {self.parkingSpaces}")
        print(f"Price: ${self.cost}")
        print(f"Tickets: {self.tickets}")
        for spot, state in self.currentTicket.items():
            print(f'Spot {spot} is currently set to {self.currentTicket[spot]}')
        print("")


garageSize = 5
print(f"\nBuilding garage with {garageSize} spots.")
Huntington_and_Rosemead = Garage(garageSize, garageSize)

print("\nTake 1")
Huntington_and_Rosemead.takeTicket()
print("\nTake 2")
Huntington_and_Rosemead.takeTicket()
print("\nTake 3")
Huntington_and_Rosemead.takeTicket()
print("\nTake 4")
Huntington_and_Rosemead.takeTicket()
print("\nTake 5")
Huntington_and_Rosemead.takeTicket()
print("\nTake 6")
Huntington_and_Rosemead.takeTicket()

print("\nPay 1")
Huntington_and_Rosemead.payForParking(1)
print("\nPay 2")
Huntington_and_Rosemead.payForParking(2)
print("\nPay 3")
Huntington_and_Rosemead.payForParking(3)
print("\nLeave 1")
Huntington_and_Rosemead.leaveGarage(1)
print("\nLeave  2")
Huntington_and_Rosemead.leaveGarage(2)
print("\nLeave  3")
Huntington_and_Rosemead.leaveGarage(3)
print("\nLeave  4 (no pay)")
Huntington_and_Rosemead.leaveGarage(4)
print("\nPay 5")
Huntington_and_Rosemead.payForParking(5)
print("Leave 5")
Huntington_and_Rosemead.leaveGarage(5)

print("\nInfo:")
Huntington_and_Rosemead.dispInfo()

print("Leave 6 (no pay), should crash")
Huntington_and_Rosemead.leaveGarage(6)

print("\nInfo:")
Huntington_and_Rosemead.dispInfo()


