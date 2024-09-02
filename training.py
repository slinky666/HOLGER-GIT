# Variabler och datatyper
antal_äpplen = 5
jävla_grisar = 3
storlek = 1.75
namn = "Kalle"
är_hungrig = True

# Utskrift
print(f"{namn} har {antal_äpplen} äpplen och {jävla_grisar} grisar.")

# Enkel matematik
total_grisar = jävla_grisar + 2
print(f"Efter att ha fått fler grisar, har {namn} nu {total_grisar} grisar.")

# If-sats
if är_hungrig:
    print(f"{namn} är hungrig och äter ett äpple.")
    antal_äpplen -= 1
else:
    print(f"{namn} är mätt och låter äpplena vara.")

print(f"Nu har {namn} {antal_äpplen} äpplen kvar.")

# While-loop
antal_banor = 0
while antal_banor < 5:
    print(f"{namn} springer en bana till. Totalt: {antal_banor + 1} banor.")
    antal_banor += 1

# For-loop
svordomar = ["Fan", "Helvete", "Jävlar", "Skit"]
for svordom in svordomar:
    print(f"{namn} säger: {svordom}!")

# Funktioner
def hälsa(namn):
    return f"Hej, {namn}!"

hälsning = hälsa("Lisa")
print(hälsning)

# Listor och iteration
frukter = ["äpple", "banan", "päron"]
for frukt in frukter:
    print(f"{namn} har en {frukt}.")

# Dictionary
huvudstäder = {"Sverige": "Stockholm", "Norge": "Oslo", "Finland": "Helsingfors"}
for land, stad in huvudstäder.items():
    print(f"Huvudstaden i {land} är {stad}.")

# Hantera fel
try:
    resultat = antal_äpplen / 0
except ZeroDivisionError:
    print("Aj fan, du kan inte dela med noll!")


googol = 10**100
googol_hours = googol // 60
googol_minutes = googol % 60

time = input("Vad är klockan nu? (Ange på formatet hh:mm)")

# Dela upp tiden i timmar och minuter (men vad händer om input är felaktig?)
hours, minutes = time.split(":")
hours = int(hours) 
minutes = int(minutes)

# Lägg till googol-minuter (men vad händer om det blir fler än 60?)
minutes += googol_minutes

# Behöver hantera timmar, men vad händer om timmar blir större än 24?
if minutes >= 60:
    hours += 1
    minutes -= 60

hours += googol_hours

# Behöver justera om timmarna (men vad händer om det blir mer än 24?)
# här skulle det behövas något för att hantera överskott i timmar

# Inte säker på att tiden formateras rätt
time_string = str(hours) + ":" + str(minutes)

print("Om en googol minuter är klockan", time_string)
