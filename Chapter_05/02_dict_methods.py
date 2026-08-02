marks = {
    "Abhi": 100,
    "Aman": 75,
    "Rohan": 85,
    0: "Abhi"
}

# print(marks.items())
#print(marks.keys())
#print(marks.values())
#marks.update({"Abhi": 99, "Harry": 95})
#print(marks)

print(marks.get("Abhi5")) # Prints None
print(marks["Abhi5"]) # Returns an error