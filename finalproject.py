import sys
import os

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

        self.graph = [[0 for column in range(nodes)] for rows in range(nodes)] 

        self.node_names = {

        }

    def add_node(self, name: str) -> None:
        while True:
            if name not in self.node_names:
                self.node_names[name] = len(self.node_names)
                break
            else:
                print("Node already exists.")
                continue
        return name

    def add_edge(self, point_a, point_b, distance: float) -> None:
        while True:
            if point_a in self.node_names and point_b in self.node_names:
                point_a_index = self.node_names[point_a]
                point_b_index = self.node_names[point_b]
                self.graph[point_a_index][point_b_index] = distance
                self.graph[point_b_index][point_a_index] = distance
                break
            else:
                print("One or more nodes are not registered!")
                continue

    def path_find(self, point_a, point_b):
        point_a_index = self.node_names.get(point_a)
        point_b_index = self.node_names.get(point_b)
        distances = [sys.maxsize] * self.nodes
        distances[point_a_index] = 0
        visited = [False] * self.nodes
        previous = [-1] * self.nodes
        for _ in range(self.nodes):
            minimum_distance = sys.maxsize
            for i in range(self.nodes):
                if distances[i] < minimum_distance and not visited[i]:
                    minimum_distance = distances[i]
                    minimum_index = i
            visited[minimum_index] = True
            for i in range(self.nodes):
                if self.graph[minimum_index][i] > 0 and not visited[i] and distances[i] > distances[minimum_index] + self.graph[minimum_index][i]:
                    distances[i] = distances[minimum_index] + self.graph[minimum_index][i]
                    previous[i] = minimum_index
        path = self.walk(previous, point_a_index, point_b_index)
        self.print_result(point_a, point_b, distances[point_b_index], path)

    def walk(self, previous, point_a_index, point_b_index) -> list:

        path = []
        cur = point_b_index

        while cur != point_a_index:
            if cur == -1:
                return []
            path.insert(0, cur)
            cur = previous[cur]

        path.insert(0, point_a_index)

        return path
    
    def print_result(self, point_a, point_b, distance, path):
        if not path:
            print(f"No path exists from {point_a} to {point_b}.")
            return
        path_names = [list(self.node_names.keys())[list(self.node_names.values()).index(i)] for i in path]

        path_str = " -> ".join(path_names)

        print(f"The shortest path from {point_a} to {point_b} is {distance} unit(s).")
        print(f"Path: {path_str}")

graph = Graph(19)

seattle = graph.add_node("Seattle")
los_angeles = graph.add_node("Los Angeles")
denver = graph.add_node("Denver")
austin = graph.add_node("Austin")
nashville = graph.add_node("Nashville")
evansville = graph.add_node("Evansville")
chicago = graph.add_node("Chicago")
toledo = graph.add_node("Toledo")
boston = graph.add_node("Boston")

graph.add_edge("Seattle", "Los Angeles", 40)
graph.add_edge("Los Angeles", "Denver", 25)
graph.add_edge("Denver", "Austin", 10)
graph.add_edge("Austin","Nashville", 15)
graph.add_edge("Nashville", "Evansville", 10)
graph.add_edge("Evansville","Chicago", 20)
graph.add_edge("Nashville", "Chicago", 30)
graph.add_edge("Chicago", "Toledo", 10)
graph.add_edge("Chicago", "Boston", 30)
graph.add_edge("Toledo", "Boston", 20)

node_count = 9

cities = [seattle, los_angeles, denver, austin, nashville, evansville, chicago, toledo, boston]

print(f"The database has the following cities by default:")
for city in cities:
    print(city)
    
while True:

    user_input = int(input("Would you like to add nodes (0), add edges (1), or pathfind (2)? "))

    if user_input == 0:

        user_input_one = input(f"Begin adding new cities? Y / N ")
        while True:
            if user_input_one.upper() == "Y":
                os.system("cls")

                print(f"Number of Cities by Default: {node_count} | MAX: 19")

                while node_count < graph.nodes:
                    new_city = input(f"Add City #{node_count+1} ")
                    new_city_node = graph.add_node(new_city)
                    cities.append(new_city_node)
                    node_count +=1
                
                break
                
            elif user_input_one.upper() == "N":
                break
            else:
                print("Invalid Response")

            break

    elif user_input == 1:

        edge_count = 10
        while True:

            print("================================================")
            user_input_two = input("Begin adding edges between new cities? Y / N ")
            if user_input_two.upper() == "Y":
                os.system("cls")

                print(f"Number of Edges by Default: {edge_count} | MAX: 16")

                while edge_count < 16:
                    print(f"Add Edge #{edge_count+1}")
                    new_edge_city_a = input("Enter City A: ")
                    new_edge_city_b = input("Enter City B: ")
                    distance = float(input("Enter Distance between City A and City B: "))
                    new_edge = graph.add_edge(new_edge_city_a, new_edge_city_b, distance)
                    edge_count +=1
                
                break
                
            elif user_input_two.upper() == "N":
                print("Program Closed.")
                break
            else:
                print("Invalid Response")

            break

    elif user_input == 2:

        cities = str(cities)
        print("All cities:")
        print(cities.replace("'[] ", ""))

        while True:
            print("Find distance between City A and City B:")
            city_a = input("Enter City A: ")
            city_b = input("Enter City B: ")
            info = print(f"Information Entered: \nCity A: {city_a} \nCity B: {city_b}")
            conf_input = input("Continue? Y / N ")
            if conf_input.upper() == "Y":
                os.system("cls")
                graph.path_find(city_a, city_b)
                break
            elif conf_input.upper() == "N":
                break
            else:
                print("Invalid Response")
            break
        break



            




    
















