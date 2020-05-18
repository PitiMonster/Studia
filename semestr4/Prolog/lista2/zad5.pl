czyPusty(L):-
    length(L,K),
    K =:= 0.

czyD³ugoœæ(N,X):-
    K is 2*N,
    length(X,S),
    S = K.

czyDwaRazy(N,X,Current):-
    (   Current is N+1 -> !
    ;
    select(Current, X, Newx), % usuniêcie elementu X dwa razy i sprawdzenie czy nadal tam jest
    select(Current, Newx, Newx2),
    not(member(Current,Newx2)),
    C is Current+1,
    czyDwaRazy(N,Newx2, C)
    ).

czyParzyœcie(X,L):-
    L=[Elem|Reszta],
    append(_,[Elem|K],X),
    append(P,[Elem|_],K), % P - elementy pomiêdzy dwoma takimi samymi elementami
    length(P,Size),
    0 is mod(Size,2),
    (   czyPusty(Reszta) -> true; czyParzyœcie(X,Reszta)).


lista(N, X):-
    czyD³ugoœæ(N,X),
    czyDwaRazy(N,X,1),
    sort(X,L), % lista elementów bez powtórzeñ
    czyParzyœcie(X,L).
