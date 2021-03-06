perm([], []).
perm(L1, [X | L3]) :-
    select(X, L1, L2),
    perm(L2, L3).

even_permutation(L,X):-
    perm(L,X),
    disorders_number(X,0,K),
    0 is mod(K,2).

odd_permutation(L,X):-
    perm(L,X),
    disorders_number(X,0,K),
    1 is mod(K,2).

% sumuje wszystkie nieporz�dki i zwracam ich liczb�
disorders_number(P,K,Disorders):-
    length(P,Size),
    (   Size =:= 0 -> append([],K,Disorders), !
    ;
    P = [Elem|Reszta],
    count_dis(Elem,Reszta,0,1,X),
    S is X + K,
    disorders_number(Reszta,S,Disorders)).

% zliczam ile element�w < Elem jest przed nim w permutacji
count_dis(Elem,Reszta,K,Curr,X):-
    (   Curr =:= Elem -> append([],K,X),!
    ;
    (   member(Curr, Reszta) -> S is K+1; S is K),
        NextCurr is Curr + 1,
        count_dis(Elem,Reszta,S,NextCurr,X)).



