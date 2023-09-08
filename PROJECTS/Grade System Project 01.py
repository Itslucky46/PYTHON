# # >85	        O  
# # 75 to 85	A
# # 60 to 75	B
# # 45 to 60	C
# # 35 to 45	D
# # 0 - 35	Fail



Name=str(input("Enter Your Name : "))
School_Name=str(input("Enter Your School_Name : "))
Java_Marks=int(input("Enter Java Marks out of 100 : "))
Cplus_Marks=int(input("Enter C++ Marks out of 100 : "))
JSP_Marks=int(input("Enter JSP Marks out of 100 : "))
Python_Marks=int(input("Enter Python Marks out of 100 : "))
JavaScript_Marks=int(input("Enter JavaScript Marks out of 100 : "))
GO_Marks=int(input("Enter GO Marks out of 100 : "))



def Grade(marks):
    if marks>=85:
        return "O"
    elif marks>=75:
        return "A"
    elif marks>=60:
        return "B"
    elif marks>=45:
        return "C"
    elif marks>=35:
        return "D"    
    else:
        return "Fail"  



Total=Java_Marks+Cplus_Marks+JSP_Marks+Python_Marks+JavaScript_Marks+GO_Marks
percentage=int((Total/600)*100)
overallgrade=Grade(percentage)

print("School Name      : ",School_Name)
print("Name             : ",Name)
print("Java marks       = ",Java_Marks,"/ 100 - Grade",Grade(Java_Marks))
print("C++ Marks        = ",Cplus_Marks,"/ 100 - Grade",Grade(Cplus_Marks))
print("JSP MArks        = ",JSP_Marks,"/ 100 - Grade",Grade(JSP_Marks))
print("Python Marks     = ",Python_Marks,"/ 100 - Grade",Grade(Python_Marks))
print("JavaScript Marks = ",JavaScript_Marks,"/ 100 - Grade",Grade(JavaScript_Marks))
print("GO Marks         = ",GO_Marks,"/ 100 - Grade",Grade(GO_Marks))
print("------------------------------------------------")
print("Total            : ",Total)
print("Percentage       : ",percentage,"%")
print("Overall Grade    : ",overallgrade)        






# NAME=input("ENTER YOUR NAME : ")
# DESIGNATION=input("ENTER  YOUR DESIGNATION : ")
# PASSWORD=int(input("ENTER YOUR PASSWORD : "))

# def ACCESS(DESIGNATION):
#     if DESIGNATION =="ADMIN" or "MANAGER" :
#         return "ACCESS GRANTED"
#     else:
#         return "ACCESS DENIED"    
# if DESIGNATION == "ADMIN" or "MANAGER" and PASSWORD == 123456:
#      print("acess granted")
# else:
#     print( "Acess Denied"    )


# print(NAME)
# print(DESIGNATION)
