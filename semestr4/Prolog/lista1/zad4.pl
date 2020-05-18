le(1,2).
le(2,3).
le(3,4).

le(4,5).
le(4,6).
le(3,5).
le(2,5).
le(1,5).
le(1,3).
le(1,4).
le(1,6).
le(1,1).
le(5,5).
le(6,6).



walidacja(X):-
    le(X,_);
    le(_,X).

najwiêkszy(X):-
    walidacja(X),
    \+ (
          walidacja(Y),
          \+ le(Y,X)
      ).

najmniejszy(X):-
    walidacja(X),
    \+ (
    walidacja(Y),
    \+ le(X,Y)
).

maksymalny(X):-
    walidacja(X),
    \+ (le(X,Y),
       X \= Y).

minimalny(X):-
    walidacja(X),
    \+ (le(Y,X),
        Y \= X).


