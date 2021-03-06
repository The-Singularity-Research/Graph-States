# Graph-States
## Compatability
We currently have compatability with:

- [IBM Qiskit](https://qiskit.org/)
- [Google Cirq](https://cirq.readthedocs.io/en/stable/)

## Introduction
What are **Graph States**? Graph States are systems of interacting particles, usually 2-level systems (qubits), which are represented by graphs like the ones seen below found in the Nature paper [Experimental entanglement of six photons in graph states](https://www.nature.com/articles/nphys507) and [Estimating localizable entanglement from witnesses](https://www.researchgate.net/figure/Color-online-Graph-state-stabilizers-and-local-complementation-operation-a-A_fig1_323627521):

![Graph States](https://github.com/The-Singularity-Research/Graph-States/blob/master/Use%20Case%20Examples/graph_states.png)

![Graph States 2](https://github.com/The-Singularity-Research/Graph-States/blob/master/Use%20Case%20Examples/graph_states_2.png)



## Applications

### Measurement Based (One-Way) Quantum Computing

---

**Measurement Based Quantum Computing (MBQC)** (see [Completeness of classical spin models and universal
quantum computation](https://arxiv.org/pdf/0812.2368.pdf)), also known as **One-Way Quantum Computing**
 is one way of performing adaptive measurements on a highly entangled system of qubits so that entanglement 
 is used as a resource, which is gradually reduced after each *adaptive* measurement on individual qubits. 
 This is one of the primary uses of graph states, and using the graphs given by surface codes, this can be 
 done in a way that is topologically protected from errors. Morevover, the measurement based approach makes 
 the computation "one-way", which can also protect against errors by making the thermal requirements less strict 
 (see [From molecular biology to quantum computing - Charles H. Bennett](https://www.youtube.com/watch?v=a-i_yhLLkiY&t=48s)).


### Error Correction
Any stabilizer code can be modeled as a graph state, so understanding quantum error correction through graph states gives a graphical presentation of stabilizer codes. 


### Quantum Cryptography and blind quantum computation 
See for example 

#### Papers:

- [Graph States for Quantum Secret Sharing](https://arxiv.org/pdf/0808.1532.pdf) 
- [Verifiable measurement-only blind quantum computing with stabilizer testing](https://arxiv.org/pdf/1505.07535.pdf), 
- [Experimental demonstration of graph-state
quantum secret sharing](https://www.nature.com/articles/ncomms6480.pdf)

#### Videos:

- [Matthew G. Parker / Exclusivity graphs from quantum graph states – and mixed graph generalisations](https://www.youtube.com/watch?v=Dka96mKnm9U&t=29s)
- [Simon Perdrix: Quantum Secret Sharing with Graph States](https://www.youtube.com/watch?v=igphWtdZJww&t=25s)


### Modeling Ising type models 
Graph states are naturally an example of Ising models in statistical mechanics, with entanglement/interactions represented by edges of the graph between nodes representing the particles. 
- [Mapping Classical Spin Models to the Graph State Formalism](https://perimeterinstitute.ca/videos/mapping-classical-spin-models-graph-state-formalism)


### Quantum Complexity using Partition Functions 
See  
- [Section 5: Measurement-based quantum computation](https://arxiv.org/pdf/0910.1116.pdf)
- [Commuting quantum circuits and complexity of Ising partition functions](https://iopscience.iop.org/article/10.1088/1367-2630/aa5fdb/pdf)

### Modeling Quantum Phase Transitions 

See A. Kitaev's lecture on [Topological quantum phases](https://www.youtube.com/watch?v=W2vUbTR2RWQ&t=898s) 


### Measurement Based Quantum Computing, Entanglement Entropy, and Entanglement as a Computational Resource 
See 
- [Entanglement in Graph States and its Applications](https://arxiv.org/pdf/quant-ph/0602096.pdf)
- [Physical-depth architectural requirements for generating universal
photonic cluster states](https://iopscience.iop.org/article/10.1088/2058-9565/aa913b/pdf)


### Modeling Condensed Matter Physics on Quantum Computers 


### Modeling Quantum/Classical Information Processing in DNA 

This is useful for applications to Bio-informatics, protien folding, and understanding applications of CRISPR, 
see for example 

- [Adiabatic graph-state quantum computation](https://arxiv.org/pdf/1309.1443.pdf) 

- [Quantum entanglement between the electron clouds of nucleic acids in DNA](https://arxiv.org/pdf/1006.4053.pdf), 

which also has an accompanying Google lecture: 

- [Classical and Quantum Information in DNA (Google Workshop on Quantum Biology)](https://www.youtube.com/watch?v=2nqHOnVTxJE&t=66s)
