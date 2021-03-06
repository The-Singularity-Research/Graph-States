import unittest

import networkx as nx
from qiskit.circuit.classicalregister import Clbit, ClassicalRegister

from QiskitGraphStates import QiskitGraphState


class GraphStateTest(unittest.TestCase):
    def setUp(self):
        self.G = nx.Graph()
        self.G.add_edges_from([(0, 1), (1, 2)])

    def test_init_edges(self):
        a = QiskitGraphState(self.G)
        self.assertEqual(sorted(a.graph.edges), sorted([(0, 1), (1, 2)]))

    def test_init_build_node_dict(self):
        a = QiskitGraphState(self.G)
        assert a.node_dict == {0: 0, 1: 1, 2: 2}

    def test_x_measurement(self):
        """this will give you something different every time,
         so don't try to test the exact answer"""
        a = QiskitGraphState(self.G)
        a.x_measurement(a.qreg[0], a.creg[0])
        assert isinstance(a.creg[0], type(Clbit(ClassicalRegister(3, 'c2'), 0)))

    def test_apply_stabilizer(self):
        a = QiskitGraphState(self.G)
        assert a.circuit.depth() == 3
        a.apply_stabilizer(0)
        assert a.circuit.depth() == 4
        a.apply_stabilizer(1)
        assert a.circuit.depth() == 5


if __name__ == '__main__':
    unittest.main()
