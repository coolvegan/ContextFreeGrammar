# Write a CFG that defines the set of all strings over the alphabet {a,b} that have exactly two b.

S -> RZ
R -> T| TR
T -> a | EMPTY
Z -> bb
