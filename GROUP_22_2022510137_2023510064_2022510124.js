let point1 = [6, 148, 72, 35, 0, 33.6, 0.627, 50];
let point2 = [1, 85, 66, 29, 0, 26.6, 0.351, 31];

let sum = 0;

for (let i = 0; i < point1.length; i++) {
    let difference = point1[i] - point2[i];
    sum += difference * difference;
}

let distance = Math.sqrt(sum);

console.log("Euclidean Distance:", distance);