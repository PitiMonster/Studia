dzialanie(X, D1, D2) :-
    X = D1 + D2.

dzialanie(X, D1, D2) :-
    X = D1 - D2.

dzialanie(X, D1, D2) :-
    X = D1 * D2.

dzialanie(X, D1, D2) :-
  0 =\= D2,
  X = D1 / D2.

stworz([X], X).
stworz(L, X) :-
	append(L1, L2, L),
	\+ length(L1, 0),
	\+ length(L2, 0),
	stworz(L1, D1),
	stworz(L2, D2),
	dzialanie(X, D1, D2).

wyrazenie(Liczby, Wynik, Wyrazenie) :-
  stworz(Liczby, X),
	Wynik is X,
	Wyrazenie = X, !.
