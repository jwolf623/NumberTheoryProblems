def Tot_M(LST):
    T_medals = sum(LST)
    return T_medals

def g_medals(LST):
    for country in world:
        return [item[0] for item in LST]

def tm_greatest(tm_world):                   #This works
    total=0
    for value in tm_world:
        if total < value:
            total = value

    return total

GRB = [29, 17, 19]
CHN = [38, 28, 22]
RUS = [24, 25, 32]
US = [46, 28, 29]
KOR = [13, 8, 7]
JPN = [7, 14, 17]
GER = [11, 11, 14]
world = [GRB, CHN, RUS, US, KOR, JPN, GER]

tm_GRB=Tot_M(GRB)
tm_CHN=Tot_M(CHN)
tm_RUS=Tot_M(RUS)
tm_US=Tot_M(US)
tm_KOR=Tot_M(KOR)
tm_JPN=Tot_M(JPN)
tm_GER=Tot_M(GER)
tm_world = [Tot_M(GRB),Tot_M(CHN),Tot_M(RUS),Tot_M(US),Tot_M(KOR),Tot_M(JPN),Tot_M(GER)]


print('GRB, CHN, RUS, US, KOR, JPN, GER received', end='')
print(g_medals(world), 'gold medals and won' ,tm_world, 'total medals respectively.')
print('The United States won the most medals overall with', tm_greatest(tm_world),'total medals.')
print('The United States won the most gold medals with',US[0],'medals.')
print('Japan was the country who won the smallest amount of gold medals with',JPN[0],'medals.')
