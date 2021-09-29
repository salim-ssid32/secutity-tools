#!/usr/bin/python3
# This script is written by ssid32

import os
from sys import argv

content = '<!DOCTYPE html>\n<html><head>\n<title>Nothing here...</title>\n</head><body>\n<h1>Nothing here...</h1>\n<p>There is nothing here. Please go back.</p>\n<hr>\n<address>Nothing here...</address>\n</body></html>'
action = 0
def usage():
  print(f'\nUsage:\n      python3 {argv[0]} [Option] /path/to/thedir\n\n     -c : Create index.html files in '\
  'all directories\n     -d : Delete index.html files created with this script in all directories\n'\
  f'Examples : \n     python3 {argv[0]} -c /tmp\n     python3 {argv[0]} -d /var/www/html')
  exit()
if len(argv) != 3:
  usage()

def createIndex(path):
  global action
  open(path+'/index.html','w').write(content)
  action+=1

def deleteIndex(path):
  global action
  if not isExistIndexHtml(path):
    return
  if content == open(path+'/index.html').read():
    os.remove(path+'/index.html')
    action+=1

def isExistIndexHtml(path):
  if os.path.exists(path+'/index.html'):
    return True
  return False

def isExistIndex(inp):
  if 'index.php' in inp or 'index.html' in inp:
    return True
  return False

if '-d' == argv[1] :
  for dirname, dirnames, filenames in os.walk(argv[2]):
    if isExistIndex(filenames):
      deleteIndex(dirname)
  print(f'{action} index files have been deleted')
  exit()

if '-c' == argv[1] :
  for dirname, dirnames, filenames in os.walk(argv[2]):
    if not isExistIndex(filenames):
      createIndex(dirname)
  print(f'{action} index files have been created')
  exit()
usage()


