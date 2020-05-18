arc(a,b).
arc(b,a).
arc(b,c).
arc(c,d).

osi¹galny(X,X).
osi¹galny(X,Y):-
    œcie¿ka(X,Y,[X]).

œcie¿ka(X,Y,L):-
    arc(X,Y),
    \+ member(Y,L).

œcie¿ka(X,Y,L):-
    arc(X,Z),
    \+ member(Z,L),
    œcie¿ka(Z,Y,[Z|L]).
