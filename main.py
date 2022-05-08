from FlightRadar24.api import FlightRadar24API
import json
fr_api = FlightRadar24API()

zones = fr_api.get_zones()


# bounds = fr_api.get_bounds(zones['europe']['subzones']['uk']['subzones']['london'])
flightFound = False
y1=51.48
y2=51.38
x1=-0.1
x2=-0.03
itt = 0

while flightFound == False:
    london_bounds = str(y1)+","+str(y2)+","+str(x1)+","+str(x2)
    print("Iteration: "+ str(itt))
    flights = fr_api.get_flights(bounds = london_bounds)



    for flight in flights:
        if flight.ground_speed > 100 and flight.altitude >500:
            template = "\"aircraft\":\"{}\",\"registration\":\"{}\",\"altitude\":\"{}\",\"ground_speed\":\"{}\",\"heading\":\"{}\",\"latitude\":\"{}\",\"longitude\":\"{}\"\,\"origin_airport\":\"{},\"dest_airpot\":\"{}\""
            tempTemplate = template.format(flight.aircraft_code, flight.registration, flight.altitude, flight.ground_speed, flight.heading, flight.latitude, flight.longitude, flight.origin_airport_iata, flight.destination_airport_iata)
            flightFound = True
            flightDetails =  fr_api.get_flight_details(flight.id)
            # for key, value in flightDetails.items() :
            #     print (key)
            flightSummary = {}
            flightSummary["modelName"] = flightDetails["aircraft"]["model"]["text"]
            flightSummary["originFullName"] = flightDetails["airport"]["origin"]["name"]
            
            if flightDetails["airport"]["destination"] == "None":
                flightSummary["destinationFullName"] = "NA"
            else:
                flightSummary["destinationFullName"] = flightDetails["airport"]["destination"]["name"]
                
            flightSummary["destinationFullName"] = flightDetails["airport"]["destination"]["name"]
            flightSummary["destinationFullName"] = flightDetails["airport"]["destination"]["name"]
            flightSummary["altitude"] = flight.altitude
            flightSummary["groundSpeed"] = flight.ground_speed
            flightSummary["heading"] = flight.heading

            # print((flightSummary))
            for key, value in flightSummary.items() :
                print (key, value)
        

    if flightFound == False:
        y1=y1+0.05
        y2=y2-0.05
        x1=x1-0.05
        x2=x2+0.05
        itt +=1
