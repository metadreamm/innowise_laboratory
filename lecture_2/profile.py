def generate_profile(age):
    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teenager"
    elif age >= 20 and age <= 130:
        return "Adult"
    else:
        raise Exception("Invalid values")


print("Hello!")
user_name = input('Enter your full name: ')
birth_year_str = input('Enter your birth year: ')
birth_year = int(birth_year_str)
current_age = 2025 - birth_year

hobbies = []
while(True):
    hobby = str(input("Enter a favorite hobby or type 'stop' to finish: "))
    if hobby == "stop":
        break
    hobbies.append(hobby)

life_stage = generate_profile(current_age)
user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

print("\n---")
print("Profile Summary:")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['stage']}")
if len(hobbies) == 0:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite hobbies ({len(hobbies)}):")
    for hobby in hobbies:
        print(f"- {hobby}")
print("---")
