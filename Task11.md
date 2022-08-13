Show that the following CFG is ambiguous

<S> -> <S><S> | 'a'

1. <S> -> <S><S>
2. <S><S> -> <S_2><S_1><S>
3. <S_2><S_1><S> -> a<S_1><S>
4. a<S_1><S> -> aa<S>
5. aa<S> -> aaa

1. <S> -> <S><S>
2. <S><S> -> <S><S_1><S_2>
3. <S><S_1><S_2> -> a<S_1><S_2>
4. a<S_1><S_2> -> aa<S_2>
5. aa<S_2> -> aaa
