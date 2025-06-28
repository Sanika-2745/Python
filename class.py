
class students:
    rollno = 0
    name = ""
    fees = 0
    address = ""
    perc = 0
    
    def __init__(self,rollno,name,fees,address,perc):
        self.rollno = rollno
        self.name = name
        self.fees = fees
        self.address = address
        self.perc = perc
        
    def display(self):
        print("rollno",self.rollno)
        print("name",self.name)
        print("fees",self.fees) 
        print("address",self.address)
        print("perc",self.perc)   
        
info = students(41,"sanika",185000,"radhanagari",86)
info1 = students(19,"gauri",250000,"gargoti",83)  
info.display()
info1.display()  
      