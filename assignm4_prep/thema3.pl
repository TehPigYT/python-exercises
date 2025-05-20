is_odd(X) :- 1 is X mod 2.
is_even(X) :- 0 is X mod 2.

even_elements([], []).
even_elements([H|T], [H,R]) :-
  is_even(H),
  even_elements(T, R).
even_elements([H|T], R) :-
  is_odd(H),
  even_elements(T, R).