œrodkowy([X], X).
œrodkowy([_|L], X):-
    append(L1,[_],L),
    œrodkowy(L1,X).

œrodkowy(L,X):-
    append(P,[X|S],L),
    same_length(P,S).
