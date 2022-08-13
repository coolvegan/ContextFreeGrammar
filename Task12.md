12. Draw the parse tree for a*b+c corresponding to the grammars in Fig 3.3 and Fig 3.4

S -> T | S * T
T -> F | T + F
F -> a | b | c | S


            [+]
           /   \
         /      \
       [*]       c
      /   \
     /     \
    a       b


                  S
                / * \
               |    / \
               c   F + F
                   |   |
                   a   b
                      