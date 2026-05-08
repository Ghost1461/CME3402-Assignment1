point1 = [6, 148, 72, 35, 0, 33.6, 0.627, 50]
point2 = [1, 85, 66, 29, 0, 26.6, 0.351, 31]

sum = 0

for i in 0...point1.length
  difference = point1[i] - point2[i]
  sum += difference ** 2
end

distance = Math.sqrt(sum)

puts "Euclidean Distance: #{format('%.3f', distance)}"