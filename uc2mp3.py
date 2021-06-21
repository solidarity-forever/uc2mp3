#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""convert netease music cache file (.uc) to mp3"""


def uc2mp3(file_path):

	with open(file_path, 'rb') as fi, open(file_path + '.mp3', 'wb') as fo:

		while True:
			b = fi.read(1024)
			if not b:
				break
			b = bytes(map(lambda a: a ^ 0xa3, [x for x in b]))
			fo.write(b)


if __name__ == '__main__':
	import sys

	uc2mp3(sys.argv[1])
