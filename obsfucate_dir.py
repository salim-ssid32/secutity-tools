#!/usr/bin/python3
# This script is written by ssid32
import os
from sys import argv
import re

action = 0



def usage():
  print(f'\nUsage:\n      python3 {argv[0]} [Option] /path/to/thedir\n\n     -c : Create random name for '\
  'all directories\n     -d : Delete the random name created with this script for all directories\n'\
  f'Examples : \n     python3 {argv[0]} -c /tmp\n     python3 {argv[0]} -d /var/www/html')
  exit()


if len(argv) != 3:
  usage()
  


def getName(name):
  return name+'_obs_'+os.urandom(10).hex()
  
def getdir(path):
  out=[]
  for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
      out.append(os.path.join(path, i))
  return out

def isNamed(i):
  d = re.match(r'.*_obs_.{20}$',i,re.M)
  if d:
    return True
  return False

def rename(dirs):
  global action
  for i in dirs:
    if isNamed(i):
      continue
    os.rename(i,getName(i))
    action+=1

def getOrigineName(i):
  return i[:-25]


def originalName(dirs):
  global action
  for i in dirs:
    if isNamed(i):
      os.rename(i,getOrigineName(i))
      action+=1


if '-d' == argv[1] :
  dirs  = getdir(argv[2])
  originalName(dirs)
  print(f'{action} dirs have been renamed')
  exit()

if '-c' == argv[1] :
  dirs  = getdir(argv[2])
  rename(dirs)
  print(f'{action} dirs have been renamed')
  exit()
usage()
