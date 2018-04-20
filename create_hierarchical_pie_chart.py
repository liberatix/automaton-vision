#!/usr/bin/python
from pprint import *
import json

file = open('coggle/automaton-vision.txt', 'r') 
lines = file.readlines()

mindmap = { 'groups': [], 'label': 'Root' }
levels = [ mindmap ]

for line in lines:
  if len(line) < 3:
    continue
  level = line.count('\t')
  if level == 0:
    continue
  cur_level = len(levels) - 1
  label = line.strip()
  item = { 'label': label, 'weight': 1 }
  if level > cur_level:
    if not 'groups' in levels[-1]:
      print " " * level + "Creating " + label + " under " + levels[-1]['label']
      levels[-1]['groups'] = [item]
    else:
      print " " * level + "Adding " + label + " to " + levels[-1]['label']
      levels[-1]['groups'].append(item)
    levels.append(item)
    continue
  elif level == cur_level:
    print " " * level + "Appending " + label + " under " + levels[-1]['label']
    levels[-2]['groups'].append(item)
    levels[-1] = item
    continue
  levels = levels[:level]
  levels[-1]['groups'].append(item)
  levels.append(item)

print json.dumps(mindmap)
