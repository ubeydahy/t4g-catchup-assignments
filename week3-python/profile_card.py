#Part 4 -- Putting it together
#Variables
first_name = "Ubeydah"
last_name = "Yussuf"
age = 19
course = "Backend development track"
cohort = "Cohort 4"
favourite_topic = "Linux"
week = "week 3"
full_name = f"{first_name} {last_name}"
current_week = 3

#String method
formatted_week = week.title()
formatted_course = course.replace("Backend development track", "Backend Development")
formatted_name = full_name.upper()

#Weeks left
weeks_left = 12 - current_week
#Profile card
print(                 "PROFILE CARD"                    )
print(f"Name: {formatted_name}")
print(f"Cohort: {cohort}")
print(f"Age: {age}")
print(f"Favourite Topic: {favourite_topic}")
print(f"Current Week: {formatted_week}")
print(f"Course: {formatted_course}")
print(f"Weeks left in the 12-week program: {weeks_left}")
