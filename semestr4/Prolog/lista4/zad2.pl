% Norweg zamieszkuje pierwszy dom
fakt1(L):-
    ustaw(1, L,(norweg,_,_,_,_)).

% Anglik mieszka w czerwonym domu
fakt2([(anglik,czerwony,_,_,_)|_]).
fakt2([_|L]):-
    fakt2(L).

% Zielony dom znajduje sie bezposrednio po lewej stronie domu bialego
fakt3([(_,zielony,_,_,_),(_,bialy,_,_,_)|_]).
fakt3([_|L]):-
    fakt3(L).

% Dunczyk pija herbatke
fakt4([(dunczyk,_,_,herbata,_)|_]).
fakt4([_|L]):-
    fakt4(L).

% Palacz papierosow light mieszka obok hodowcy kotow
fakt5([(_,_,_,_,kot),(_,_,light,_,_)|_]).
fakt5([(_,_,light,_,_),(_,_,_,_,kot)|_]).
fakt5([_|L]):-
    fakt5(L).

% Mieszkaniec zoltego domu pali cygara
fakt6([(_,zolty,cygaro,_,_)|_]).
fakt6([_|L]):-
      fakt6(L).

% Niemiec pali fajke
fakt7([(niemiec,_,fajka,_,_)|_]).
fakt7([_|L]):-
    fakt7(L).

% Mieszkaniec srodkowego domu pija mleko
fakt8(L):-
    ustaw(3, L, (_,_,_,mleko,_)).

% Palacz papierosow light ma sasiadam ktory pije wode
fakt9([(_,_,_,woda,_),(_,_,light,_,_)|_]).
fakt9([(_,_,light,_,_),(_,_,_,woda,_)|_]).
fakt9([_|L]):-
    fakt9(L).

% Palacz papierosow bez filtra hoduje ptaki
fakt10([(_,_,filtr,_,ptaki)|_]).
fakt10([_|L]):-
    fakt10(L).

% Szwed hoduje psy
fakt11([(szwed,_,_,_,psy)|_]).
fakt11([_|L]):-
    fakt11(L).

% Norweg mieszka obok niebieskiego domu
fakt12([(norweg,_,_,_,_),(_,niebieski,_,_,_)|_]).
fakt12([(_,niebieski,_,_,_),(norweg,_,_,_,_)|_]).
fakt12([_|L]):-
    fakt12(L).

% Hodowca koni mieszka obok zoltego domu
fakt13([(_,zolty,_,_,_),(_,_,_,_,konie)|_]).
fakt13([(_,_,_,_,konie),(_,zolty,_,_,_)|_]).
fakt13([_|L]):-
    fakt13(L).

% Palacz mentolowych pija piwo
fakt14([(_,_,mentol,piwo,_)|_]).
fakt14([_|L]):-
    fakt14(L).

% W zielonym domu pija sie kawe
fakt15([(_,zielony,_,kawa,_)|_]).
fakt15([_|L]):-
    fakt15(L).

dodaj_ryby([(_,_,_,_,ryby)|_]).
dodaj_ryby([_|L]):-
    dodaj_ryby(L).

ludzie(0,[]):- !.
ludzie(N,[(Kto, Kolor, Palenie, Picie, Zwierze)|T]):-
    N1 is N-1,
    ludzie(N1,T).

ustaw(1, [D|_], D):-!.
ustaw(_, [D|_], D).
ustaw(Numer, [_|Lista], Dane):-
    N1 is Numer - 1,
    ustaw(N1, Lista, Dane).


fakty(L):-
    ludzie(5,L),
    fakt1(L),
    fakt2(L),
    fakt3(L),
    fakt4(L),
    fakt5(L),
    fakt6(L),
    fakt7(L),
    fakt8(L),
    fakt9(L),
    fakt10(L),
    fakt11(L),
    fakt12(L),
    fakt13(L),
    fakt14(L),
    fakt15(L),
    dodaj_ryby(L).

rybka(Kto):-
    fakty(L),
    ustaw(5, L, (Kto,_,_,_,ryby)), !.

