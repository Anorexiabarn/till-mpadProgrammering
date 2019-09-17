# vaknar
vaken = "n"

print("Du sover djupt som björnen i ide...")

while vaken == "n":
    vaken = input("Vaknar du? [y/n] ").lower()

# duscha
print("Du masar dig upp och släpar dig in i duschen.")
print("Någon har lämnat en brödrost i din dusch...")
duscha = input("Flyttar du på brödrosten? [y/n] ").lower()

if duscha == "n":
    print("Du går in och sätter på duschen")
    print("Du dör och ser jesus av elchocken...")
    exit()

elif duscha == "y":
    print("Friskt vatten sköljer över dig och du börjar vakna till.")
else:
    print("DOES NOT COMPUTE")

# årstid
season = False
while season == False:
    season = input("VIlken årstid är det? [vår, vinter, sommar, höst]")
    if season == "vår" or season == "vinter" or season == "höst":
        print("Det är kallt som fan, fyfan, jag sjukanmäler mig")
        print("Du klär på dig vinterpälsen")
    elif season == "sommar":
        print("sommar! fan va skönt, nu behöver jag inte ta på alla kläder jag äger")
    else:
        season = False

