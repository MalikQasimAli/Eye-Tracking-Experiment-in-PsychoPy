#!/usr/bin/env python3

import sys, os, math

def catCSVFile(infile,df,ct):
  try:
    f = open(infile,'r')
  except IOError:
    print("Can't open file: " + infile)
    return

  path, base = os.path.split(infile)

  print("Processing: ", infile, "[", base, "]")

  # split filename from extension
  filename, ext = os.path.splitext(base)

  print("path, base, filename, ext: ", path, base, filename, ext)

  # extract stimulus name and subj id
  # filename now has the form 'date-rest_of_it', extract just the second part
  subj = filename.split('-')[0]
  exp_id = filename.split('-')[1]
  ses_id = filename.split('-')[2]
  stim = filename.split('-')[3]

  # HACK: override exp_id with first part of stim and ses_id with trailing
  #       numeral, e.g., if stim is 'tcq01', exp_id is 'tcq' and ses_id is 1.
  exp_id = stim[:3]
  ses_id = int(stim[3:])

  print("subj, exp_id, ses_id, stim: ", \
         subj, exp_id, ses_id, stim)

  # read lines, throwing away first one (header)
# linelist = f.readlines()
# linelist = f.read().split('\r')
  linelist = f.read().splitlines()
  header = linelist[0].split(',')
  linelist = linelist[1:]

  # timestamp,x,y,duration,prev_sacc_amplitude,aoi_label
  for idx, label in enumerate(header):
    if label.strip() == "timestamp":
      TIMESTAMP = idx
    if label.strip() == "x":
      X = idx
    if label.strip() == "y":
      Y = idx
    if label.strip() == "duration":
      DURATION = idx
    if label.strip() == "prev_sacc_amplitude":
      PREV_SACC_AMPLITUDE = idx
    if label.strip() == "aoi_span":
      AOI_SPAN = idx
    if label.strip() == "aoi_order":
      AOI_ORDER = idx
    if label.strip() == "aoi":
      AOI = idx

  for line in linelist:
    entry = line.split(',')

    # get line elements
    timestamp = entry[TIMESTAMP]
    x  = entry[X]
    y  = entry[Y]
    duration  = entry[DURATION]
    prev_sacc_amplitude  = entry[PREV_SACC_AMPLITUDE]
    aoi_span  = entry[AOI_SPAN]
    aoi_order  = entry[AOI_ORDER]
    # text label
    aoi_label  = entry[AOI]
    # for TMs need numerical code
    if aoi_label == "Instruction" or aoi_label == "argument":
      aoi = 1
    if aoi_label == "A" or aoi_label == "operator":
      aoi = 2
    if aoi_label == "B" or aoi_label == "function":
      aoi = 3
    if aoi_label == "C" or aoi_label == "variable":
      aoi = 4
    if aoi_label == "D" or aoi_label == "object":
      aoi = 5
    if aoi_label == "E" or aoi_label == "content":
      aoi = 6

    str = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d,%s" % ( \
                         subj, \
                         exp_id, \
                         ses_id, \
                         stim, \
                         timestamp,\
                         x,y,\
                         duration,\
                         prev_sacc_amplitude,\
                         aoi_span,\
                         aoi_order,\
                         aoi_label,\
                         aoi,\
                         ct)
    print(str, file=df)
    ct += 1

  return ct

###############################################################################

# clear out output file
df = open("fxtn-aois.csv",'w')
print("subj,exp_id,ses_id,stim,timestamp,x,y,duration,prev_sacc_amplitude,aoi_span,aoi_order,aoi_label,aoi,order", file=df)

dir = './data/'

# find all files in dir with .csv extension
lst = [a for a in os.listdir(dir) if a.endswith('-fxtn-aoi.csv')]

lineno = 1

for item in lst:

  file = dir + item
  print('Processing ', file)

  # cat csv files into one
  lineno = catCSVFile(file,df,lineno)

df.close()
