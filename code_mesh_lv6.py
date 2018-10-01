import requests
import itertools
import pandas as pd
import jismesh.utils as ju
from bs4 import BeautifulSoup as Soup

df = pd.read_csv("lv6mesh.csv")
df.columns = ["no","code"]
res = df.iloc[0:,1]

def create_polygon(meshcode):
    """
    create polygon for corresponding mesh code
    """
    lat1,lon1 = ju.to_meshpoint(meshcode,0,0)
    lat2,lon2 = ju.to_meshpoint(meshcode,1,1)
    poly_text = 'POLYGON (('+str(lon1)+' '+str(lat1)+','+str(lon1)+' '+str(lat2)+','+str(lon2)+' '+str(lat2)+','+str(lon2)+' '+str(lat1)+','+str(lon1)+' '+str(lat1)+'))'
    return poly_text

listpoly = []
for row in res:
    listpoly.append(create_polygon(row))
code_list1 = pd.DataFrame(df, columns = ['meshcode'])
code_list2 = pd.DataFrame(listpoly, columns = ['geometry'])
code_list = pd.concat([code_list1,code_list2], axis=1)
code_list['meshcode'] = code_list['meshcode'].astype(str)
code_list.to_csv("lv6meshwithcode.csv", index=None)
print("all done")
