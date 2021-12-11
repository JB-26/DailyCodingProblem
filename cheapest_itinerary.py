# THE PROBLEM
# You are given a huge list of airline ticket prices between cities around the world on a given day.
# These are all direct flights
# Each element in the list has the format (source_city, destination, price)
# Consider a user who is willing to take up k connections to get from their origin city A to destination B.
# Find the cheapest fare possible for this journey and print the itinerary.

# For example, a traveler wants to go from JFK to LAX with up to 3 connections, with the following input

# [
    # ('JFK', 'ATL', 150),
    # ('ATL', 'SFO', 400),
    # ('ORD', 'LAX', 200),
    # ('LAX', 'DFW', 80),
    # ('JFK', 'HKG', 800).
    # ('ATL', 'ORD', 90),
    # ('JFK', 'LAX', 500 )
# ]

# This would return JFK -> ATL -> ORD -> LAX, costing 440

# import libraries
import heapq

from collections import defaultdict

# create list of flights (tuples)
flights = [('JFK', 'ATL', 150), ('ATL', 'SFO', 400), ('ORD', 'LAX', 200), ('LAX', 'DFW', 80), ('JFK', 'HKG', 800), ('ATL', 'ORD', 90), ('JFK', 'LAX', 500 )]

def get_itinerary(flights, source, destination, k):
    """
    Returns the cheapest fare possible for a given journey
    """

    #create new dictionary
    prices = defaultdict(dict)

    #creates dictionary of nested dictionaries
    #the source of the flight while the key is the dictionary of the destination and price
    for u, v, cost in flights:
        prices[u][v] = cost
    
    path = [source]

    heap = [(0, source, k + 1, path)]

    #total cost for flight
    total_cost = 0

    #unordered collection of unique items
    visited = set()

    print(f"Flights for today:\n")
    for a, b, c in flights:
        print(f"Source: {a} Destination: {b} Cost: {c}")

    print(f"The start of the journey is {source}")

    print(f"The destination is {destination}")

    print(f"The maximum ammount of connections is {k}")

    print("Now finding journey...")

    while heap:
        visited.add(u)
        #pops the smallest item from the heap
        cost, u, k, path = heapq.heappop(heap)



get_itinerary(flights, 'JFK', 'LAX', 3)
