#!/usr/bin/env python

import numpy as np
import time as tm
from datetime import datetime, date, time


def picoyplaca(inputdayofweek, inputhour, lastplatenumber):
    time1rest1=time(7,0,0)
    time1rest2=time(9,30,0)
    time2rest1=time(16,0,0)
    time2rest2=time(19,30,0)
    if (inputhour>=time1rest1 and inputhour<=time1rest2) or (inputhour>=time2rest1 and inputhour<=time2rest2):
        if inputdayofweek==0 and (lastplatenumber==1 or lastplatenumber==2):
            return False
        elif inputdayofweek==1 and (lastplatenumber==3 or lastplatenumber==4):
            return False
        elif inputdayofweek==2 and (lastplatenumber==5 or lastplatenumber==6):
            return False
        elif inputdayofweek==3 and (lastplatenumber==7 or lastplatenumber==8):
            return False
        elif inputdayofweek==4 and (lastplatenumber==9 or lastplatenumber==0):
            return False
        else: return True 
    else: return True




#Check the date is correct
def validateDate(dates):
    for format in ['%d/%m/%Y', '%d/%m/%y']:
        try:
            result = tm.strptime(dates, format)
            return True
        except:
            pass
    return False


#Check the hour is correct 
def validateHour(hour):
    for format in ['%H:%M:%S']:
        try:
            result = tm.strptime(hour, format)
            return True
        except:
            pass
    return False



if __name__ == '__main__':
    import sys
    #print help_message
    plate_value= False
    date_value= False
    hour_value= False
    

    while True:
        print "PICO Y PLACA CHECK \n" 
        print " Ingrese el numero de placa como consta en su especie de matricula Ej:AAA0123"
        print " Ingrese la fecha y la hora en el formato que se especifican"

        while plate_value==False:

            plate= raw_input(" Ingrese placa del vehiculo: ")
            if len(plate)==7 and plate[3:].isdigit()==True and plate[0:3].isupper()==True: #Check the plate is correct
                plate_value= True
            else: print("\t Ingreso de placa invalido")
    
        while date_value==False:
            dates= raw_input(" Ingrese fecha (dd/mm/aaaa): ")
            date_value=validateDate(dates)
            if date_value==True:
                break
            else: print("\t Ingreso fecha invalido")
    
    
        while hour_value==False:
            hours= raw_input(" Ingrese hora (hh:mm:ss): ")
            hour_value=validateHour(hours)
            if hour_value==True:
                break
            else: print("\t Ingreso de hora invalido")
    
               
        new_date=date(int(dates[6:]), int(dates[3:5]), int(dates[0:2]))  
        new_hour=time(int(hours[0:2]), int(hours[3:5]), int(hours[6:]))  
        dayofweek=datetime.weekday(new_date) #Zeller congruence to compute the day
        action=picoyplaca(dayofweek, new_hour, int(plate[6]))
        if action is True:
            print "El vehiculo de placas "+plate +" SI puede circular" 
        else:
            print "El vehiculo de placas "+plate +" NO puede circular"  
            
    
        ch=raw_input("Nueva consulta? s/n ")        
        if ch=="n" or ch=="N":
            break
        elif ch=="s" or ch=="S": 
            plate_value= False
            date_value= False
            hour_value= False
            continue 
        else:
            print("Error: Hasta pronto")
            break    
