import json
states_and_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar"
}



with open(r"C:\Users\sathi\OneDrive\Documents\GitHub\DS140823\json\assignment2.json","w") as file:
 json.dump(states_and_capitals,file, indent=4)

 
 
