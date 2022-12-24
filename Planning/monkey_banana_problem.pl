% banana is at B 
% Box is at C
% Monkey is at A

at(A,monkey).
at(B,banana).
at(C,box).

grasp(monkey).
go(monkey,C).
go(monkey,B).

push(monkey,box):- go(monkey,C).
climb(monkey,box):-go(monkey,B).

canreach(banana,monkey):- at(A,monkey),push(monkey,Box),climb(monkey,box).

canget(banana,monkey):- canreach(banana,monkey),grasp(monkey).