# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 22:51:48 2020

@author: mmehboudi
"""
import materialpro
a=materialpro.VaspInputs()
lv=[[0.5, 0.5, 0.5 ], [0.0, 0.0 ,0.0]]
a.poscar_selec_dyn(a1=[0,1,1],a2=[1,0,1],a3=[1,1,0],species_vec=[1,1], lattice_cons=3.57, basis_vec= lv)

coords= a.unit_2_super(a1=[0,1,1],a2=[1,0,1],a3=[1,1,0],basis_vec= lv,nx=2,ny=3,nz=4)

a.parse_POSCAR()

a.write_xyz(coords.values.tolist())
#print(coords.values.tolist())
print(coords)
print()

