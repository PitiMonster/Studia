czyDzielenie(X):-
    X = '/'.

czyMno�enie(X):-
    X = '*'.

isEmpty(L):- % sprawdzenie czy lista jest pusta
    length(L,S),
    S=:=0.

rozdzielMno�enia(Dzia�anie,Elementy):-
    Dzia�anie=..[Operacja|L],
    czyMno�enie(Operacja)->( % je�li operacja jest mno�eniem
               L=[Lewy,Prawy], % bior� mno�n� i mno�nik
               rozdzielMno�enia(Lewy,Lelems), % dalej sprwadzam czy zawieraj� iloraz i dostaj� tablic� mno�nych i mno�nik�w
               rozdzielMno�enia(Prawy,Pelems),
               K=[Lelems,Pelems],  % scalam dwie tablice
               append([],K,Elementy), % dodaj� do zmiennej elementy
               true
           )
    ; append([],Dzia�anie,Elementy).

po��czMno�enia(Elementy, Dzia�anie):- % tworzenie ilorazu z element�w w Elementy i wpisanie go do Dzia�anie
    Elementy=[Element|Reszta], % bior� pierwszy element z listy
    length(Reszta,Len),
    Len =:= 0 ->(
                append([],Element,Dzia�anie),!
            )
    ;
    po��czMno�enia(Reszta,Dzia�), % reszt� dalej dziel�
    K=..[*,Element,Dzia�], % p�niej rekurencyjne ��czenie znakiem *
    append([],K,Dzia�anie).

regu�a(X,O,Y,Y):- % sprawdzenie czy nie dodaj� zera
    O = '+',
    X = 0, !.
regu�a(X,O,Y,0):- % sprawdzenie czy nie odejmuj� takich samych element�w od siebie
    O = '-',
    X = Y.
regu�a(X,O,Y,0):- % sprawdzenie iloczynu lub ilorazu z udzia�em zera
    not(
        O = '+';
        O = '-'
    ),
    X = 0;
    Y = 0. % tu si� pozbywam operacji, kt�re maj� dzielenie przez 0

regu�a(X,O,Y,S):- % regu�a skracaj�ca u�amki
    czyDzielenie(O),
    rozdzielMno�enia(X,Xelems), % zwraca tablic� element�w kt�re mo�na skr�ci� z dzielnej
    (   ( \+ is_list(Xelems)) -> Xele=[Xelems] % je�li zwr�ci� jeden element to robi� z niego list�
    ;
    Xele=Xelems
   ),
    rozdzielMno�enia(Y,Yelems), % zwraca tablic� element�w kt�re mo�na skr�ci� z dzielnika
   (    (\+ is_list(Yelems)) -> Yele=[Yelems]
    ;
    Yele=Yelems
   ),
    intersection(Xele,Yele,Common), % znalezienie elemnt�w wsp�lnych z dzielnika i dzielnej
    length(Common,Len),
    (   Len =:= 0 ->( % je�li nie ma wsp�lnych element�w to zwr�cenie pierwotnego dzia�ania
                K=..[O,X,Y],
                append([],K,S),
                true
            )
    ;
        subtract(Xele,Common,Newx), % znalezienie element�w, kt�re nie zostan� skr�cone z dzielnej
        subtract(Yele,Common,Newy), % znalezienie element�w, kt�re nie zostan� skr�cone z dzielnika

        (isEmpty(Newx) -> Xdzia�=1; po��czMno�enia(Newx,Xdzia�)), % je�li s� jeszcze jakie� elementy w dzielniku to ��cz� je mno�eniem
        (isEmpty(Newy) -> append([],Xdzia�,S); po��czMno�enia(Newy,Ydzia�), % je�li nie ma element�w w dzielnej to ona znika
        K=..[O,Xdzia�,Ydzia�],
        append([],K,S))
    )
    .

upro��(X,W):-
    setof(X, upro��_(X,W), Set),
    member(X,Set), !. % wypisanie tylko wyniku

% rozdzielam na termy dop�ki nie dostan� pojedy�czych symboli
upro��_(X,W):-
    append([],X,X),
    append([],X,W).
upro��_(X,W):-
    X =..[Operacja, Lewa, Prawa],
    upro��(Lewa, Lwynik),
    upro��(Prawa,Pwynik),
    (
         (
              \+ czyMno�enie(Operacja),
              \+ czyDzielenie(Operacja),
              regu�a(Lwynik, Operacja, Pwynik, Pwynik)  % sprawdzam czy dodaje lub odejmuje 0
          ) ->
              (Pwynik = 0 -> append([],Lwynik,W); append([],Pwynik, W))
          ;  regu�a(Lwynik, Operacja, Pwynik, 0) -> append([],0,W) % sprawdzam czy wynik dw�ch operacji da mi w rezultacie zero
          ;  regu�a(Lwynik,Operacja, Pwynik, S) -> append([],S,W)  % sprawdzam czy da si� co� sk�ci� w u�amku
          ;  K=..[Operacja, Lwynik, Pwynik], append([],K,W) % je�li si� nic nie da zredukowa� zwracam form� pocz�tkow�
          ).

