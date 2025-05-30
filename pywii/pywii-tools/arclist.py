#!/usr/bin/env python2

import sys, os, os.path, struct
import pywii as wii
with open(sys.argv[1], "rb") as arc:
    
    tag, fstoff, fstsize, dataoff = struct.unpack(">IIII16x",arc.read(0x20))
    
    arc.seek(fstoff)
    fst = arc.read(fstsize)

fst = wii.WiiFST(fst)

fst.show()
