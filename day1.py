############        Question 18, password strength checker      ##########
############        Group members: Esteban Galvan, Lance Espino ##########
passwordlength = int(input("How long is your password?: "))
specialused = input("Does your password have any special characters? (@, #, $) Y/N: ").lower()

if passwordlength < 8: 
    print ("Password is too short!")
#if the password is less than 8 characters

elif passwordlength > 8 <= 11:
    if specialused == "y":
        print("moderate strength")

    elif specialused == "n": 
        print("Weak password, add special characters")
#if the password is between 8-12 characters and if it uses special characters

elif passwordlength >= 12: 
    if specialused == "y": 
        print("Strong password!")

    elif specialused == "n":
        print("add special characters to make the password stronger!")
#if the password goes above 12 characters and if it uses special characters

############# Question 10, Scholarship checker ##################

grade_point_average = float(input("What is your Grade Point Average?: "))
community_service_hours = float(input("How many community service hours have you done?: "))
# asks the user for their GPA and community service hours

if grade_point_average >= 3.5:
    if community_service_hours > 50:
        print("Eligible for full scholarship.")
    elif community_service_hours > 30 and community_service_hours < 50:
        print("Eligible for partial scholarship")
# if the user's GPA is 3.5 or higher, it goes through this process where it tells the user if
# they're eligible for a full or partial scholarship depending on their community service hours

if grade_point_average > 3 and grade_point_average < 3.5:
    if community_service_hours > 50:
        print("Eligible for partial scholarship")
    else:
        print("Requires more community service hours for scholarship consideration")
# if the user's GPA is between 3.0 and 3.5, it goes through this process where it tells the user if they're eligible
# for a partial scholarship or they require more hours for a scholarship depending on their community service hours

if grade_point_average < 3:
    print("Not eligible for scholarship")
# if the user's GPA is below than 3.0 they are not eligible for any scholarship