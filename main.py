import heapq

def find_min_hotel_stays(n, hotels, roads):
  INF = float('inf')
  max_driving_time = 600
  hotel_set = set(hotels)
  graph = {i: [] for i in range(1, n + 1)}
  for a, b, t in roads:
    graph[a].append((b, t))
    graph[b].append((a, t))
  dist = {i: INF for i in range(1, n + 1)}
  dist[1] = 0
  pq = [(0, 1, 0)]
  heapq.heapify(pq)
  while pq:
    time, city, hotel_stays = heapq.heappop(pq)
    if city in hotel_set:
      hotel_stays += 1
      time = 0
    if city == n:
      return hotel_stays-1
    for neighbor, road_time in graph[city]:
      new_time = time + road_time
      if new_time <= max_driving_time and new_time < dist[neighbor]:
        dist[neighbor] = new_time
        heapq.heappush(pq, (new_time, neighbor, hotel_stays))
  return -1

test_cases = [
    # Test Case 1 ostad
    (6, [2, 5, 3], [
        (1, 2, 400), (3, 2, 80), (3, 4, 301), (4, 5, 290), (5, 6, 139),
        (1, 3, 375), (2, 5, 462), (4, 6, 300)
    ]),
    # Test Case 2
    (5, [3, 2], [
        (1, 2, 400), (1, 3, 350), (2, 3, 200), (2, 4, 300), (3, 4, 500),
        (4, 5, 200)
    ]),
    # Test Case 3 ostad
    (3, [0], [
        (1, 2, 371), (2, 3, 230)
    ]),
    # Test Case 4
    (7, [2, 3, 5], [
        (1, 2, 400), (1, 3, 300), (2, 4, 200), (2, 5, 150), (3, 4, 350),
        (3, 6, 400), (4, 5, 250), (4, 6, 300), (5, 6, 100), (5, 7, 200)
    ]),
    # Test Case 5
    (8, [2, 4, 7], [
        (1, 2, 300), (1, 3, 200), (2, 4, 400), (2, 5, 500), (3, 4, 350),
        (3, 6, 250), (4, 5, 100), (4, 6, 300), (4, 7, 200), (5, 6, 400),
        (6, 7, 150), (6, 8, 200)
    ])
]
choice = input("Choose (1) User Input or (2) Run Test Cases: ")
if choice == "1":
  n = int(input("Enter the number of cities: "))
  hotels = [int(x) for x in input("Enter the list of hotel city indices (separated by spaces): ").split()]
  num_roads = int(input("Enter the number of roads: "))
  roads = []
  for _ in range(num_roads):
    a, b, t = map(int, input("Enter road details (starting city, ending city, travel time): ").split())
    roads.append((a, b, t))
  result = find_min_hotel_stays(n, hotels, roads)
  print(f"Minimum hotel stays: {result}")
elif choice == "2":
  for n, hotels, roads in test_cases:
    result = find_min_hotel_stays(n, hotels, roads)
    print(f"Test Case: n = {n}, hotels = {hotels}, roads = {roads}")
    print(f"Minimum hotel stays: {result}")
    print()
else:
  print("Invalid choice!")
