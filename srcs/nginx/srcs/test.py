#!/usr/bin/python3
import os    # 既存ファイルの有無を確認するため
import sys    # exit()するため

def print_header():
	print('Content-Type: text/html')
	print('')
	print('<!DOCTYPE html>')
	print('')
	print('<html lang="ja">')
	print('')
	print('<head>')
	print('  <meta charset="UTF-8">')
	print('  <meta name="description" content="file upload">')
	print('  <meta name="keywords" content="upload">')
	print('  <title>File upload</title>')
	print('</head>')
	print('')
	print('<body>')

def print_footer():
	print('</body>')
	print('')
	print('</html>')
	sys.exit(0)

print_header()
print("Hello world")
print_footer()