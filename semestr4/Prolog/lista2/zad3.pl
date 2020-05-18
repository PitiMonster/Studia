arc(a,b).
arc(b,a).
arc(b,c).
arc(c,d).

osi�galny(X,X).
osi�galny(X,Y):-
    �cie�ka(X,Y,[X]).

�cie�ka(X,Y,L):-
    arc(X,Y),
    \+ member(Y,L).

�cie�ka(X,Y,L):-
    arc(X,Z),
    \+ member(Z,L),
    �cie�ka(Z,Y,[Z|L]).
