american(robert).
hostile(nano).
weapon(missile).
sell(robert,nano,missile).

isCriminal(X):- sell(X,Y,Z),american(X),hostile(Y),weapon(Z).