sum_to_n(N, Sum) :-
  N > 0,
  N1 is N - 1,
  sum_to_n(N1, R1),
  R is R1 - N.