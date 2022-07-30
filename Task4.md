# Write a CFG that defines the set of all strings over the alphabet {a,b} that have exactly one b.

S -> RZ
R -> T| TR
T -> a | EMPTY
Z -> b

# TESTING:
S -> RZ
RZ -> TRZ
TRZ -> TTRZ
TTRZ -> TTTZ
TTTZ -> aTTZ
aTTZ -> aaTZ
aaTZ -> aaaZ
aaaZ -> aaab
