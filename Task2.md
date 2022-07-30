
# Define a Context Free Grammar that defines a*|b* = {(),(a),(ab),(aa), (bb),(aabb),...} 

S -> leer | KZL | T | R 
Z -> KZL | leer
T -> K | KT | leer
R -> L | LR | leer
K -> a
L -> b 
