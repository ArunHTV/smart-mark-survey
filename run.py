# Open text file to save user's input
file = open("user_data.txt", "w")
print("\nSmark Mark Survey, a survey all about wrestling. But first..\n")


# Input for users name and age
print("\n")
name = input("What is your name? ")
print("-" * 80)
print("Hello, " + name + str(". Thank you for taking my quiz."))
print("-" * 80)

file.write("Name: " + name + "\n")

age = input("How old are you? ")
print("-" * 80)
print(age + str(". Oh. Getting on a bit, aren't you?"))
print("-" * 80)

file.write("Age: " + age + "\n")

# Questions

first = input("Who's the first person you associate with wrestling? ")
print("-" * 80)
print(first + str("...pff. What a casual."))
print("-" * 80)

file.write("Most associates with wrestling: " + first + "\n")

second = input("Who was your favourite wrestler growing up? ")
print("-" * 80)
print(second + str(". Not a bad pick, actually."))
print("-" * 80)

file.write("Favourite wrestler when growing up: " + second + "\n")

third = input("Who do you consider the greatest wrestler of all time? ")
print("-" * 80)
print("So you picked " + third + str(". You're kidding, right?"))
print("-" * 80)

file.write("Greatest wrestler of all time: " + third + "\n")

fourth = input("Who is your favourite tag team of all time? ")
print("-" * 80)
print("Wow...*scoff* " + fourth + str(". What a mark."))
print("-" * 80)

file.write("Greatest tag team: " + fourth + "\n")

fifth = input("What's your dream singles match that never happened? ")
print("-" * 80)
print(fifth + str(". I'm disappointed in your lack of imagination, ") + name)
print("-" * 80)

file.write("Dream singles match that didn't happen: " + fifth + "\n")

sixth = input("What's your dream singles match that could still happen? ")
print("-" * 80)
print("Hmm. " + sixth + str(". Not bad indeed."))
print("-" * 80)

file.write("Dream singles match that could happen: " + sixth + "\n")

seventh = input("Switching gears, who is your favourite manager? ")
print("-" * 80)
print(seventh + str(". A fine choice."))
print("-" * 80)

file.write("Favourite manager: " + seventh + "\n")

eighth = input("We're almost done. What's your favourite pay-per-view?. ")
print("-" * 80)
print("Strange, when I want to fall asleep I watch " + eighth + str("."))
print("-" * 80)

file.write("Favourite pay-per-view: " + eighth + "\n")

ninth = input("And, your favourite weekly wrestling show of all time? ")
print("-" * 80)
print(ninth + str(". I too like to waste hours of my life."))
print("-" * 80)

file.write("Favourite weekly wrestling show: " + ninth + "\n")

tenth = input("Lastly, who is your LEAST favourite wrestler of all time? ")
print("-" * 80)
print("Hahaha, " + tenth + str(". I love it. Way to end on a high."))
print("-" * 80)

file.write("Least favourite wrestler: " + tenth + "\n")

# Close text file
file.close()
print("Thank you for participating. Your answers have been collated.")
