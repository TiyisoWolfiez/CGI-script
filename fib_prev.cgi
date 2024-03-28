#!"C:\xampp\perl\bin\perl.exe"

use strict;
use warnings;

# Read Fibonacci numbers from file
open my $fh, '<', 'fibonacci.txt' or die "Could not open file 'fibonacci.txt': $!";
my $line = <$fh>;
close $fh;

# Parse Fibonacci numbers
my @fib_nums = split /,/, $line;

# Calculate previous Fibonacci number
my $prev_fib;

if ($fib_nums[0] == 0 && $fib_nums[1] == 1) {
    $prev_fib = '---';
} else {
    $prev_fib = $fib_nums[1] - $fib_nums[0];
}

# Update file with new sequence
open my $fh_out, '>', 'fibonacci.txt' or die "Could not open file 'fibonacci.txt' for writing: $!";
print $fh_out "$prev_fib,$fib_nums[0],$fib_nums[1]";
close $fh_out;

# Print HTML content with CSS
print "Content-type: text/html\n\n";
print <<EOF;
<!DOCTYPE html>
<html>
<head>
<title>Fibonacci Sequence</title>
<meta http-equiv="Cache-control" content="no-cache">
<style>
body {
    font-family: Arial, sans-serif;
    background-color: #f7f7f7;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: 0 auto;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

h1 {
    color: #333;
}

p {
    color: #555;
}

a {
    color: #007bff;
    text-decoration: none;
    margin-right: 10px;
}

a:hover {
    text-decoration: underline;
}
</style>
</head>
<body>
<div class="container">
<h1>Fibonacci Sequence</h1>
<p>Current Sequence: 

EOF

# Print previous Fibonacci number or '---' if less than 0
if ($prev_fib < 0) {
    print "---";
} else {
    print "$prev_fib";
}

print ", $fib_nums[0], $fib_nums[1]</p>\n";

# Check if 'Previous' should be disabled
if ($prev_fib eq '---') {
    print "<p>Previous<p>\n";
} else {
    print "<a href=\"fib_prev.cgi\">Previous</a>\n";
}

print "<a href=\"fib_next.cgi\">Next</a>\n";
print "</div>\n";
print "</body>\n";
print "</html>\n";
