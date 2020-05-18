le(1,1).
le(1,2).
le(2,3).
le(1,3).
le(2,2).
le(3,3).

walidacja(X):-
    le(X,_);
    le(_,X).

zwrotna():-
    \+ (
    walidacja(X),
    \+ (le(X,X))
).

przechodnia():-
    \+ (
        le(X,Y),
        le(Y,Z),
        \+ (le(X,Z))
    ).

s³aba_antysymetria():-
    \+ (
      le(X,Y),
      le(Y,X),
      X \= Y).

czêœciowy_porz¹dek :-
    zwrotna(),
    przechodnia(),
    s³aba_antysymetria().
