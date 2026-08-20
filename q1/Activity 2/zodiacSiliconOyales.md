![Working demo of python code](image.png)
![Invalid birth year](image-1.png)

# source code

#Greets user and states program purpose
print("Greetings user welcome to Chinese zodiac identifier")

#list of zodiacs
zodiacs = ["Rat (鼠 / Shǔ)","Ox (牛 / Niú)","Tiger (虎 / Hǔ)","Rabbit (兔 / Tù)","Dragon (龙 / Lóng)","Snake (蛇 / Shé)","Horse (马 / Mǎ)","Goat (羊 / Yáng)","Monkey (猴 / Hóu)","RoosterRooster (鸡 / Jī)","Dog (狗 / Gǒu)","Pig (猪 / Zhū)"]

#Gets Birth year from user
birthyear = int(input("Input Birth year: "))
if birthyear < 1900:
    print("Invalid Year, it should not be earlier than 1900")
    exit()
else:
    #Calculates zodiac
    userzodiacp1 = (birthyear - 4) % 12
    userzodiactrue = zodiacs[userzodiacp1]
    #prints zodiac
    print(userzodiactrue)

# Valid:
Greetings user welcome to Chinese zodiac identifier
Input Birth year: 2011
Rabbit (兔 / Tù)

# Invalid
Greetings user welcome to Chinese zodiac identifier
Input Birth year: 1700
Invalid Year, it should not be earlier than 1900