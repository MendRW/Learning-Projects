
import re
hand = open ('C:poedata.txt', 'r')
numlist = list()
num = 0
for line in hand:
    line = line.rstrip()
    essenceprice = re.findall ('^X-Deafening Essence of ([0-9.]+)', line)
    if len(essenceprice) !=1 : continue
    num = float(essenceprice[0])
    numlist.append(num)
    print(numlist)


essenceprice = 0

hand = open ('poedata.txt')
numlistjuice = list()
for line in hand:
    line = line.rstrip()
    juiceprice = re.findall ('^X-Primal Crystallised Lifeforce ([0-9.]+)',line)
    if len (juiceprice) !=1 :continue
    num= float(juiceprice)
    numlistjuice(num)
print(numlistjuice)
