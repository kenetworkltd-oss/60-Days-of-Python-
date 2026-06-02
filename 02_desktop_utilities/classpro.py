  #start with the blueprint (class and its attributes)
  
class Organization: #class for organization information
    def __init__(self, name, registration_number, address, tel, ceo_name): #constructor/parameter for organization class
        #attributes data
        self.name = name 
        self.registration_number = registration_number
        self.address = address
        self.tel = tel
        self.ceo_name = ceo_name 
        
        #passing attributes to the print for value\data display
    def show_organization_info(self):
        print(f"Organization Name:{self.name}")
        print(f"Our registration number:{self.registration_number}")
        print(f"Our address located at: {self.address}")
        print(f"Our telephone number is: {self.tel}")
        print(f"The CEO name is : {self.ceo_name}")
        
        #creating an object while passing the argumment/value inside the class(def __init__(name, registration_number, address, tel, ceo_name))
our_organiza = Organization("SQI", "136467", "Iwo road", "0713378553", "MR Farakan")

#call out def func in attributes to fully display the value for each of the variable while it print 
our_organiza.show_organization_info()