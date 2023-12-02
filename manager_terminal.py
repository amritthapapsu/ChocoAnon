
import manager_controller as mc
import data

#Displays the user options
def main_menu():
    print("\n1. End of Week")
    print("2. Add Members")
    print("3. Update Member")
    print("4. Remove Member")
    print("5. Add Provider")
    print("6. Update Provider")
    print("7. Remove Provider")
    print("8. Turn Off Terminal\n")


#Generates the Provider, Member, and ETF reports.
def endOfWeek():
    mc.ManagerControl().createReport()


#Takes in a member's data, such as name, address, city, etc. Then passes to manager.py.
def addMember():
    print(mc.ManagerControl().addMember(data.BasicData().createBasicData()))


#Takes in a member's data, such as name, address, city, etc. Then passes to manager.py.
def updateMember():
    member = data.BasicData().createBasicData()
    print(mc.ManagerControl().editMember(member.Id, member))


#Takes in a member's id for deletion.
def removeMember():
    print(mc.ManagerControl().removeMember(data.BasicData().getId()))


#Takes in a provider's data, such as name, address, city, etc. Then passes to manager.py.
def addProvider():
    print(mc.ManagerControl().addProvider(data.BasicData().createBasicData()))


#Takes in a provider's data, such as name, address, city, etc. Then passes to manager.py.
def updateProvider():
    provider = data.BasicData().createBasicData()
    print(mc.ManagerControl().editProvider(provider.Id, provider))


#Takes in a provider's id for deletion.
def removeProvider():
    print(mc.ManagerControl().removeProvider(data.BasicData().getId()))


if __name__ == '__main__':
    choice = 1
    while choice != 8:
        try:
            main_menu()
            choice = int(input("Please enter choice: "))
            print()

            if choice == 1:
                endOfWeek()
            elif choice == 2:
                addMember()
            elif choice == 3:
                updateMember()
            elif choice == 4:
                removeMember()
            elif choice == 5:
                addProvider()
            elif choice == 6:
                updateProvider()
            elif choice == 7:
                removeProvider()
            elif choice == 8:
                pass
            else:
                print("Invalid Choice.")

        # Intended to catch letters/characters.
        except ValueError:
            print("Invalid Choice.")

    print("Shutting off terminal.")
