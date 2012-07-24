#!/usr/bin/perl -w
#
# Sometimes you need a lowest common denominator type of solution
# and this is one of them. A script for sending email via an SMTP
# server, written in Perl.
#
# Inspired by the example code in http://www.xav.com/perl/site/lib/Net/SMTP.html
#
# This script is public domain. Do with it anything you like.
#
# Needless to say the software is provided "as is". There is no warranty of any kind
# and it's not guaranteed to work anywhere but the original environment it was used in.

use strict;
use Net::SMTP;
use Text::ParseWords;

$#ARGV >= 3 or die "Usage: send_email <server> <from_addr> <subject> <to_addr> [<to_addr> ...]";

my $server = shift; # host name or ip address
my $from = shift; # email address
my $subject = shift;
my @to;
my $line;

my $smtp = Net::SMTP->new($server);
$smtp->mail($from);

foreach my $argnum (0 .. $#ARGV) { push(@to, $ARGV[$argnum]); }
$smtp->to(@to);

$smtp->data();
$smtp->datasend("To: " . join(", ", @to) . "\n");
$smtp->datasend("Subject: " . $subject . "\n");
$smtp->datasend("\n");
while (defined($line = <STDIN>)) {
    $smtp->datasend($line . "\n");
}
$smtp->dataend();

$smtp->quit;

