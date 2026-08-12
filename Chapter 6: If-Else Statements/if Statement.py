# age = 20

# if age >= 18:
#     print("You are an adult")

# age = 10

# if age >= 18:
#     print("You can vote")
# else:
#     print("You cannot vote")

    # Two paths — if condition is True, if block runs; otherwise else block runs.

#    // if-elif-else Statement

# marks = 30

# if marks >= 90:
#     print("A+")
# elif marks >=75:
#     print("A")
# elif marks >= 60:
#     print("B") 
# elif marks >= 50:
#     print("C")
# else:
#     print("Fail")

#     # When you need to check multiple conditions one after another, use elif.


# temp = int(input("please tell your temperature: "))

# if temp >= -5 and temp <= 5:
#     print("It is freezing cold")
# elif temp >=6 and temp <=18:
#     print("It is cold")

# elif temp >=19 and temp <30:
#     print("It is warm")

# elif temp >=30 and temp <=40:
#     print("It is hot") 

# else :
#     print("It is very hot")


gender = input("Enter your gender (M/F): ")

if gender == "M" or gender == "m":
    print("You are a male")
elif gender == "F" or gender == "f ":
    print("You are a female")
else:
    print("Invalid input")