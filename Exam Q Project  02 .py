

user_name = input("Enter User Name: - ")
password = input("Enter Password: - ")

if user_name == "Admin" and password == "Admin@123":
    print("MCQ: - Are You Want To Join Exam [ Y / N ]")
    choice = input().upper()

    if choice == "Y":
        print("Select Exam type:")
        print("Maths   : 1")
        print("Python  : 2")
        exam_type = int(input("Exam type: "))

        if exam_type == 1:
            while True:
                print("1. How Much would u rate keerti institute out of 5")
                print("(a) 0")
                print("(b) 3")
                print("(c) 5")
                print("(d) 4")

                answer = input("Select Answer: ").lower()
                if answer == "a":
                    print("Correct Answer!")
                    break  # Exit the loop on correct answer
                else:
                    print("Wrong Answer! Please try again.")

        elif exam_type == 2:
            while True:
                print("2. The product of a rational and irrational number is")
                print("(a) rational")
                print("(b) irrational")
                print("(c) both of above")
                print("(d) none of above")
                answer = input("Select Answer: ").lower()
                if answer == "a":
                    print("Correct Answer!")
                    break  # Exit the loop on correct answer
                else:
                    print("Wrong Answer! Please try again.")

        else:
            print("Invalid Exam type selected.")

    elif choice == "N":
        print("Exit Program")
    else:
        print("Invalid choice.")
else:
    print("Invalid User Name or Password.")
