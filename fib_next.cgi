#!"C:\xampp\perl\bin\perl.exe"

use strict;
use warnings;

# Read Fibonacci numbers from file
open my $fh, '<', 'fibonacci.txt' or die "Could not open file 'fibonacci.txt': $!";
my $line = <$fh>;
close $fh;

# Fibonacci numbers
my @fib_nums = split /,/, $line;

# Calculate next Fibonacci number
my $next_fib = $fib_nums[1] + $fib_nums[2];

# Update file with new sequence
open my $fh_out, '>', 'fibonacci.txt' or die "Could not open file 'fibonacci.txt' for writing: $!";
print $fh_out "$fib_nums[1],$fib_nums[2],$next_fib";
close $fh_out;

# Print HTML content with CSS
print "Content-type: text/html\n\n";
print "<!DOCTYPE html>\n";
print "<html>\n";
print "<head>\n";
print "<title>Fibonacci Sequence</title>\n";
print <<EOF;
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
EOF
print "</head>\n";
print "<body>\n";
print "<div class=\"container\">\n";
print "<h1>Fibonacci Sequence</h1>\n";
print "<p>Current Sequence: $fib_nums[1], $fib_nums[2], $next_fib</p>\n";
print "<a href=\"fib_prev.cgi\">Previous</a> | <a href=\"fib_next.cgi\">Next</a>\n";
print "</div>\n";
print "</body>\n";
print "</html>\n";
