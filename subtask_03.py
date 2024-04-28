from collections import defaultdict, deque


def minimal_travel_time_with_capacity(flights, origin, destination, group_size):
    # Check if the origin and destination have exactly three capital letters
    if not (origin.isalpha() and origin.isupper() and len(origin) == 3):
        raise ValueError("Origin must be a 3-letter code in all uppercase.")
    if not (destination.isalpha() and destination.isupper() and len(destination) == 3):
        raise ValueError("Destination must be a 3-letter code in all uppercase.")

    # Construct a graph from the list of flights with capacities
    graph = defaultdict(list)
    capacity = defaultdict(int)
    for flight in flights:
        src, dest, cap = flight.split(',')
        if not (src.isalpha() and src.isupper() and len(src) == 3):
            raise ValueError("Invalid city code: {}".format(src))
        if not (dest.isalpha() and dest.isupper() and len(dest) == 3):
            raise ValueError("Invalid city code: {}".format(dest))
        try:
            cap = int(cap)  # Convert capacity to integer
            if cap < 0:  # Ensure non-negative capacity
                raise ValueError("Capacity must be non-negative.")
        except ValueError:
            raise ValueError("Invalid capacity: {}".format(cap))
        graph[src].append(dest)
        capacity[(src, dest)] = cap

    # Initialize a queue for BFS, a set to track visited cities, and a dictionary to track remaining capacity
    queue = deque([(origin, 0, group_size)])
    visited = set()

    while queue:
        city, time, remaining_capacity = queue.popleft()

        # Check if the destination is reached with the entire group
        if city == destination and remaining_capacity >= 0:
            return time

        # Explore neighboring cities
        for neighbor in graph[city]:
            if neighbor not in visited and capacity[(city, neighbor)] >= remaining_capacity:
                queue.append((neighbor, time + 1, remaining_capacity))
                visited.add(neighbor)

    # If destination is unreachable
    return 0


# Example 1
flights1 = ["SOF,MLE,2", "SOF,LON,3", "LON,MLE,4"]
origin1 = "SOF"
destination1 = "MLE"
group_size = 3
print(minimal_travel_time_with_capacity(flights1, origin1, destination1, group_size))  # Output: 2



