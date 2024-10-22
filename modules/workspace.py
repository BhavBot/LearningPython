#/\/\/\
import calc
print("from import: ",calc.add(200,199))
print("from import: ",calc.mine(123,412))
import sys
print("my part where i look for the modules is: ",sys.path)
import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
import functions
x=functions.recursionmeth(12)
print(x)
#is a factorial a multidimensional spiral
import complex.thecalc as comp
print("nested modules",comp.mult(0,1231234125423431425362341234),comp.div(123413123413124,0))
from complex.thecalc import div
print("example of importing a sinlge method: ",div(123,3))
print("workspace.py: the name of my module is: ",__name__)
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

