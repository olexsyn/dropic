#!/usr/bin/perl

=head1 NAME

Скрипт заменяет стандартные иконки Dropbox на более наглядные

Примечание: для 16 и 64 битных версий линукса разные директории "...dropbox-lnx.x86_64..."

=cut

use strict;
use warnings 'all';
use File::Copy qw(copy);

$\ = "\n";

my $dest_dir     = "/home/olex/Dropbox/dropbox-icons";
my $drop_version = "/home/olex/.dropbox-dist/VERSION";
my $img_dir      = "/home/olex/.dropbox-dist/dropbox-lnx.x86_64-%VERSION%/images/hicolor/16x16/status";

my @files = qw(
	dropboxstatus-blank.png
	dropboxstatus-busy.png
	dropboxstatus-busy2.png
	dropboxstatus-idle.png
	dropboxstatus-logo.png
	dropboxstatus-x.png
);

open(DROPVFILE, $drop_version) || die "Error open of $drop_version; $!";
my $version = <DROPVFILE>;
close(DROPVFILE);

$img_dir =~ s/%VERSION%/$version/;

my $removed = unlink( map {$img_dir.'/'.$_} @files );
print "Removed $removed file(s).";

my $i = 0;
foreach my $fil (@files)
{
	copy $dest_dir.'/'.$fil, $img_dir.'/'.$fil;
	$i++;
}
print "Successfully copied $i file(s).";

exit 0;
