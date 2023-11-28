
from .GPS_class import GPS
from .Vector_class import Vector
import math as m
#from geopy import distance 
import geopy.distance

class avoidance_vectors():
    #Deklarerer startverdier for klassen
    def __init__(self, other, other_speed, other_bearing):
        
        #self.own = GPS()
        self.own = (60.3947, 5.2675) #Denne brukes ettersom dronen programmet ikke er koblet opp mot dronen enda og har dermed ikke GPS posisjon
        self.other = other
        self.other_speed = other_speed
        self.other_bearing = other_bearing
        self.distance = geopy.distance.distance(self.own, self.other)
        self.placeholder = GPS() # Kommer errormelding hvis denne er borte men brukes ikke til noe
        self.avoidance_vecs = []

        #self.relative = self.calc_bearing(self.own,self.other)


    # Call funksjonen som returnerer en liste med vektorer og distansene til punktene som vektorene regnes ut ifra
    def __call__(self, own, other, other_speed, other_bearing):
        
        aliases = self.create_aliases(other, other_speed, other_bearing)
        vec_tuple = self.make_avoid_vec(own,aliases)

        return vec_tuple
    
    #Regner ut relativ vinkel mellom to koordinater
    def calc_bearing(self, cordA, cordB):
        PointA = cordA
        PointB = cordB
        delta_lon =  PointB[1] - PointA[1]
        X = m.cos(PointB[0]*(m.pi/180))*m.sin(delta_lon*(m.pi/180))
        Y = m.cos(PointA[0]*(m.pi/180))*m.sin(PointB[0]*(m.pi/180))-m.sin(PointA[0]*(m.pi/180))*m.cos(PointB[0]*(m.pi/180))*m.cos(delta_lon*(m.pi/180))
        sigma = m.atan2(X,Y)
        bearing = m.degrees(sigma)
        return bearing
    # Regner ut distansen mellom to punkter
    def calc_distance(self, cord1, cord2):
        own = cord1
        other = cord2
        dist = geopy.distance.distance(own,other).km
        return dist 
    
    # Funksjon som regner ut aliaser
    def create_aliases(self, cord, speed, rel_angle):
   
        intervals = [60, 300, 600]
        la1 = cord[0]
        lo1 = cord[1]
        
        speed_mps = (speed * 1.852)*(5/18) #Konverter fra knop til meter per sekund
        distances = [i * speed_mps for i in intervals] 
        alias_list = []
        alias_list.append(cord) #Legger til original posisjon først i lista
        #Looper gjennom distanse lista for a regne ut posisjonen den vil tilsvare i koordinatsystemet 
        #Sidekommentar: gatt over til m.radians her grunnet jeg trodde det var en mate pa a fikse en feil, men feilen la et annet sted sa na tør jeg ikke endre det
        for dist in distances:
            a_d = (dist/1000) #/ 6371 #Angular distance,Gjør om distanse til km og så deler på joras radius i km
            """ 
            Gamle koden vi brukte for utregning av ny posisjon. Denne ble erstattet av geopy biblioteket sin funksjon. Denne var en del verre på posisjon
            la2 = la1 + m.asin(m.sin(m.radians(la1))*m.cos(a_d)+ m.cos(m.radians(la1))*m.sin(a_d)*m.cos(m.radians(rel_angle)))
            lo2 = lo1 + m.atan2(m.sin(m.radians(rel_angle))*m.sin(a_d)*m.cos(m.radians(la1)),m.cos(a_d)-m.sin(m.radians(la1))*m.sin(m.radians(la2)))
            la2_deg = m.degrees(la2)
            lo2_deg = m.degrees(lo2)
            """
            #Geopy funksjon som regner ut punktet man ender opp etter cord antall kilometer
            point = geopy.distance.distance(kilometers=a_d).destination(cord,rel_angle)
            #al_pos = (la2, lo2)
            alias_list.append(point)
        return alias_list
    
    #Funksjon som lager unnvikelsesvektorer
    def make_avoid_vec(self ,own_position, other_positions):
        angle_list = []
        vector_list = []
        distance_list = []
        #Funksjon som jobber gjennom alle aliasene og lager en vektor motsatt rettet av vinkelen til punktet
        for positions in other_positions:
            ang = self.calc_bearing(own_position,positions)
            al_dist = geopy.distance.distance(own_position,positions).km
            #For å passe på at vinkelen er i forhold til et kompass
            if ang < 0:
                ang = 360 + ang
            avoid_ang = ang + 180
            if avoid_ang > 360:
                avoid_ang = avoid_ang - 360
            else:
                avoid_ang = avoid_ang
            angle_list.append(avoid_ang)
            distance_list.append(al_dist)
        for i in range(len(angle_list)):
            vec = Vector(1/(i+1),angle_list[i]) # Lager vektorer der fremtidige posisjoner blir svakere vektet
            vector_list.append(vec)
        print(vector_list)
        return_arg = (vector_list,distance_list)
        
        return return_arg
    


