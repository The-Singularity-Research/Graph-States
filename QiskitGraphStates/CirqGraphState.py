import networkx as nx
import cirq


class QiskitGraphState():

    def __init__(self, graph):
        # super().__init__()
        assert isinstance(graph, nx.Graph) or isinstance(graph, nx.DiGraph), \
            ValueError("Graphs have to be networkx.Graph() or networkx.DiGraph()")
        self.graph = graph

        # Create a quantum register based on the number of nodes in G
        self.qubits = [cirq.NamedQubit(str(node)) for node in self.graph]
        self.circuit = cirq.Circuit()

        # For each vertex, apply a Hadamard gate
        for node in self.graph.nodes:
            self.circuit.append(cirq.H(cirq.NamedQubit(str(node))))

        # For each edge e={x,y} apply a controlled-Z gate on its vertices
        for x, y in self.graph.edges:
            self.circuit.append(cirq.CZ(cirq.NamedQubit(str(x)), cirq.NamedQubit(str(y))))

        # create a node dictionary from node to integer index of a qubit
        # in a Qiskit circuit
        self.node_dict = dict()
        for count, node in enumerate(self.graph.nodes):
            self.node_dict[node] = count

    def add_node(self):
        raise NotImplemented("Disallowed: don't expect to do this after you have the initial graph state")

    def x_measurement(self, qubit):
        """Measure 'qubit' in the X-basis
        :param qubit: a name to designate a cirq.NamedQubit(str(qubit))
        :return None
        """
        self.circuit.append(cirq.H(cirq.NamedQubit(str(qubit))))
        self.circuit.append(cirq.measure(cirq.NamedQubit(str(qubit))))
        self.circuit.append(cirq.H(cirq.NamedQubit(str(qubit))))

    def apply_stabilizer(self, node):
        """
        applies the stabilizer generator corresponding to node
        :param self:
        :param node: a node in self.graph
        """
        self.circuit.append(cirq.X(cirq.NamedQubit(str(node))))
        for neighbor in self.graph.neighbors(node):
            self.circuit.append(cirq.Z(cirq.NamedQubit(str(neighbor))))


    def __str__(self):
        return str(self.circuit.draw('text'))

    def __eq__(self, other):
        return nx.is_isomorphic(self.graph, other.graph)

    def __hash__(self):
        return hash((self.graph.nodes, self.graph.edges, self.circuit.width()))
