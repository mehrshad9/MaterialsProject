

class materialpro:
    def __init__(self, Mat,key1="kI8OEewx6FTbDV4A"):
        import requests
        import json
        import pandas as pd
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
        




