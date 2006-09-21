#!/usr/bin/perl

open INFILE, "input.txt" or die;
$count=1;
@C;
@D;
@R;
@RD;
while ($line = <INFILE>) {
	chomp $line;
	if ($count > 1) {
		$in[1]=$line;
		@in=split /\t/, $line;
		$C[$count-1]=$in[1];
		$D[$count-1]=$in[2];
		$R[$count-1]=$in[3];
		$RD[$count-1]=$in[4];
	}
	$count++;
}

$id=1;
$count=0;
print "id", "\t", "grp", "\t", "time", "\n";

foreach $mouse (@C) {
	while ($mouse > 0) {
		print $id, "\t", "C", "\t", $count, "\n";
		$mouse--;
		$id++;
	}
	$count++;
}
$count=0;
foreach $mouse (@D) {
	while ($mouse > 0) {
		print $id, "\t", "D", "\t", $count, "\n";
		$mouse--;
		$id++;
	}
	$count++;
}
$count=0;
foreach $mouse (@R) {
	while ($mouse > 0) {
		print $id, "\t", "R", "\t", $count, "\n";
		$mouse--;
		$id++;
	}
	$count++;
}
$count=0;
foreach $mouse (@RD) {
	while ($mouse > 0) {
		print $id, "\t", "RD", "\t", $count, "\n";
		$mouse--;
		$id++;
	}
	$count++;
}
