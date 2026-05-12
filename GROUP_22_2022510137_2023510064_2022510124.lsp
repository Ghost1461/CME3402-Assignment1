(setq point1 '(6 148 72 35 0 33.6 0.627 50))
(setq point2 '(1 85 66 29 0 26.6 0.351 31))

(setq sum-squares 0)

(loop for x in point1
      for y in point2
      do (setq sum-squares
               (+ sum-squares
                  (* (- x y) (- x y)))))

(setq distance (sqrt sum-squares))

(format t "Euclidean Distance: ~,3f~%" distance)