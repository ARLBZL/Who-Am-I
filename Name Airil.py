#Check user name
username = input("Enter name: ")
name = "Airil"
if username.lower() == name.lower():
    print("Welcome, Airil")
    # Python3 code to calculate age in years
    age = int(input("Enter age: "))

    from datetime import date

    def calculateAge(birthDate):
        today = date.today()
        age = today.year - birthDate.year -((today.month, today.day) <
            (birthDate.month, birthDate.day))

        return age
        
    # Driver code 
    if age == calculateAge(date(2002, 1, 21)):
        print("Correct.")

        hobby = input("What is your hobby? ")
        ans_hobby = "video games"

        if hobby.lower() == ans_hobby.lower():
            print("Correct.")
        else:
            print("Wrong.")

    else:
        print("Wrong.")
else:
    print("Access denied")

