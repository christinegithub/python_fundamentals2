# print("How far did person 1 run (in metres)?")
# distance1 = float(input())
# print("How long (in minutes) did person 1 run take to run {} metres?".format(distance1))
# mins1 = float(input())
#
# print("How far did person 2 run (in metres)?")
# distance2 = float(input())
# print("How long (in minutes) did person 2 run take to run {} metres?".format(distance2))
# mins2 = float(input())
#
# print("How far did person 3 run (in metres)?")
# distance3 = float(input())
# print("How long (in minutes) did person 3 run take to run {} metres?".format(distance3))
# mins3 = float(input())



participant = 1
mins = 1
secs = mins * 60
distance = 1

def speed(distance, secs):
    return distance / secs

while participant <= 3:
    print("How far did person {} run (in metres)?".format(participant))
    distance = float(input())
    print("How long (in minutes) did person {} run take to run {} metres?".format(participant, distance))
    mins = float(input())
    participant += 1
    print("The speed you ran is " + str(speed(distance, secs)))



#
# secs1 = mins1 * 60
# speed1 = distance1/secs1
# secs2 = mins2 * 60
# speed2 = distance2/secs2
# secs3 = mins3 * 60
# speed3 = distance3/secs3
#




# if speed3 > speed2 and speed3 > speed1:
#   print("Person 3 was the fastest at {} m/s".format(speed3))
# elif speed2 > speed3 and speed2 > speed1:
#   print("Person 2 was the fastest at {} m/s".format(speed2))
# elif speed1 > speed3 and speed1 > speed2:
#   print("Person 1 was the fastest at {} m/s".format(speed1))
# elif speed1 == speed2 and speed2 == speed3:
#   print("Everyone tied at {} m/s".format(speed1))
# else
#   print("Well done everyone!")
