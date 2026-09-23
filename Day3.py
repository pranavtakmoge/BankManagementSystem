# # --------------------------------------File Handling --------------------------------------------- 
# file=open('text.txt','w')
# my_file=file.write('this is new text file')
# print(my_file)
# file.close()



# file=open('text.txt','r')
# for i in file:
#     print(i)



# file=open('text.txt','r')
# print(file.read(7))
# file.close()




# file=open('text.txt','a')
# data=file.write('\nKJCOEMR')
# print(data)
# file.close()




# file=open('text.txt','r')
# my_file=file.read()
# print(my_file)
# file.close()



# with open('text.txt','r+') as file:
#     file.write('this is pranav')
#     print(file.readline())


# with open('text.txt','r') as file:
#     data=file.readline()
#     print(data.upper())


# import csv
# with open('text.txt','r') as file:
#     myfile=csv.reader(file)
#     x=next(myfile)
#     for row in x:
#         print(row)




# import json
# file=open('post.json','r')
# my_file=file.read()
# x=json.loads(my_file)
# print(x)




# # --------------------------------------------------------Exception Handling---------------------------------------------------------------
# try:
#     A=int(input('Enter the 1st number : '))
#     B=int(input('Enter the 2nd number : '))
#     C=A/B
#     print(C)
# except ZeroDivisionError:
#     print('can not divided by zero !')
# else:
#     print('division performed without exception !')

# finally:
#     print("Done")





# try:
#     A=90
#     B=k
#     C=A/B
#     print(C)
# except ValueError:
#     print('inside exception !')

# else:
#     print('inside else')

# finally:
#     print('thanks')





# try:
#     A=int(input('Enter the 1st number : '))
#     B=int(input('Enter the 2nd number : '))
#     C=A/B
#     print(C)
# except ArithmeticError:
#     print('can not divided by zero !')
# else:
#     print('division performed without exception !')

# finally:
#     print("Done")






# #---------------------------------------------Lambda Function----------------------------------------------------------
# a=lambda x,y:(x%y)
# print(a(90,20))


# list=[1,2,3,4,5,6,7,8,9,10]
# a=lambda i:(i%2==0)
# for i in list:
#     if a(i):
#         print(i)


# list1=[1,2,3,4,5,6,7,8,9,10]
# output=list(filter(lambda x:x%2==0,list1))
# print(output)




# list1=[1,2,3,4,5,6,7,8,9,10]
# output=list(map(lambda x:x*x,list1))
# print(output)




# list1=[1,2,3,4,5,6,7,8,9,10]
# output=list(filter(lambda x:x%2==0,list1))
# output=list(map(lambda x:x*x,output))
# print(output)




# ------------------------------------------------- Decorator ----------------------------------------------------

# def decor_function(function):
#     def product():
#         print('this is very good product')
#         function()

#     return product()

# @decor_function
# def IIT():
#     print('welcome to IIT Mumbai')



# # ------------------------------------------------------- Iterator -------------------------------------------------------

# list=[34,90,45,44,98,48]
# x=iter(list)
# print(next(x))
# print(next(x))




# ----------------------------------------------------- Yeild ------------------------------------------------------------
# def add(a,b):
#     yield a
#     yield b

# print(add(23,44))
# print(type(next))



# a=90
# b=20

# c=b
# b=a
# a=c

# print('a : ',a)
# print('b : ',b)



def func(x,y):
    z=x,y
    print(z)

def fun(*x):
    for i in x:
        print(i)
fun(90,10)
fun(90,'satyam')
fun('satyam','suryawanshi')