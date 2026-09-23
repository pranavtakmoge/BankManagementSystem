# class parent1:
#     def show(self):
#         print('this is parent1 class')

# class parent2:
#     def printdetails(self):
#         print('this is parent2 class')



# class child(parent1,parent2):
#     def display(self):
#         print('this is child class')


# obj=child()
# obj.show()
# obj.printdetails()
# obj.display()





# class product:
#     def show(self):
#         print(self.name)
#         print(self.price)


# class IIT(product):
#     def show(self):
#         super().show()
#         print("Welcome to IIT Delhi")


# obj=IIT()
# obj.name='Iphone17'
# obj.price=99900
# obj.show()



# class product:
#     def show(self,name=''):
#         print('this is very good product :'+name)

# obj=product()
# obj.show()
# obj.show('laptop')




# Encapsulation - encapsulation means keeping data and methods together and controlling access to data




# class school:
#     def __init__(self):
#         self.__name='Dav' #private data
#         self.__address='pune' 

#         print(self.__name)
#         print(self.__address)

# obj=school()




# class school:
#     def __init__(self):
#         self._name='Dav'  #protected data
#         self._address='pune'

#         print(self._name)
#         print(self._address)

# obj=school()




# class school:
#     def __init__(self):
#         self.name='Dav'  #public data
#         self.address='pune'

#         print(self.name)
#         print(self.address)
# obj=school() 




# class mobileinfo():
#     def __init__(self):
#         self._name=''

#     def getname(self):
#         return self._name

#     def setname(self,name):
#         self._name=name
#         print(self._name)

# obj=mobileinfo()
# obj.getname()
# obj.setname('mobile')

    

               
# Abstraction ->abstraction hides the internal data and shows only the outer data

