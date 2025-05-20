book('The Hobbit', 'Tolkien', 1937).
book('1984', 'Orwell', 1949).
book('The Silmarillion', 'Tolkien', 1977).
book('Brave New World', 'Huxley', 1932).

by_author(Author, Title) :-
  book(Title, Author, _).

before_year(Year, Title) :-
  Year(Title, _, Y),
  Y < Year.

by_author_before_year(Author, Year, Title) :-
  by_author(Author, Title),
  before_year(Year, Title).