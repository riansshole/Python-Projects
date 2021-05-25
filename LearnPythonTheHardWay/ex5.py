name = 'Zed A. Shaw'
age = 35
height = 74 #of inches
weights = 180 #lbs
eyes = 'Blue'
hair = 'Brown'
teeth = 'White'
kilo = 0.453592 #pounds
cm = 2.54 #inch

print(f"Let's talk about {name}")
print(f"He's {height*cm:.2f} centimeters tall")
print(f"He's {weights*kilo:.2f} kilograms heavy")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weights
print(f"If I add {age}, {height*cm:.1f}, and {weights*kilo:.1f}, I get {total}")