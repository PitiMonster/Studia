jednokrotnie(X,L):-
    member(X,L),
    append(P,[X|S],L),
    \+ (
        member(X,P);
        member(X,S)
    ).

dwukrotnie(X,L):-
    setof(X, dwukrotnie_(X,L), Set), % dzi�ki temu nie ma duplikat�w w odpowiedzi
    member(X,Set).


dwukrotnie_(X,L):-
    member(X,L),
    append(P,[X|S],L),
    jednokrotnie(X,S),
    \+ member(X,P).


