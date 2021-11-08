def flights(*args):
    flights_dict = {}
    for i in range(0, len(args),2):
        if (args[i] or args[i + 1]) == 'Finish':
            return flights_dict


        destination = args[i]
        passengers = args[i + 1]
        if not destination in flights_dict:
            flights_dict[destination] = 0
        flights_dict[destination] += passengers

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))