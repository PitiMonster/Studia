max_sum(L,X):-
  length(L,Size),
  Size =:= 0 -> X is 0,!;
  L=[Elem|Reszta],
  % lista, najwieksza suma, aktualna najwieksza suma, aktualna suma
  max_sum_(Reszta,X,Elem,Elem).
% ide od pierwszego do ostatniego elementu je�li curr elem > curr elem +
% curr sum to curr sum = curr elem
max_sum_(L,X,CurrMaxSum,CurrSum):-
    length(L,Size),
    (   Size =:= 0 -> append([],CurrMaxSum,X), !
    ;
    L=[Elem|Reszta],
    K is CurrSum + Elem,
    (   K > Elem -> NextSum is K,(
                K > CurrMaxSum -> NextMaxSum is K; NextMaxSum is CurrMaxSum)
    ;
    (   NextSum is Elem,
        (   Elem > CurrMaxSum -> NextMaxSum is Elem; NextMaxSum is CurrMaxSum))
    ),
    max_sum_(Reszta,X,NextMaxSum,NextSum)).
