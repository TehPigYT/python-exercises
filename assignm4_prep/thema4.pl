positive_average(List, Avg) :-
  positive_sum_count(List, 0, 0, Sum, Count),
  Avg is Sum / Count.

positive_sum_count([], Sum, Count, Sum, Count).
positive_sum_count([H|T], S0, C0, Sum, Count) :-
  ( H > 0 ->
      S1 is S0 + H,
      C1 is C0 + 1;
      S1 = S0,
      C1 = C0
  ),
  positive_sum_count(T, S1, C1, Sum, Count).