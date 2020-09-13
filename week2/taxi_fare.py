#taxi_fare.py

def taxi_fare_calc(km):
    ''''Calculates the taxi fare,
    the base fare is 4 $ and for every 140 m
    traveled another 0.25 $ would be added )
    '''
    base_fare = 4.00
    meters_fare = 0.25/140
    distance_meter = km * 1000
    fare = distance_meter * meters_fare + base_fare
    return fare
