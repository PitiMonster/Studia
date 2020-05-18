zla(X) :-
append(_, [Wi | L1], X),
append(L2, [Wj | _], L1),
length(L2, K),
abs(Wi - Wj) =:= K + 1.

dobra(X) :-
\+ zla(X).

hetmany(N, P) :-
numlist(1, N, L),
permutation(L, P),
dobra(P).



draw_line(0):- writeln("+"), !.
draw_line(Length):-
    write("+-----"),
    N is Length - 1,
    draw_line(N).


draw_field(Field):-
    Field = "B",
    write("|:::::").
draw_field(Field):-
    Field = "W",
    write("|     ").
draw_field(Field):-
    Field = "BH",
    write("|:###:").
draw_field(Field):-
    Field = "WH",
    write("| ### ").

draw_row([]):- writeln("|"), !.
draw_row([Field|Rest_fields]):-
    draw_field(Field),
    draw_row(Rest_fields).

draw([], N):- draw_line(N), !.
draw([Row|Fields], N):-
    draw_line(N),
    draw_row(Row),
    draw_row(Row),
    draw(Fields, N).

generate_row([], _, _, Curr_row, Row):- append([], Curr_row, Row), !.
generate_row([Hetman_pos|L], Row_num, N, Curr_row, Row):-
    (   N mod 2 =:= 0 -> Color = "W"; Color = "B"),
    (   Hetman_pos =:= Row_num -> (Color = "W" -> Color2 = "WH"; Color2 = "BH"); Color2 = Color),
    N1 is N + 1,
    append(Curr_row, [Color2], New_curr_row),
    generate_row(L, Row_num, N1, New_curr_row, Row).


generate_fields_list(_, 0, Curr_fields, Fields):- append([],Curr_fields, Fields) ,!.
generate_fields_list(L, N, Curr_fields, Fields):-
    generate_row(L, N, N, [], Row),
    append(Curr_fields, [Row], New_curr_fields),
    N1 is N - 1,
    generate_fields_list(L, N1, New_curr_fields, Fields).


board(L):-
    length(L,N),
    generate_fields_list(L, N,[], Fields),
    draw(Fields, N).
