


class Workers:
    def __init__ (self,id,name):
        self.id=id
        self.name=name
        
    def display(self):
        print(self.id,self.name)

work1= Workers(12,"Fawa")
work1.display()
work2=Workers(10,"Mini")
work2.display()
