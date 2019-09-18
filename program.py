# vaknar
vaken = "n"
# skapar en strängvariabel med värdet "n"
print("Du sover djupt som björnen i ide...")
# använder funktionen print för att skriva ut

while vaken == "n":
    # När vaken är då "n" så loopar den tillbaka tills du skriver "y"
    vaken = input("Vaknar du? [y/n] ").lower()

# duscha
print("Du masar dig upp och släpar dig in i duschen.")
print("Någon har lämnat en brödrost i din dusch...")
duscha = input("Flyttar du på brödrosten? [y/n] ").lower()

if duscha == "n":
    print("Du går in och sätter på duschen")
    print("Du dör och ser jesus av elchocken...")
    exit()
    # Om du svarar "n" så dör du
elif duscha == "y":
    print("Friskt vatten sköljer över dig och du börjar vakna till.")
    # Om svaret är "y" så bryts loopen och scriptet fortsätter
else:
    print("DOES NOT COMPUTE")
    # fortsätter loopen tills scriptet får ett giltigt svar

# årstid
season = False
# Gör en season variabel till False
while season == False:
    season = input("VIlken årstid är det? [vår, vinter, sommar, höst]")
    # Skapar en loop tills du väljer en årstid
    if season == "vår" or season == "vinter" or season == "höst":
        print("Det är kallt som fan, fyfan, jag sjukanmäler mig")
        print("Du klär på dig vinterpälsen")
        # skriver ut en text för de årstider du valt
    elif season == "sommar":
        print("sommar! fan va skönt, nu behöver jag inte ta på alla kläder jag äger")
        # skriver ut en text för de årstid du valt
    else:
        season = False
        # Fortsätter loopen tills scripten får ett giltigt svar

skola = "n"

skola = input("Ska du fara till skolan idag? [y/n] ").lower()
   
if skola == "n":
    print("Du fake hostar eller något")
    print("Du Sjukanmäler dig för due tjock")
    exit()
    
    # Om du svarar "n" så blir du sjuk
elif skola == "y":
    print("Du går till bussen och åker till skolan.")
    # Om svaret är "y" så far du till skola


