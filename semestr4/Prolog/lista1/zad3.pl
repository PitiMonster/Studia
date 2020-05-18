above(rower, o³ówek).
above(aparat, motyl).

left_of(o³ówek, klepsydra).
left_of(klepsydra, motyl).
left_of(motyl, ryba).

right_of(X,Y):- left_of(Y,X).

below(X,Y) :- above(Y,X).

left_of_rec(X,Y) :-
    left_of(X,Y).
left_of_rec(X,Y):-
    left_of(X,Z),
    left_of_rec(Z,Y).

above_rec(X,Y):-
    above(X,Y).
above_rec(X,Y):-
    above(Z,Y),
    above_rec(X,Z).


higher(X,Y) :-
    above_rec(X,Y);
    (
        above(X,A),
        above(Y,B),
        higher(A, B)
    );
    (
        above(X,_), \+ above(Y,_)
    ).
