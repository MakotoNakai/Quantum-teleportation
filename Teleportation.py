from qiskit import IBMQ, QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.qasm import pi
from qiskit.tools.visualization import plot_histogram, circuit_drawer
import numpy as np

APItoken = "Replace me"
url = "Replace me"
IBMQ.enable_account(APItoken, url)

IBMQ.backends()

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

#Suppose Alice is going to send |+> state to Bob
qc.h(qa[0])
qc.barrier()

qc.h(qa[1])
qc.cx(qa[1],qb[0])
qc.cx(qa[0],qa[1])
qc.h(qa[0])
qc.cx(qa[1],qb[0])
qc.cz(qa[0],qb[0])
qc.measure(qb[0],c[0])
	
qc.draw()

#Put the real device first and put a simulator later.	
backends = ['ibmq_20_tokyo', 'qasm_simulator']

#Use this for the actual machine
#backend_sim = IBMQ.get_backend(backends[0]) #{'0': 2075, '1': 2021}

#Use this for the simulation
backend_sim = Aer.get_backend(backends[1]) #{'1': 2041, '0': 2055}

result = execute(qc, backend_sim, shots=4096).result()

#You can get the quantum circuit in Latex style.
#circuit_drawer(qc).show()

print(result.get_counts(qc))

# I recommend you to execute the following command in the next cell in Anaconda, 
#because this didn't work in the command line on my laptop.
plot_histogram(result.get_counts(qc))