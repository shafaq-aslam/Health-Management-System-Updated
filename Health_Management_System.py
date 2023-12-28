import datetime

print("          HEALTH MANAGEMENT SYSTEM          \n")


class DietPlan:

    def dietPlan(self, name):
        self.name = name
        with open(f"{name}Diet.text", "a") as f:
            f.write(str(datetime.datetime.now().strftime("Date: %m/%d/%Y,\nTime: %H:%M:%S")) + " " + input(
                "Enter Diet Plan Here: "))
            print("Diet Plan Added Successfully!")


class ExePlan:

    def exePlan(self, name):
        self.name = name
        with open(f"{name}Exe.text", "a") as f:
            f.write(str(datetime.datetime.now().strftime("Date: %m/%d/%Y,\nTime: %H:%M:%S")) + " " + input(
                "Enter Exercise Plan Here: "))
            print("Exercise Plan Added Successfully!")


class RetDietPlan:

    def retDietPlan(self, name):
        self.name = name
        try:
            with open(f"{name}Diet.text", "r") as f:
                file = f.read()
                print(file)
        except FileNotFoundError:
            print("File Not Found")


class RetExePlan:

    def retExePlan(self, name):
        self.name = name
        try:
            with open(f"{name}Exe.text", "r") as f:
                file = f.read()
                print(file)
        except FileNotFoundError:
            print("File Not Found")


while True:
    pde = input("1 for Add Diet Planner \n2 for Add Exercise Planner \nWhat do you want?: ")
    if pde == '1':
        name = input("For whom you want to plan Diet? \nEnter Name Here: ")
        Name = DietPlan()
        Name.dietPlan(name)
    else:
        name = input("For whom you want to plan Exercise? \nEnter Name Here: ")
        Name = ExePlan()
        Name.exePlan(name)

    while True:
        ask = input("Want to retrieve diet plan or exercise plan?(Y/N): ")
        if ask == 'Y'.lower():
            pde = input("1 for Retrieve Diet Planner \n2 for Retrieve Exercise Planner \nWhat do you want?: ")
            if pde == '1':
                name = input("Whose diet plan you want to retrieve? \nEnter Name Here: ")
                Name = RetDietPlan()
                Name.retDietPlan(name)
            else:
                name = input("Whose exercise plan you want to retrieve? \nEnter Name Here: ")
                Name = RetExePlan()
                Name.retExePlan(name)

            perm1 = input("Want to retrieve more planners?(Y/N): ")
            if perm1 == 'y':
                continue
            else:
                break
        else:
            break

    perm2 = input("Want to enter more planners?(Y/N): ").lower()
    if perm2 != 'y':
        break

print("Bye Bye... Come again!")
