point1([6, 148, 72, 35, 0, 33.6, 0.627, 50]).
point2([1, 85, 66, 29, 0, 26.6, 0.351, 31]).

euclidean_distance([], [], 0).

euclidean_distance([X|Xs], [Y|Ys], Distance) :-
    euclidean_distance(Xs, Ys, PartialDistance),
    Difference is X - Y,
    Distance is PartialDistance + Difference * Difference.

main :-
    point1(P1),
    point2(P2),

    euclidean_distance(P1, P2, SumSquares),

    FinalDistance is sqrt(SumSquares),

    format('Euclidean Distance: ~3f~n', [FinalDistance]).

:- initialization(main).