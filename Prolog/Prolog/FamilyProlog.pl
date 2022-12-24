female(seeta).
female(hema).
female(maya).
male(arjun).
male(shyam).
male(ram).
male(mohan).

parent(seeta,shyam).
parent(ram,shyam).
parent(shyam,maya).
parent(shyam,hema).
parent(hema,arjun).
parent(mohan,arjun).

mother(X,Y):- parent(X,Y),female(X).
ismother(X):- parent(X,Y),female(X).
father(X,Y):- parent(X,Y),male(X).
isfather(X):- parent(X,Y),male(X).
grandfather(X,Y):- father(X,Z),father(Z,Y).
ismarried(X):- isfather(X);ismother(X).