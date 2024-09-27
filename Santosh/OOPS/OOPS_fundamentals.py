"""

Class: Class is the blueprint of the object where we defined all the methods/attributes and properties of  the object

Object: Object is an entity through which we access all the properties/attributes/methods defined in the class

Methods: Method is a code block in side the class which has its own feature and functionality.

Constructor:

Variables:


"""
#
# # Class
# class abc:
#     def __init__(self):
#         print('Initiale the memory - Constructor')
#     # Method
#     def greetings(self):
#         print('Good Morning')
#
#     def addition(self):
#         n1 = 100
#         n2 = 200
#         print(n1+n2)
#
#
# # Creating Object
# obj_abc1 = abc()    # default constructor is executed
# obj_abc2 = abc()    # default constructor is executed
# obj_abc3 = abc()    # default constructor is executed
# obj_abc4 = abc()    # default constructor is executed
#
# obj_abc1.greetings()    # accessing a method through class using object
# obj_abc2.addition()
#
# ################## class with parametrize constructor ##############
# class car:
#     # parametrised constructor
#     def __init__(self, car_name, car_price, car_company):
#         self.car_name1 = car_name    # instance variable
#         self.car_price1 = car_price
#         self.car_company1 = car_company
#         self.show_car_greetings()
#
#     def show_car_greetings(self):
#         print(f'Welcome to {self.car_company1} and Drive your {self.car_name1} slowly')
#
#     def show_car_name(self):
#         print('Car Name is : ', self.car_name1)
#
#     def show_car_price(self):
#         print('Car Price is : ', self.car_price1)
#
#     def show_car_company(self):
#         print('Car Company is : ', self.car_company1)
#
#     def show_car_details(self):
#         self.show_car_name()
#         self.show_car_price()
#         self.show_car_company()
#
# obj_car1 = car('Sonet', '15lacs', 'Kia')
#
#
# # obj_car1.show_car_name()
# # obj_car1.show_car_price()
# # obj_car1.show_car_company()
# obj_car1.show_car_details()
#
# obj_car2 = car('Creta', '20lacs', 'Hyundai')
# obj_car2.show_car_details()

# Home work :
# create a class structure for school institute.

class school_institute_details():

    school_located = 'Bailhongal'
    def __init__(self):
        print('Welcome to School')
        self.school = 'SNVVS'
        print(self.school)


    def school_departments(self, p, c, m, b):
        print('Departments: ', p, c,m,b)

    def school_sports(self, c, f, v, b):
        print('Sports : ', c, f, v, b)

    def school_lecturers(self, a, b, c, d):
        print('Lecturers : ', a, b, c, d)

    def school_all_details(self):
        self.school_departments('Physics', 'Chemistry', 'Maths', 'Biology')
        self.school_sports('Cricket', 'Football', 'Volleyball', 'Basketball')
        self.school_lecturers('Advik', 'Shravik', 'Santosh', 'Shruti')
        self.school_place()

    @classmethod
    def school_place(cls):
        print(f'School is located in : {cls.school_located}')


obj_school_institute_details = school_institute_details()
# obj_school_institute_details.school_departments('Physics', 'Chemistry', 'Maths', 'Biology')
# obj_school_institute_details.school_sports('Cricket', 'Football', 'Volleyball', 'Basketball')
# obj_school_institute_details.school_lecturers('Advik', 'Shravik', 'Santosh', 'Shruti')

obj_school_institute_details.school_all_details()






















