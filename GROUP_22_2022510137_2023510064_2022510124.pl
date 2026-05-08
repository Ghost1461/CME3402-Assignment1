use strict;
use warnings;

my @point1 = (6, 148, 72, 35, 0, 33.6, 0.627, 50);
my @point2 = (1, 85, 66, 29, 0, 26.6, 0.351, 31);

my $sum = 0;

for (my $i = 0; $i < scalar(@point1); $i++) {
    my $difference = $point1[$i] - $point2[$i];
    $sum += $difference * $difference;
}

my $distance = sqrt($sum);

print "Euclidean Distance: $distance\n";