from time import sleep
from random import randint

class Building:
    def __init__(self, floorNums, custNums):
        self.floorNums = floorNums
        self.custNums = custNums
        self.cust_up = []
        self.cust_down = []
        self.create_custs()

    def start_elevator(self, cust_up, cust_down, floorNums):
        elevator = Elevator()
        elevator.go_up(cust_up, cust_down, floorNums)

    def create_custs(self):
        for i in range(self.custNums):
            start = stop = 0
            while start == stop:
                start = self.gen_rand_start()
                stop = self.gen_rand_stop()

            if start < stop:
                self.cust_up.append(Customer(start, stop))
            elif start > stop:
                self.cust_down.append(Customer(start, stop))

        self.start_elevator(self.cust_up, self.cust_down, self.floorNums)

    def gen_rand_start(self):
        return randint(0, self.floorNums)

    def gen_rand_stop(self):
        return randint(0, self.floorNums)


class Elevator:
    def __init__(self):
        self.cur_floor = 0
        self.elev = []
    
    def in_to_elev(self,i):
        self.elev.append(i)

    def out_of_elev(self,i):
        self.elev.remove(i)

    def go_up(self, cust_up, cust_down, floorNums):
        for j in range(floorNums+1):
            sleep(1)
            print("\nWe are in floor:",self.cur_floor)
            for i in cust_up:
                if i.start_floor == self.cur_floor:
                    print('in',i)
                    self.in_to_elev(i)
                elif i.stop_floor == self.cur_floor:
                    print('out',i)
                    self.out_of_elev(i)
            print('Persons:', len(self.elev))
            self.cur_floor += 1
        print('\n------------------')
        self.go_down(cust_down, floorNums) 
                
    def go_down(self, cust_down, floorNums):
        for j in range(floorNums+1):
            self.cur_floor -= 1
            sleep(1)
            print("\nWe are in floor:",self.cur_floor)
            for i in cust_down:
                if i.start_floor == self.cur_floor:
                    print('in',i)
                    self.in_to_elev(i)
                elif i.stop_floor == self.cur_floor:
                    print('out',i)
                    self.out_of_elev(i)
            print('Persons:', len(self.elev))


class Customer:
    def __init__(self, start_floor, stop_floor):
        self.start_floor = start_floor
        self.stop_floor = stop_floor

    def __str__(self):
        return f"{self.start_floor}, {self.stop_floor}"


floorNums = int(input("# of floors: "))
custNums = int(input("# of customers: "))

building = Building(floorNums, custNums)


    