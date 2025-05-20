parent(john, mary).
parent(jane, mary).
parent(john, tom).
parent(jane, tom).
parent(mary, alice).
parent(mike, alice).

grandparent(X, Y) :-
  parent(X, Z),
  parent(Z, Y).
sibling(X, Y) :-
  parent(P, X),
  parent(P, Y),
  X \= Y.