A regular grammar is a context free grammar in which the right side of each production is either a 
single terminal, a single terminal followed by a single nonterminal, or empty. 
Give regular grammars that define the same languages as a*, aa*, a*b*, a*|b*, bcc*, (a|b)*, and (b*ab*ab*ab*)*

# a* 
S -> S | F
F -> a | aF | Empty

# aa*
S -> T 
T -> a | aT | Empty

# a*b* 
S ->  FG 
F -> a | aF | Empty
G -> b | bG | Empty

# a*|b*
S -> T | U
T -> a | aT | Empty
U -> b | bU | Empty

# bcc*
S -> FT
F -> b 
T -> cT | c

# (a|b)*
S -> T | U | X
X -> FXG | EMPTY 
T -> FT | F | EMPTY
U -> GU | G | EMPTY
F -> a
G -> b 

# (b*ab*ab*ab*)*

S -> XGXGXGX | XGXGXGX S 
G -> a
X -> F | XF | EMPTY
F -> b 
