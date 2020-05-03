#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""convert netease music cache file (.uc) to mp3"""

import sys


def uc2mp3(file_path):
	fi = open(file_path, 'rb')
	fo = open(file_path + '.mp3', 'wb')

	while True:
		b = fi.read(1024)
		if not b:
			break
		b = bytes(list(map(lambda a: a ^ 0xa3, [x for x in b])))
		fo.write(b)

	fi.close()
	fo.close()


if __name__ == '__main__':
	uc2mp3(sys.argv[1])
