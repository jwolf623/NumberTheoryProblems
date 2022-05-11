phone_number = int(input())

areaCode=str(phone_number // 10000000)
firstThree=str((phone_number // 10000) % 1000)
Lastfour=str(phone_number % 10000)


print('({}) {}-{}'.format(areaCode,firstThree,Lastfour))
