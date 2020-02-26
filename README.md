# dropic
Change Dopbox icons for better visibility

## NAME

What is `DROPIC` means? **DROP**box + **IC**ons

## FILES

- `dropic.pl` - Perl script
- `dropic.py` - Python script
- `/dropbox-icons/*.png` - directory with icons

## ICONS

filename | icon | description
-------- |:----:| -----------
`dropboxstatus-blank.png` | ![blank](/dropbox-icons/dropboxstatus-blank.png) | blank icon here
`dropboxstatus-x.png`     | ![x](/dropbox-icons/dropboxstatus-x.png)         | some error
`dropboxstatus-logo.png`  | ![logo](/dropbox-icons/dropboxstatus-logo.png)   | initialisation or syncing paused or connection lost
`dropboxstatus-busy.png`  | ![busy](/dropbox-icons/dropboxstatus-busy.png)   | syncing process (two icons that change alternately...
`dropboxstatus-busy2.png` | ![busy](/dropbox-icons/dropboxstatus-busy2.png)  | ...and creating a visual animation effect)
`dropboxstatus-idle.png`  | ![idle](/dropbox-icons/dropboxstatus-idle.png)   | syncing completed

## USAGE

`perl dropic.pl` or `python dropic.py`

Set properties `777` for scripts and check your system paths to the interpritors `#!/usr/bin/perl` or `#!/usr/bin/python`
(in the first line of script) to be able simply to run scripts as

`./dropic.pl` or `./dropic.py`
