import networkx as nx
from networkx.algorithms import bipartite
import cirq



class QiskitBipartiteGraphState():

    def __init__(self, bipartite_graph):
        # super().__init__()
        self.graph = bipartite_graph
        self.white_nodes, self.black_nodes = bipartite.sets(self.graph)

        # Create a quantum register based on the number of nodes
        # in W + the number of nodes in B (= total number of nodes in G)
        self.white_qubits = [cirq.NamedQubit(str(node)) for node in self.white_nodes]
        self.black_qubits = [cirq.NamedQubit(str(node)) for node in self.black_nodes]
        self.circuit = cirq.Circuit()

        # For each vertex in W, apply a Hadamard gate
        for node in self.white_nodes:
            self.circuit.append(cirq.H(cirq.NamedQubit(str(node))))

        # For each vertex in B, apply a Hadamard gate
        for node in self.black_nodes:
            self.circuit.append(cirq.H(cirq.NamedQubit(str(node))))

        # For each edge e={x,y} apply a controlled-Z gate on its vertices
        for x, y in self.graph.edges:
            self.circuit.append(cirq.CZ(cirq.NamedQubit(str(x)), cirq.NamedQubit(str(y))))

        self.node_dict = self.build_node_dict()

    def build_node_dict(self):
        """
        create a node dictionary from node to integer index of a qubit
        in a Qiskit circuit
        :param self:
        """
        self.node_dict = dict()
        for count, node in enumerate(self.graph.nodes):
            self.node_dict[node] = count

    def x_measurement(self, qubit):
        """Measure 'qubit' in the X-basis
        :param qubit: a name to designate a cirq.NamedQubit(str(qubit))
        :return None
        """
        self.circuit.append(cirq.H(cirq.NamedQubit(str(qubit))))
        self.circuit.append(cirq.measure(cirq.NamedQubit(str(qubit))))
        self.circuit.append(cirq.H(cirq.NamedQubit(str(qubit))))

    def x_measure_white(self):
        """
        measure the white qubits in the Pauli X-basis
        :param self:
        """
        for node in self.black_nodes:
            self.circuit.append(cirq.measure(cirq.NamedQubit(str(node))))
        for node in self.white_nodes:
            self.x_measurement(node)

    def x_measure_black(self):
        """
        measure the black qubits in the Pauli X-basis
        :param self:
        """
        self.circuit.barrier()
        for node in self.white_nodes:
            self.circuit.append(cirq.measure(cirq.NamedQubit(str(node))))
        self.circuit.barrier()
        for node in self.black_nodes:
            self.x_measurement(node)

    def apply_stabilizer(self, node):
        """
        applies the stabilizer generator corresponding to node
        :param self:
        :param node: a node in self.graph
        """
        self.circuit.append(cirq.X(cirq.NamedQubit(str(node))))
        for neighbor in self.graph.neighbors(node):
            self.circuit.append(cirq.Z(cirq.NamedQubit(str(neighbor))))
