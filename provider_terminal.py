import provider_controller as pc
import data


#Displays the main menu
def main_menu():
    print("\n1. Create Service Record")
    print("2. Show Provider Directory")
    print("3. Logout\n")


#Displays provider directory.
def displayProviderDirectory():
    directory = pc.ProviderControl().getProviderDirectory()

    for service in directory:
        print(f"Service: {service['name']}\nCode: {service['code']}\nFee: {service['fee']}")


#This will take user input and pass it to provider.py. Lots of back and forth.
def createServiceRecord(providerNumber):
    memberRecord = data.ServiceData()

    #Checks if the member is valid
    memberRecord.memberNumber = memberRecord.getMemberNumber()
    memberStatus = pc.ProviderControl().messageMemberId(memberRecord.memberNumber)
    if (memberStatus != "Valid"):
        print(memberStatus)
        return
    print("Validated")

    #Gets date of service from user.
    memberRecord.dateOfService = memberRecord.getDateOfService()


    #Gets the service code from the user, then verifies its validity.
    memberRecord.serviceCode = memberRecord.getServiceCode()
    result = pc.ProviderControl().verifyServiceCode(memberRecord.serviceCode)
    if (result == False):
        print("Invalid Service")
        return

    #Prints service. Then asks the user to re-enter and verify service.
    for service in pc.ProviderControl().getProviderDirectory():
        if service['code'] == memberRecord.serviceCode:
            print(f"Verify that the service provided was '{service['name']}'.")
    serviceCodeVerify = memberRecord.getServiceCode()
    if (memberRecord.serviceCode != serviceCodeVerify): #If does not match.
        print("Does not match previous entry. Canceling service.")
        return
    result = pc.ProviderControl().verifyServiceCode(memberRecord.serviceCode)
    if (result == False): #If does not exist.
        print("Invalid Service")
        return
    
    #Gets comment from user.
    memberRecord.comments = memberRecord.getComment()

    #Creates service record data object.
    serviceRecord = pc.ProviderControl().createServiceRecord(
            providerNumber,
            memberRecord.memberNumber, 
            memberRecord.serviceCode,
            memberRecord.dateOfService,
            memberRecord.comments)
    if (type(serviceRecord) != dict):
        print(serviceRecord)
        return

    #Adds service record to disk.
    pc.ProviderControl().appendServiceRecord(serviceRecord)
    print("Written into database.")

    #Prints fee for verification.
    print(f"\nFee for the service is: {pc.ProviderControl().getServiceFee(memberRecord.serviceCode)}")

    #Verification of above entered information.
    verifyRecord = data.ServiceData()
    verifyRecord.dateOfService = '1-1-1000'
    verifyName = ''
    verifyFee = -1
    while (pc.ProviderControl().verifyService(
        verifyRecord.dateOfService, 
        verifyName, 
        verifyRecord.memberNumber, 
        verifyRecord.serviceCode, 
        verifyFee) != True):

        print("\nFor verification, please re-enter information when prompted.")
        verifyRecord.dateOfService = '1-1-1000'
        verifyName = ''
        verifyFee = -1

        try:
            verifyRecord.dateOfService = verifyRecord.getDateOfService()
            verifyName = data.BasicData().getName()
            verifyRecord.memberNumber = verifyRecord.getMemberNumber()
            verifyRecord.serviceCode = verifyRecord.getServiceCode()
            verifyFee = int(input("Enter the service fee: "))

        except ValueError:
            verifyRecord.dateOfService = '1-1-1000'
            verifyName = ''
            verifyFee = -1
            print("Invalid.")


#Placeholder for provider.py function
def login():
    providerNumber = data.ServiceData().getProviderNumber()

    while (pc.ProviderControl().giveAuthorization(providerNumber) == False):
        providerNumber = data.ServiceData().getProviderNumber()

    return providerNumber


if __name__ == '__main__':
    providerNumber = login()

    choice = 0
    while choice != 3:
        try:
            main_menu()
            choice = int(input("Please enter choice: "))
            print()

            if choice == 1:
                createServiceRecord(providerNumber)
            elif choice == 2:
                displayProviderDirectory()
            elif choice == 3:
                pass
            else:
                print("Invalid.")

        except ValueError:
            print("Invalid.")

    print("Logging out.")
