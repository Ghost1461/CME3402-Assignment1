fn main() {
    let point1 = [6.0, 148.0, 72.0, 35.0, 0.0, 33.6, 0.627, 50.0];
    let point2 = [1.0, 85.0, 66.0, 29.0, 0.0, 26.6, 0.351, 31.0];

    let mut sum_squares = 0.0;

    for i in 0..point1.len() {
        let difference = point1[i] - point2[i];
        sum_squares += difference * difference;
    }

    let distance = f64::sqrt(sum_squares);

    println!("Euclidean Distance: {:.3}", distance);
}