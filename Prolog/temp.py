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
father(X,Y):- parent(X,Y),male(X).
haschild(X):- parent(X,_).
