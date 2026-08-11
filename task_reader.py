import questionary


tasks={}
with open("tasks.txt", "+r") as file:
    lines = file.readlines()
    print(lines)
