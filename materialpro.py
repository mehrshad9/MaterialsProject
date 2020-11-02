#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[76]:


import pandas as pd
import requests
import json
class MaterialPro:    
    def __init__(self, Mat,key1="kI8OEewx6FTbDV4A"):
        URL1="https://www.materialsproject.org/rest/v2/materials/"
        self.Mat=Mat
        self.key1=key1
        URL2="/vasp?API_KEY="
        url=URL1+Mat+URL2+key1        
        def getResponse(self):
            r1 = requests.get(url)
            if(r1.status_code==200):
                data1=r1.json()
            else:
                print("Error receiving data", r1.status_code())
            return data1
        self.data1=getResponse(url)
        self.N=len(self.data1['response'])
        self.options=list(self.data1['response'][0].keys())
        self.NOp=len(self.options)
        
    def get_option(self,option):
        for i in range(self.NOp):
            if option == self.options[i]:
                list1=[]
                for j in range (self.N):
                    list1.append(self.data1['response'][j][option])
        return(list1)
            
    def get_df(self):
        dic1={}
        for op in self.options:
            dic1[op]=self.get_option(op)
        return pd.DataFrame(dic1)   
    
        


# In[ ]:





# In[181]:


class VaspInputs:
    def __init__(self):
        pass
    def poscar_selec_dyn( self,a1,a2,a3,species_vec,basis_vec,lattice_cons=1,Comment ='Comment'):
        fw=open('POSCAR','w')
        fw.write(Comment)
        fw.write('\n  {}'.format(float(lattice_cons)))
        fw.write('\n  {} {} {}'.format(float(a1[0]),float(a1[1]),float(a1[2])))
        fw.write('\n  {} {} {}'.format(float(a2[0]),float(a2[1]),float(a2[2])))
        fw.write('\n  {} {} {}\n'.format(float(a3[0]),float(a3[1]),float(a3[2])))
        fw.write(' '.join([str(x) for x in species_vec]))
        fw.write('\n Selective dynamics \n Cartesian \n')
        for b in basis_vec:
            fw.write(' '.join([str(x) for x in b]))
            fw.write('\n')
        
    def plot_bandgap(self):
        pass
    def bandgap(self):
        pass
    def poscar2unitcell(self):
        pass
    def unit_2_super(self,a1,a2,a3,basis_vec,nx = 1,ny = 1,nz = 1):
        counter=0
        nb=len(basis_vec)
        coords = [[0 for col in range(3)] for row in range(nx*ny*nz*nb)]
        for i in range(nx):
            for j in range(ny):
                for m in range(nz):
                    for k in range(1,nb+1):                  
                        counter+=1
                        coords[counter]=[i*a[1][s]+j*a[2][s]+m*a[3][s]+b[k][s] for s in range(2)]
            


# In[ ]:





# In[182]:


a=VaspInputs()


# In[183]:


lv=[[0.5, 0.5, 0.5 ], [0.0, 0.0 ,0.0]]


# In[184]:


a.poscar_selec_dyn(a1=[0,1,1],a2=[1,0,1],a3=[1,1,0],species_vec=[1,1], lattice_cons=3.57, basis_vec= lv)


# In[ ]:





# In[ ]:




