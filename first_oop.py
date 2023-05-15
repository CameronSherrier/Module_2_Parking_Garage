class MyFirstGarage():

    def __init__(self):
        self.tickets = ['ticket']
        self.parkingSpaces = ['x']
        self.currentTicket = {}

    def takeTicket(self):
        self.tickets.pop()
        self.parkingSpaces.pop()

    def payForParking(self):
        paid = input("Please enter 'paid' to make payment: ")
        if paid.lower() == 'paid':
            print("You have paid for your ticket. You have 15 minutes to leave.")
            self.currentTicket[paid] = True
        else:
            pass
    
    def leaveGarage(self):
        flag = True
        while flag:
            if Rochester_Garage.currentTicket == {}:
                prompt = input("Please make payment by entering 'paid': ")
                if prompt.lower() == 'paid':
                    self.currentTicket[prompt] = True
                else:
                    print("You seriously need to pay before you leave.")
            else:
                for k,v in self.currentTicket.items():
                    if v == True:
                        print("Thank you, have a nice day!")
                        flag = False
                        self.tickets.append('ticket')
                        self.parkingSpaces.append('x')
                        break

Rochester_Garage = MyFirstGarage()

def run():

    while True:

        response = input("Would you like to Park or Leave?: ")

        if response.lower() == 'park':
            if Rochester_Garage.parkingSpaces == []:
                print("There are no spots, sorry!")
            else:
                Rochester_Garage.takeTicket()
                print("Here is your ticket")
        elif response.lower() == 'leave':
            if bool(Rochester_Garage.tickets) == True:
                print("You dont have to pay since you never bought a ticket.")
                break
            else:
                Rochester_Garage.payForParking()
                Rochester_Garage.leaveGarage()
                break
        else:
            print("Please enter a valid command.")

run()