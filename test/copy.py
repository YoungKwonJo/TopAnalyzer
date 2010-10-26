#!/usr/bin/env python
# Author: Tae.Jeong.Kim@cern.ch
# Filename: analysis.py
# How to run: ./copy.py status mc ElEl 
import os
import re
import sys
import time

input = sys.argv[1]
dataormc =sys.argv[2] 
type = sys.argv[3]

if dataormc == "mc":
  dir = "/castor/cern.ch/user/t/tjkim/ntuple/top/"+type+"/MC/Spring10"
  destination = "/home/tjkim/ntuple/top/"+type+"/MC/Spring10"

  if type == "MuMu":
    list = ["ZJets", "Ztautau", "WJets", "VVJets", "TTbar", "SingleTop", "Zmumu", "DYmumu","InclusiveMu15"]
  elif type == "ElEl":
    list = ["ZJets", "Ztautau", "WJets", "VVJets", "TTbar", "SingleTop", "Zee", "DYee"]
  elif type == "MuEl":
    list = ["ZJets", "Ztautau", "WJets", "VVJets", "TTbar", "SingleTop"]
  else: 
    print "wrong type"
elif dataormc == "data":
  dir = "/castor/cern.ch/user/t/tjkim/ntuple/top/"+type+"/RD/Oct6"
  destination = "/home/tjkim/ntuple/top/"+type+"/RD/Oct6"
  list = ["data_1","data_2"]
else:
  print "data or mc?"  

def copySample(dir,sample,destination):
  os.system("rm -rf "+destination+"/"+sample)
  os.system("mkdir "+destination+"/"+sample)
  os.system("rfcpMany.py "+dir+"/"+sample+" "+destination+"/"+sample+" \".*root\"")

if input == "status":
  print dir
  os.system("rfdir "+dir)
  for s in list:
    os.system("ls "+destination+"/"+s+" | wc -l")
  print destination
  os.system("ls -al "+destination)
elif input == "run":
  for s in list:
    copySample(dir,s,destination)
elif input == "merge":
  if dataormc == "mc":
    for s in list:
      os.system("hadd -f "+destination+"/vallot_"+s+".root "+destination+"/"+s+"/vallot_*.root")
  if dataormc == "data":
    os.system("hadd -f "+destination+"/vallot.root "+destination+"/data*/vallot_*.root")
elif input =="remove":
  for s in list:
    os.system("rm -r "+destination+"/"+s)
else:
  print "with 'status' or 'run'"
