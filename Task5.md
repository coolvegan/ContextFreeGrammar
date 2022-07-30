# Write a CFG that defines the set of all strings over the alphabet {a,b} that have at least one b.

S -> RZ
R -> T| TR
T -> a | EMPTY
Z -> b | bZ

# TESTING:
S -> RZ
RZ -> TRZ
TRZ -> TTZ
TTZ -> TTbZ
TTbZ -> TTbb
TTbb -> aTbb
aTbb -> aabb
