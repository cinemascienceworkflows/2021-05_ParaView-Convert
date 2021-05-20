from paraview.simple import *
import numpy
from vtk import vtkStructuredPointsReader
from vtk.util import numpy_support as VN
import glob
import os
import shutil
import re
import sys

indir   = ""
outdir  = ""
cddbase = ""

if (len(sys.argv) == 3):
    indir  = sys.argv[1]
    outdir = sys.argv[2]
    cdbbase = os.path.basename(indir) 
else:
    print("ERROR: must provide indir and outdir")

os.mkdir(os.path.join(outdir, cdbbase))

reader = vtkStructuredPointsReader()
for f in glob.glob("{}/*.vtk".format(indir)):
    reader.SetFileName(f)
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()

    data = reader.GetOutput()

    dim = data.GetDimensions()
    vec = list(dim)
    vec = [i-1 for i in dim]
    vec.append(3)

    u = VN.vtk_to_numpy(data.GetPointData().GetArray('scalars'))
    basename = os.path.basename(f)
    basename = basename.split(".")[0]
    fullpath = os.path.join(outdir, cdbbase, basename + ".npz")
    print(fullpath)
    numpy.savez_compressed(fullpath, data=u)

# update the data.csv file
oldcsv = os.path.join(indir, "data.csv")
newcsv = os.path.join(outdir, cdbbase, "data.csv")

print(oldcsv)
print(newcsv)
with open(oldcsv, 'r') as ofile, open(newcsv, 'w') as nfile:
    lines = ofile.readlines()
    for l in lines:
        clean = l.strip()
        newline = re.sub('\.vtk$', '.npz', clean)
        nfile.write(newline)
        nfile.write("\n")
