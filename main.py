import os
import re
import time
import random


def read_file(filename):
    nodes = []
    with open(filename) as f:
        lines = f.readlines()
    for idx, i in enumerate(lines):
        value = i.replace('\n', '')
        nodes.append(Node(value, idx))

    paths = [[Path(0, 1) for _ in range(len(nodes))] for _ in range(len(nodes))]

    return nodes, paths


def set_lengths(nodes, paths):
    for y, node_y in enumerate(nodes):
        for x, node_x in enumerate(nodes):
            if x != y:
                value = node_y.set_distance(node_x)
                paths[y][x].length = value
    return paths


class Ant:
    def __init__(self, max_words, start):
        self.max_words = max_words
        self.current = start
        self.road = []
        self.result = 1
        self.running = True

    def travel_road(self, paths, nodes):
        global best_result
        global best_path
        while self.running:
            potential_nodes = []
            self.road.append(self.current)
            for i in nodes:
                if i == self.current:
                    continue
                if self.current.get_path(i, paths).length <= self.max_words and i not in self.road:
                    potential_nodes.append(i)
            if not potential_nodes:
                self.running = False
            if not self.running:
                break
            possibilities = [
                pow(self.current.get_path(i, paths).pheromone, alfa) / pow(self.current.get_path(i, paths).length, beta)
                for i in potential_nodes]
            choice = random.choices(potential_nodes, possibilities)[0]
            self.result += 1
            self.max_words -= self.current.get_path(choice, paths).length
            self.current = choice

        prev_node = None
        for temporary_node in potential_nodes:
            if prev_node is None:
                prev_node = temporary_node
                continue
            temporary_path = temporary_node.get_path(prev_node, paths)
            temporary_path.add_pheromone(self.result)
            prev_node = temporary_node

        if self.result >= best_result and n - len(self.road) <= n - len(best_path):
            best_path = self.road
            best_result = self.result


class AntColony:
    def __init__(self, ants, iteration):
        self.iteration = iteration
        self.ants = ants

    def launch(self, paths, nodes):
        for i in range(self.iteration):
            print("iteration:", i + 1)
            for ant in range(self.ants):
                # print("ant:", ant + 1)
                temp = Ant(n, nodes[random.randint(0, len(nodes) - 1)])
                temp.travel_road(paths, nodes)
            self.release_pheromones(paths)

    def release_pheromones(self, paths):
        for path in paths:
            for x in path:
                x.evaporate_pheromone()


class Node:
    def __init__(self, value, id):
        self.value = value
        self.id = id

    def set_distance(self, other):
        for i in range(len(self.value)):
            if self.value[i:] == other.value[:len(other.value) - i]:
                return i
        return len(self.value)

    def get_path(self, other, paths):
        return paths[self.id][other.id]

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class Path:
    def __init__(self, length, pheromone):
        self.length = length
        self.pheromone = pheromone

    def evaporate_pheromone(self):
        self.pheromone *= (1 / p)

    def add_pheromone(self, result):
        self.pheromone += result * Q

    def __str__(self):
        return str(self.length, self.pheromone)

    def __repr__(self):
        return str(self.length, self.pheromone)

if __name__ == "__main__":
    folder_list = ['los_neg', 'los_poz', 'pow_neg', 'poz_kon_olig']

    p = 0.7  # скорость испарения феромонов
    Q = 0.7  # константа добавления феромонов
    alfa = 1  # значемость феромонов
    beta = 5  # значемость расстояния
    ants_number = 30
    iterations_number = 40
    
    for folder in folder_list:
        for file in os.listdir(f'input/{folder}/'):
            best_path = []
            best_result = 0
            print(file)

            n = int(''.join(re.findall("\.(.*)[-+]", file))) + 9
            print(n)

            nodes, paths = read_file(f'input/{folder}/{file}')

            # заносит "расстояние"(похожесть) каждого элемента (node) со всеми другими в paths
            set_lengths(nodes, paths)

            start_time = time.time()

            colony = AntColony(ants_number, iterations_number)
            colony.launch(paths, nodes)

            final_length = sum(node.get_path(best_path[i + 1], paths).length for i, node in enumerate(best_path[:-1]))
  
            end_time = time.time()
            execution_time = end_time - start_time
            
            print("Final length:", final_length)
            print("Number of words:", len(best_path))
            print("Execution time:", execution_time, "seconds")
            print("Best road:", best_path)

            with open(f"output/{folder}/{file}", "w") as f:
                f.write("Final length: " + str(final_length) + '\n')
                f.write("Number of words:" + str(len(best_path))+'\n')
                f.write("Execution time:" + str(execution_time) + "seconds" + '\n')
                f.write("Best road: " + str(best_path) + '\n')
                f.write("p:" + str(p) + '\n')
                f.write("Q:" + str(Q) + '\n')
                f.write("alfa:" + str(alfa) + '\n')
                f.write("beta:" + str(beta) + '\n')
                f.write("ants number:" + str(ants_number) + '\n')
                f.write("iterations number:" + str(iterations_number) + '\n')