a={
    "Name":"Saurabh",
    "Study":"PG",
    "Profession":"SW",
    "Contact":989889,
    "Saurabh":100
}

#print(a)
#print(a["Saurabh"])
#print(a.keys())
#print(a.values())
#a.update({"Study": "PHD","Amit":99})
#print(a)
print(a.get("Contact"))
print(a.get("Saurabh2"))  #If in dictinory not found then it will show none
print(a.get["Saurabh2"])  #If in dictinory not found then it will show error