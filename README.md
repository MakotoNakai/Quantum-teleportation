# Quantum-teleportation

## Definition  
Quantum teleportation is a protocal of quantum communication which send information of 1 qubits by creating entanglement between 2qubits(the sender and the receiver).  

## Mathematical representation.   
Suppose you want to send the <img src="https://latex.codecogs.com/gif.latex?|1\rangle" title="|1\rangle" /> state.  
I will explain how to deliver this state below.  

<img src="https://latex.codecogs.com/gif.latex?|1\rangle|00\rangle&space;\xrightarrow&space;{I\bigotimes&space;H&space;\bigotimes&space;I}&space;|1\rangle&space;\frac{|0\rangle&plus;|1\rangle}{\sqrt{2}}&space;|0\rangle&space;\xrightarrow{cx_{12}}|1\rangle&space;\frac{|00\rangle&plus;|11\rangle}{\sqrt{2}}&space;\xrightarrow{cx_{01}}|1\rangle&space;\frac{|10\rangle&plus;|01\rangle}{\sqrt{2}}" title="|1\rangle|00\rangle \xrightarrow {I\bigotimes H \bigotimes I} |1\rangle \frac{|0\rangle+|1\rangle}{\sqrt{2}} |0\rangle \xrightarrow{cx_{12}}|1\rangle \frac{|00\rangle+|11\rangle}{\sqrt{2}} \xrightarrow{cx_{01}}|1\rangle \frac{|10\rangle+|01\rangle}{\sqrt{2}}" />  

<img src="https://latex.codecogs.com/gif.latex?\xrightarrow&space;{H\bigotimes&space;I&space;\bigotimes&space;I}&space;\frac{|0\rangle&plus;|1\rangle}{\sqrt{2}}&space;\frac{|10\rangle&plus;|01\rangle}{\sqrt{2}}&space;=&space;\frac{|010\rangle&plus;|110\rangle&plus;|001\rangle&plus;|101\rangle}{2}\xrightarrow&space;{cx_{12}}\frac{|011\rangle&plus;|111\rangle&plus;|001\rangle&plus;|101\rangle}{2}" title="\xrightarrow {H\bigotimes I \bigotimes I} \frac{|0\rangle+|1\rangle}{\sqrt{2}} \frac{|10\rangle+|01\rangle}{\sqrt{2}} = \frac{|010\rangle+|110\rangle+|001\rangle+|101\rangle}{2}\xrightarrow {cx_{12}}\frac{|011\rangle+|111\rangle+|001\rangle+|101\rangle}{2}" />  

<img src="https://latex.codecogs.com/gif.latex?=\frac{|01\rangle&plus;|11\rangle&plus;|00\rangle&plus;|10\rangle}{2}|1\rangle" title="=\frac{|01\rangle+|11\rangle+|00\rangle+|10\rangle}{2}|1\rangle" />  

This you implement this computation by typing the following codes in `Teleportation.py`  

```
#Qubits as Alice	
ba = 2

#Qubits as Bob
bb = 2
cn = 1

qa = QuantumRegister(ba)
qb = QuantumRegister(bb)
c = ClassicalRegister(cn)
qca  = QuantumCircuit(qa,c)
qcb  = QuantumCircuit(qb,c)
qc = qca+qcb

#Suppose Alice is going to send |1> state to Bob
qc.x(qa[0])
#Protect the state by putting barrier
qc.barrier()

qc.h(qa[1])
qc.cx(qa[1],qb[0])
qc.cx(qa[0],qa[1])
qc.h(qa[0])
qc.cx(qa[1],qb[0])
qc.measure(qb[0],c[0])
```   

Here is the result on the QASM simulator.  
![quantum_teleportation_sim](https://user-images.githubusercontent.com/45162150/50746950-cc9f2980-1274-11e9-8899-fb46e81c3c39.png)


