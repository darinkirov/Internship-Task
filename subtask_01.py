from collections import defaultdict, deque


def minimal_travel_time(flights, origin, destination):
    # Check if the origin and destination have exactly three capital letters
    if not (origin.isalpha() and origin.isupper() and len(origin) == 3):
        raise ValueError("Origin must be a 3-letter code in all uppercase.")
    if not (destination.isalpha() and destination.isupper() and len(destination) == 3):
        raise ValueError("Destination must be a 3-letter code in all uppercase.")

    # Construct a graph from the list of flights
    graph = defaultdict(list)
    for flight in flights:
        src, dest = flight.split(',')
        if not (src.isalpha() and src.isupper() and len(src) == 3):
            raise ValueError("Invalid city code: {}".format(src))
        if not (dest.isalpha() and dest.isupper() and len(dest) == 3):
            raise ValueError("Invalid city code: {}".format(dest))
        graph[src].append(dest)

    # Initialize a queue for BFS and a set to track visited cities
    queue = deque([(origin, 0)])
    visited = set()

    while queue:
        city, time = queue.popleft()

        # Check if the destination is reached
        if city == destination:
            return time

        # Explore neighboring cities
        for neighbor in graph[city]:
            if neighbor not in visited:
                queue.append((neighbor, time + 1))
                visited.add(neighbor)

    # If destination is unreachable
    return 0


# Example 1
flights1 = ["SOF,IST", "IST,CMB", "CMB,MLE"]
origin1 = "SOF"
destination1 = "MLE"
print(minimal_travel_time(flights1, origin1, destination1))  # Output: 3

# Example 2
flights2 = ["SOF,MLE", "SOF,LON", "LON,MLE"]
origin2 = "SOF"
destination2 = "MLE"
print(minimal_travel_time(flights2, origin2, destination2))  # Output: 1

# Example 3
flights3 = ["SOF,LON", "SOF,NYC"]
origin3 = "SOF"
destination3 = "MLE"
print(minimal_travel_time(flights3, origin3, destination3))  # Output: 0
