#!/usr/bin/python

"""
Скрипт заменяет стандартные иконки Dropbox на более наглядные
Примечание: для 32 и 64 битных версий линукса разные директории,
напр.: "...dropbox-lnx.x86_64..."

"""

import shutil as sh
from os      import mkdir, rmdir
from sys     import exit
from pathlib import Path

home = str(Path.home())

src_dir      = home + "/Dropbox/dropbox-icons"
drop_version = home + "/.dropbox-dist/VERSION"
img_dir      = home + "/.dropbox-dist/dropbox-lnx.x86_64-{{VERSION}}/images/hicolor/16x16/status"

files = (
	'dropboxstatus-blank.png',
	'dropboxstatus-busy.png',
	'dropboxstatus-busy2.png',
	'dropboxstatus-idle.png',
	'dropboxstatus-logo.png',
	'dropboxstatus-x.png',
)


with open(drop_version,'r') as f:
	version = f.read()
f.close()

print('Dropbox version:', version)
img_dir = img_dir.replace('{{VERSION}}', version);

print('Backup original icons... ', end='')
try:
	mkdir(img_dir + '/backup', mode=0o755)
except FileExistsError as e:
	print('(backup directory already exists)', end=' - ')

try:
	for item in files:
		sh.move(img_dir + '/' + item, img_dir + '/backup/' + item)
	print('OK')
except Exception as e:
	print("Can't move icons to backup! - Fail!")
	exit(1)


print('Copy new icons... ', end='')
try:

	for item in files:
		sh.copy(src_dir + '/' + item, img_dir)
	print('OK')

except Exception as e:

	print("Can't copy new icons! - Fail!")
	print('Restore original icons... ', end='')
	try:
		for item in files:
			sh.move(img_dir + '/backup/' + item, img_dir + '/' + item)
		print('OK')
	except Exception as e:
		print("Can't restore icons from backup! - Fail!")
		print("Please restore them handly:", img_dir + '/backup')
		exit(1)

	print('Delete backup directory... ', end='')
	try:
		rmdir(img_dir + '/backup/')
		print('OK')
	except Exception as e:
		print("Can't delete backup directory! - Fail!")
		exit(1)
