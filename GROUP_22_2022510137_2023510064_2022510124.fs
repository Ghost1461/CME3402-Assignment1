let point1 = [| 6.0; 148.0; 72.0; 35.0; 0.0; 33.6; 0.627; 50.0 |]
let point2 = [| 1.0; 85.0; 66.0; 29.0; 0.0; 26.6; 0.351; 31.0 |]

let mutable sum = 0.0

for i in 0 .. point1.Length - 1 do
    let difference = point1.[i] - point2.[i]
    sum <- sum + difference * difference

let distance = sqrt sum

printfn "Euclidean Distance: %f" distance