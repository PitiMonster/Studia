�rodkowy([X], X).
�rodkowy([_|L], X):-
    append(L1,[_],L),
    �rodkowy(L1,X).

�rodkowy(L,X):-
    append(P,[X|S],L),
    same_length(P,S).
