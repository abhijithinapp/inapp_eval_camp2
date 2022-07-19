#Personality using else-if
dobMonth = int(input("enter dob month: "))
birthStone = ""
personality = ""
if dobMonth == 1:
    birthStone = "Garnet"
    personality = "People born in January are bold and alert."
elif dobMonth == 2:
    birthStone = "Amethyst"
    personality = "People born in February are lucky and loyal."
elif dobMonth == 3:
    birthStone = "Aquamarine"
    personality = "People born in March are naughty and Genius."
elif dobMonth == 4:
    birthStone = "Diamond"
    personality = "People born in April are caring and strong."
elif dobMonth == 5:
    birthStone = "Emerald"
    personality = "People born in May are loving and practical."
elif dobMonth == 6:
    birthStone = "Alexandrite"
    personality = "People born in June are romantic and Curious."
elif dobMonth == 7:
    birthStone = "Ruby"
    personality = "People born in July are adventurous and honest."
elif dobMonth == 8:
    birthStone = "Peridot"
    personality = "People born in August are active and hardworking."
elif dobMonth == 9:
    birthStone = "Sapphire"
    personality = " People born in September are sensitive and pretty."
elif dobMonth == 10:
    birthStone = "Tourmaline"
    personality = " People born in October are stylish and friendly."
elif dobMonth == 11:
    birthStone = "Citrine"
    personality = " People born in November are nice and creative."
elif dobMonth == 12:
    birthStone = "Zyrcon"
    personality = " People born in December are confident and freedom loving."
else:
    print("month does not exist")

if dobMonth <=12:
    print("""
Printed using if-else
Birthstone: %s
Personality: %s """ %(birthStone,personality))

def definebirthstone(dobMonth):
    match dobMonth:
        case 1:
            birthStone = "Garnet"
            personality = "People born in January are bold and alert."
        case 2:
            birthStone = "Amethyst"
            personality = "People born in February are lucky and loyal."
        case 3:
            birthStone = "Aquamarine"
            personality = "People born in March are naughty and Genius."
        case 4:
            birthStone = "Diamond"
            personality = "People born in April are caring and strong."
        case 5:
            birthStone = "Emerald"
            personality = "People born in May are loving and practical."
        case 6:
            birthStone = "Alexandrite"
            personality = "People born in June are romantic and Curious."
        case 7:
            birthStone = "Ruby"
            personality = "People born in July are adventurous and honest."
        case 8:
            birthStone = "Peridot"
            personality = "People born in August are active and hardworking."
        case 9:
            birthStone = "Sapphire"
            personality = " People born in September are sensitive and pretty."
        case 10:
            birthStone = "Tourmaline"
            personality = " People born in October are stylish and friendly."
        case 11:
            birthStone = "Citrine"
            personality = " People born in November are nice and creative."
        case 12:
            birthStone = "Zyrcon"
            personality = " People born in December are confident and freedom loving."
        case _:
            print("month does not exist")

if dobMonth <=12:
    print("""
Printed using switch case
Birthstone: %s
Personality: %s """ %(birthStone,personality))
