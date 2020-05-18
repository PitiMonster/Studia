% sprawdza czy X+K nalezy do L
czy_nalezy(X,K,L):-
    Res is X+K,
    member(Res,L).

% jesli podzbior ma miec kwadrat to musi miec Sciany jako swoj podzbior
duze(N,L, Uzyte_zap, Result):-
    Sciany = [1,2,3,4,7,11,14,18,21,22,23,24],
    (subset(Sciany,L) -> N1 is 1, append(Sciany, Uzyte_zap, Result)
    ; N1 is 0, append([],Uzyte_zap,Result)
    ),
    N = N1.

% zwraca true, gdy w L jest N srednich kwradratow oraz zwraca liste
% Result zawierajaca uzyte zapalki do budowy potrzebnych kwadratow
srednie(N,L,Uzyte_zap, Result):-
    Sciany = [1,2,8,9],
    ile_srednich(N,Sciany,L,0, Uzyte_zap, Result).

% dodaje wszystkie uzyte do budowania potrzbenego kwadratu zapalki do
% listy i j¹ zwraca
dodaj_uzyte_zap(_,[],Uzyte_zap,Result):-
    append([],Uzyte_zap,Result), !.
dodaj_uzyte_zap(X,[Y|Skladniki],Uzyte_zap,Result):-
    K is X+Y,
    append(Uzyte_zap,[K],Uzyte_zap1),
    dodaj_uzyte_zap(X,Skladniki,Uzyte_zap1,Result).


% zliczanie ile srednich kwradratow jest w podzbiorze L jesli tyle co N
% to zwracamy true
ile_srednich(N,[],_,Curr, Uzyte_zap, Result):-
    Curr = N,
    append([],Uzyte_zap, Result), !.
ile_srednich(N,[X|Sciany],L, Curr, Uzyte_zap, Result):-
    Skladniki = [0,1,3,5,10,12,14,15],
       (
             member(X,L), czy_nalezy(X, 1, L), czy_nalezy(X, 3, L),
             czy_nalezy(X, 5, L), czy_nalezy(X, 10, L), czy_nalezy(X, 12, L),
             czy_nalezy(X, 14, L), czy_nalezy(X, 15, L),
             dodaj_uzyte_zap(X,Skladniki,Uzyte_zap, Uzyte1),
             Curr1 is Curr+1, ile_srednich(N, Sciany, L, Curr1, Uzyte1, Result)
       );
       ile_srednich(N,Sciany,L,Curr,Uzyte_zap,Result).

% Funkcja male zwraca true gdy w L ma w sobie N malych kwadratow
% Zwraca Result zawierajacy numery zapalek uzytych w zbudowanych malych
% kwadratach
male(N, L, Uzyte_zap, Result):-
    %writeln("male"),
    %writeln(Uzyte_zap),
    Sciany = [1,2,3,8,9,10,15,16,17],
    ile_malych(N, Sciany, L, 0, Uzyte_zap, Result).

% zliczanie ile malych kwadratow jest w podzbiorze L
ile_malych(N,[],_,Curr, Uzyte_zap, Result):-
    Curr = N,
    append([],Uzyte_zap,Result), !.
ile_malych(N,[X|Sciany],L,Curr, Uzyte_zap, Result):-
    Skladniki = [0,3,4,7],
    (   member(X,L), czy_nalezy(X,3,L), czy_nalezy(X,4,L), czy_nalezy(X,7,L),
        dodaj_uzyte_zap(X,Skladniki,Uzyte_zap,Uzyte1),Curr1 is Curr + 1,
        ile_malych(N, Sciany, L, Curr1, Uzyte1, Result)
    );
    ile_malych(N,Sciany,L,Curr, Uzyte_zap, Result).

% znajdywanie wszystkich podzbiorów zbioru
subsety([],[]).
subsety([E|Tail], [E|NTail]):-
  subsety(Tail, NTail).
subsety([_|Tail], NTail):-
  subsety(Tail, NTail).

% tworzenie tablicy [1,..,N]
build_set(N,List,N, Result):-
    append([N],List,L2),
    append([],L2,Result),!.
build_set(N, List, Curr, Result):-
    append([Curr],List,L2),
    Curr1 is Curr + 1,
    build_set(N, L2, Curr1, Result).

rysuj(L):-
  between(1,24,R),
  (
    (
      between(1,3,R);
      between(8,10,R);
      between(15,17,R);
      between(22,24,R)
    ),
    (
        member(R,L),
        write("+---")
      ;
        \+ member(R,L),
        write("+   ")
    );
    (
      between(4,7,R);
      between(11,14,R);
      between(18,21,R)
    ),
    (
        member(R,L),
        write("|   ")
      ;
        \+ member(R,L),
        write("    ")
    )
),
(
  (
    (
      R=3 ;
      R=10;
      R=17;
      R=24
    ),
    write("+\n")
  );
  (
    (
      R=7;
      R=14;
      R=21
    ),
    write("\n")
  )
),
fail;
true.

wypisz_zbior([]):- !.
wypisz_zbior([X|Set]):- rysuj(X), wypisz_zbior(Set).

% wywolywanie funkcji duze,srednie,male i zwrocenie zbioru liczb jesli
% wszystko sie zgadza
rozpakuj_instr(N ,L,G):-
    build_set(24,[1],2,Sciany),
    member(N,Sciany),
    Size is 24 - N,
    subsety(Sciany,Subs),
    length(Subs,Size),
    L = (X,Y,Z),
    X =.. [FunctionD, ArgD],
    Y =.. [FunctionS, ArgS],
    Z =.. [FunctionM, ArgM],
    call(FunctionD, ArgD, Subs,[],Uzyte_zap1),
    call(FunctionS, ArgS, Subs,Uzyte_zap1, Uzyte_zap2),
    call(FunctionM, ArgM, Subs, Uzyte_zap2, Uzyte_zap3),
    subset(Subs, Uzyte_zap3),
    append([],Subs,G).

zapalki(N,L):-
    setof(G,rozpakuj_instr(N, L,G),Set),
    wypisz_zbior(Set).

% tak program widzi kwadrat
%  + 1 + 2 + 3 +
%  4   5   6   7
%  + 8 + 9 + 10+
%  11  12  13  14
%  + 15+ 16+ 17+
%  18  19  20  21
%  + 22+ 23+ 24+
