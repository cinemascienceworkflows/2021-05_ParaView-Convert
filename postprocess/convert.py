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

print(indir)
print(outdir)
os.mkdir(os.path.join(outdir, cdbbase))

reader = vtkStructuredPointsReader()
dims = []
for f in glob.glob("{}/*.vtk".format(indir)):
    reader.SetFileName(f)
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()

    data = reader.GetOutput()

    dims = data.GetDimensions()

    u = VN.vtk_to_numpy(data.GetPointData().GetArray('scalars'))
    unewshape = numpy.reshape(u, (dims[1], dims[0]))
    unewtrans = unewshape.transpose()
    unew      = numpy.fliplr(unewtrans)
    basename = os.path.basename(f)
    basename = re.sub('\.vtk$', '', basename)
    fullpath = os.path.join(outdir, cdbbase, basename + ".npz")
    print(fullpath)
    numpy.savez_compressed(fullpath, data=unew)

# update the data.csv file
oldcsv = os.path.join(indir, "data.csv")
newcsv = os.path.join(outdir, cdbbase, "data.csv")

print(oldcsv)
print(newcsv)
with open(oldcsv, 'r') as ofile, open(newcsv, 'w') as nfile:
    first = ofile.readline()
    clean = first.strip()
    newline = re.sub('\_vtk$', '', clean)
    nfile.write(newline)
    nfile.write(",CISVersion,CISImage,CISImageWidth,CISImageHeight,CISLayer,CISLayerWidth,CISLayerHeight,CISLayerOffsetX,CISLayerOffsetY,CISChannel,CISChannelVar")
    nfile.write("\n")

    lines = ofile.readlines()
    curimage = 0
    for l in lines:
        clean = l.strip()
        newline = re.sub('\.vtk$', '.npz', clean)
        nfile.write(newline)
        nfile.write(",\"1.0\",i{},{},{},l000,{},{},0,0,scalars,scalars\n".format(f'{curimage:03}', dims[0], dims[1], dims[0], dims[1]))
        curimage = curimage + 1
