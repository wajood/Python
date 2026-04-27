name = input("Enter a name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective (e.g. funny, scary): ")
animal = input("Enter an animal: ")
action = input("Enter an action (verb): ")

story = f"""
One day, {name} went to {place}. 
It was a very {adjective} day. 
Suddenly, a {animal} appeared and started {action}. 
{name} was shocked but started laughing!
"""

print(story)