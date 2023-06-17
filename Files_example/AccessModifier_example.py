#super class
class A:
    #public member
    var1 = None
     # protected member
    _var3 = None

    #private member
    __var3 = None

    # constructor
    def __int__(self,var1,var2,var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    #public member function
    def displayPublicMembers(self):
        # accessing public data members
        print("Public data member: ",self.var1)

    #protected member function
    def _displayProtectedMembers(self):
        # accessing public data members
        print("Protected data member: ", self._var2)
    #private member function
    def __displayPrivateMembers(self):
        # accessing public data members
        print("Private data member: ", self.__var3)
    #public member function
    def accessPrivateMembers(self):
        # accessing public data members
        self.__displayPrivateMembers()

class B(A):
    #constructor
    def __int__(self, var1, var2, var3):
        A.__int__(self, var1, var2, var3) # or  can use super.__int__(self, var1, var2, var3)

    # public member function
    def accessProtectedMembers(self):
        #accessing protected member functions of super class
        self._displayProtectedMembers()

# creating objects of the derived class
obj=B('Pub_Red','Pro_White','Private_Green')

#calling public members of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

#object can access public members
print('object is accessing public member', obj.var1)
#object can access protected members
print('object is accessing protected member', obj._var2)
#object cannot access private members, so it will generate Attribute error
#print(obj.__var3)
print(obj._A__var3) #Accessing Name Mangled variables
#Name Mangling
#A process in which any given identifier with one trailing underscore and two leading underscore
# is textually replaced with the _Classname__Identifier is known as 'Name Mangling'.
# In _Classname__Identifier name,
