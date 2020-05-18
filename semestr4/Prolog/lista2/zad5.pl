czyPusty(L):-
    length(L,K),
    K =:= 0.

czyD�ugo��(N,X):-
    K is 2*N,
    length(X,S),
    S = K.

czyDwaRazy(N,X,Current):-
    (   Current is N+1 -> !
    ;
    select(Current, X, Newx), % usuni�cie elementu X dwa razy i sprawdzenie czy nadal tam jest
    select(Current, Newx, Newx2),
    not(member(Current,Newx2)),
    C is Current+1,
    czyDwaRazy(N,Newx2, C)
    ).

czyParzy�cie(X,L):-
    L=[Elem|Reszta],
    append(_,[Elem|K],X),
    append(P,[Elem|_],K), % P - elementy pomi�dzy dwoma takimi samymi elementami
    length(P,Size),
    0 is mod(Size,2),
    (   czyPusty(Reszta) -> true; czyParzy�cie(X,Reszta)).


lista(N, X):-
    czyD�ugo��(N,X),
    czyDwaRazy(N,X,1),
    sort(X,L), % lista element�w bez powt�rze�
    czyParzy�cie(X,L).
