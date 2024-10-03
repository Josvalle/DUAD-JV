class person:
    pass

class Bus(person):
    def __init__(self):
        self.max_passengers = 30
        self.passengers = []
    
    def add_passenger(self,person):
        if len(self.passengers) >= self.max_passengers:
            print('Bus is full, we will need to wait that a passenger get out of the bus')
        else:
            self.passengers.append(person)
    
    def remove_passenger(self,):
        if len(self.passengers) == 0:
            print('Bus is empty!')
        else:
            self.passengers.pop()

def main():
    bus = Bus()
    while True:
        new_person = person()

        option = input('Do you want to add a new passenger to the bus (Y/N)')

        if option == 'Y':
            bus.add_passenger(new_person)
        elif option == 'N':
            bus.remove_passenger()
        
        continue_adding = input('Do you want to continue adding passenger (Y/N)')

        if continue_adding == "Y":
            continue
        else:
            break


if __name__ == '__main__':
    main()