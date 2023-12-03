"""
Dette programmet ble brukt til å simulere hvordan dronen ville reagert på en kontakt en kilometer unna på kryssende kurs


"""



from geopy import distance 
import math as m
from Behaviour.Behaviours.Classes.Vector_class import Vector 
from Behaviour.Behaviours.Classes.AIS_class import avoidance_vectors

# Simmulering av egen posisjon 
mylat = 60.3947
mylon = 5.2675 
buffer = 0.05
own_pos = (mylat,mylon)

# Simmulering av fartøy
other_lat = 60.39461
other_lon = 5.287204
speed = 7
course = 320
other_pos = (other_lat, other_lon)


tot_vector = Vector(0,0)
# Regner ut avstanden mellom 2 punkter. Brukes til å finne avstand til andre fartøyer


instsans = avoidance_vectors(other_pos, speed, course)
instans_vectors = instsans(own_pos,other_pos,speed,course)
#Henter ut de to listene som returneres
get_vec_list = instans_vectors[0]
get_distances = instans_vectors[1]

counter1 = 0
print("*"*80)
for vec in get_vec_list:
    r = get_distances[counter1]
    print(r)

    weight = (3/(m.pow(r,2)+0.25))
    temp_vec = vec * weight
    tot_vector += temp_vec
    counter1 += 1
print("*"*80)
print(tot_vector.magnitude)
print(tot_vector.angle)
vec_magn_string = str(tot_vector.magnitude)  
vec_ang_string = str(tot_vector.angle)
space = " "
tot_vector_string = vec_magn_string + space + vec_ang_string
print(tot_vector_string)
