# a=45
# b=45
# c=a+b
# print(c)



# Taking input from user
# a=int(input("Enter the 1st number:"))
# b=int(input("Enter the 2nd number:"))
# c=a+b
# print("Total=",c)



# Data Types
# a=90
# if(type(a) is complex):
#     print("Yes")
# else:
#     print("NO")



# # Logical Operator
# a=99
# b=78
# c=54
# print(a>b and a>c)




# # List
# list=[1,2,3,4,5,6,7,8,9,10]
# list.reverse()
# print(sum(list))
# print(list)





# # For Loop
# for i in range(1,20):
#     print(i)



# # While Loop
# a=0
# while(a<10):
#     a+=1
#     print(a)
    


# list=[1,2,3,4,5,6,7]
# # result=[num**2 for num in list if num%2!=0]
# # print(result)
# print(max(list))



# check duplicates in list
# list=[1,2,3,4,5,1,7]
# duplicate=[]
# seen=set()
# for i in list:
#     if i in seen:
#         duplicate.append(i)
#     else:
#         seen.add(i)

# print("list=",list)
# print("duplicate=",duplicate)



# # check prime or non-prime
# number=int(input("Enter the number:"))
# for i in range(2,number):
#     if number%i==0:
#         print("this is not prime number")
#         break
#     else:
#         print("this is prime number")
#         break



# list=[1,2,3,4,5,6,7,8]
# output=list[0:3]
# print(output)



# list1=[1,1,2,2,3,4,4,4,5,6,6]
# output=list(set(list1))
# print(output)





# # SET 
# set={10,23,12,34,56,88}
# set.add(23)
# set.pop()
# print(set)





# # Tuple
# tuple=(20,12,34,23,56,98,78,98)
# print(tuple.index(12))
# print(tuple.count(98))





# # Dictionary
# dict={'name':'Satyam','address':'karad','rollno':31}
# # for i in dict.items():
# #     print(i)
# dict['name']='satyaaaaaam'
# dict['email']='satyam@gmail.com'
# del dict['address']
# print(dict)




# dict1={'name':'pranav','rollno':34}
# dict2={'address':'Solapur','email':'pranav@gmail.com'}
# dict1.update(dict2)
# print(dict1)



# dict={
#     'student':{'name1':'amit','rollno1':34,'address1':'pune'},
#     'teacher':{'name2':'pranav','rollno2':4566,'address2':'solapur'}
# }

# for emp,details in dict.items():
#     print(emp)
#     print("<")

#     for key in details:
#         print(key)

#     print(">")
# # print(dict['student']['name'])







# # String 
# string="software test"
# # string1=string[::-1]
# # output=''.join(string[::-1])
# # output=max(string.split(),key=str.lower)
# # print(output)
# sort=sorted(string)
# output=''.join(sort)
# print(output)



string='90234820385fshjbfiusdbfis@#@##$%'
output=" "
for i in string:
    if not i.isalnum():
        output+=i

print(output)
        