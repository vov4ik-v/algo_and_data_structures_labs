class DisjointSet:
    def __init__(self, size):
        self.parent = [x for x in range(size)]
        self.rank = [0] * size

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex_in_row, vertex_in_col):
        root_for_first_vertex = self.find(vertex_in_row)
        root_for_second_vertex = self.find(vertex_in_col)

        if root_for_first_vertex != root_for_second_vertex:
            if self.rank[root_for_first_vertex] < self.rank[root_for_second_vertex]:
                self.parent[root_for_first_vertex] = root_for_second_vertex
            elif self.rank[root_for_first_vertex] > self.rank[root_for_second_vertex]:
                self.parent[root_for_second_vertex] = root_for_first_vertex
            else:
                self.parent[root_for_second_vertex] = root_for_first_vertex
                self.rank[root_for_first_vertex] += 1


def matrix_of_graph_to_sorted_dict(graph):
    num_vertexes = len(graph[0])
    if len(graph) != 0:
        dict_of_edges = []
        for vertex_in_row in range(num_vertexes):
            for vertex_in_col in range(vertex_in_row + 1, num_vertexes):
                if graph[vertex_in_row][vertex_in_col] != 0:
                    dict_of_edges.append((vertex_in_row, vertex_in_col, graph[vertex_in_row][vertex_in_col]))
        dict_of_edges.sort(key=lambda x: x[2])
        return dict_of_edges
    else:
        return []


def find_min_len_cable(dict_of_edges, disjoint_set):
    sum_of_weights = 0
    for edge in dict_of_edges:
        vertex1, vertex2, weight = edge
        if disjoint_set.find(vertex1) != disjoint_set.find(vertex2):
            disjoint_set.union(vertex1, vertex2)
            sum_of_weights += weight
    return sum_of_weights


def find_min_len_cable_in_the_island(file_input,file_output):
    graph = read_input_file(file_input)
    if not graph:
        write_to_output_file(file_output,"Graph is empty")
        return None
    num_vertexes = len(graph[0])
    sorted_dict = matrix_of_graph_to_sorted_dict(graph)
    disjoint_set = DisjointSet(num_vertexes)
    len_cable = find_min_len_cable(sorted_dict, disjoint_set)
    write_to_output_file(file_output,len_cable)


def read_input_file(file_name):
    input_matrix = []
    with open(file_name, "r") as file:
        for line in file:
            row = list(map(int, line.split(",")))
            input_matrix.append(row)
    file.close()
    return input_matrix


def write_to_output_file(file_name, value):
    with open(file_name, "w") as file:
        file.write(str(value))
    file.close()
    return file


if __name__ == '__main__':
    find_min_len_cable_in_the_island('../resources/islands_empty.csv','../resources/islands_empty.out')

