#!/usr/bin/env python
# aoi.py
# This class represents an AOI

# system includes
import sys
import math
import numpy as np

class AOI:
  def __init__(self,x,y,w,h):
    self.xy = (x,y)
#   self.xy = (x,y-h)
    self.width = w
    self.height = h

#   old:
#   self.label = None

#   new (attributes):
#   can add whatever in Scribus, e.g.,
    self.attr = {}
#   self.attr['label'] = 'None'

    self.vertices = []

    self.vertices.append((x,y))
    self.vertices.append((x+w,y))
    self.vertices.append((x+w,y+h))
    self.vertices.append((x,y+h))
#   self.vertices.append((x,y-h))
#   self.vertices.append((x+w,y-h))
#   self.vertices.append((x+w,y))
#   self.vertices.append((x,y))

  def setAttributes(self,attr):
    self.attr = attr

  def getAttribute_astring(self,key):
    aoistr = ""
    if self.attr[key]:
      aoistr += self.attr[key]
    return aoistr

  def getAttributes_astring(self):
    aoistr = ""
    for i, (k, v) in enumerate(self.attr.items()):
      if i < len(self.attr)-1:
        aoistr += v + ','
      else:
        aoistr += v
    return aoistr

  def getAOILabel(self):
    self.dump()
# this is the way I'd normally do it, using AOI name 'location' and
# value being the aoi order
#   return self.attr['location']
# here's the HACK instead:
    attrnam = self.getAttribute_astring('Name')
    attrval = self.getAttribute_astring('Value')
    attrord = int(attrnam[1:]) if attrnam[0] == 'a' else 0
    return attrord

  def getLocation(self):
# this is the way I'd normally do it, using AOI name 'location' and
# value being the aoi order
#   return int(self.attr['location'])
# here's the HACK instead:
    attrnam = self.getAttribute_astring('Name')
    attrval = self.getAttribute_astring('Value')
    attrord = int(attrnam[1:]) if attrnam[0] == 'a' else 0
    return attrord

  def getXY(self,h=None):
    if h is not None:
      return (self.xy[0],float(h) - self.xy[1])
    else:
      return self.xy

  def getWidth(self):
    return self.width

  def getHeight(self):
    return self.height

  def dump(self):
#   for i in range(len(self.vertices)):
#     print self.vertices[i]
#   old:
#   print(self.label, ": (x,y), (w,h) = ", self.xy, ",", self.width, ",", self.height)
#   new (attributes):
    print("(x,y), w, h = ", self.xy, ",", self.width, ",", self.height)
#   print("AOI attributes:")
    for k, v in self.attr.items():
      print(k,v)
		
  def inside(self,x,y):

    theta = 0
    epsilon = 0.0001

    n = len(self.vertices)

    for i in range(n):
      # an np.array([x,y]) is a 2D vector
      v1 = np.array([self.vertices[i][0] - x,self.vertices[i][1] - y])

      # don't forget the angle between the last and first vertex
      if (i+1) < n:
        v2 = np.array([self.vertices[i+1][0] - x,self.vertices[i+1][1] - y])
      else:
        v2 = np.array([self.vertices[0][0] - x,self.vertices[0][1] - y])

      # get dot product
      dot = np.dot(v1,v2)
      v1_modulus = np.sqrt((v1*v1).sum())
      v2_modulus = np.sqrt((v2*v2).sum())
      # cos of angle between x and y
      cos_angle = dot / (v1_modulus * v2_modulus)
      angle = np.arccos(cos_angle)

      # accumulate angle
      theta = theta + angle

    # check to see if we have 360 degrees
#   if abs(theta*180.0/math.pi - 360.0) < epsilon:
    if abs(theta - 2.0*math.pi) < epsilon:
      return True
    else:
      return False
