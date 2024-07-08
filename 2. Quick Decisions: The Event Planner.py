#Task 1: Code Correction You are provided with a Python script that is supposed to help in event 
# planning, but it has errors. Identify and fix them.
#Task 2: Venue Selection
# Based on the corrected code from Task 1, further enhance your code to recommend additional things like 
# "audio system" or "projector" based on the number of attendees.

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
equipment = "audio system" if attendees > 100 else "projector"
print(equipment)

#attendees = int(input("Enter number of attendees: "))
#equipment = "audio system" if attendees > 75 else "projector"
#print(equipment)


#Task 3: Catering Choices
#Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" 
# if yes, otherwise recommend "Gourmet Meals Caterers".

meal = input("Do you want vegetarian food? (Y/N) ")
recomedation = "Veggie Delight Caterers" if meal == "yes" else "Fourmet Meal Caterers"
print(recomedation)