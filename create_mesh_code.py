import requests
import pandas as pd
import jismesh.utils as ju
from bs4 import BeautifulSoup as Soup

def create_polygon(meshcode):
    """
    create polygon for corresponding mesh code
    """
    lat1,lon1 = ju.to_meshpoint(meshcode,0,0)
    lat2,lon2 = ju.to_meshpoint(meshcode,1,1)
    poly_text = 'POLYGON (('+str(lon1)+' '+str(lat1)+','+str(lon1)+' '+str(lat2)+','+str(lon2)+' '+str(lat2)+','+str(lon2)+' '+str(lat1)+','+str(lon1)+' '+str(lat1)+'))'
    return poly_text

def create_lv1():
    """
    create lv1 mesh code of japan
    parsing the data from html to get the lv1 code
    """
    print("parsing...")
    html = requests.get("http://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-L03-b.html")
    soup = Soup(html.content,"html.parser")
    listcode = []
    notlist = ['3035','3923','3924','3931','3941','4026','4041','4140','4141','4228','4827','6740']
    dataoption = soup.find_all("option")

    for option in dataoption:
        code = option.text
        listcode.append(code)
    print("editing...")
    listcode = [x for x in listcode if x not in notlist]
    listpoly = []
    for code in listcode:
        listpoly.append(create_polygon(code))
    code_list1 = pd.DataFrame(listcode, columns = ['meshcode'])
    code_list2 = pd.DataFrame(listpoly, columns = ['geometry'])
    code_list = pd.concat([code_list1,code_list2], axis=1)
    code_list.to_csv("lv1meshwithcode.csv", index=None)
    print("lv1 done")
    return listcode

def create_lv2():
    """
    create lv2 mesh code based on lv1 mesh code
    """
    listcode = create_lv1()
    lv2list = []
    listpoly = []
    for code in listcode:
        for i in range(8):
            for j in range(8):
                lv2list.append(code+str(i)+str(j))
    for code in lv2list:
        listpoly.append(create_polygon(code))
    code_list1 = pd.DataFrame(lv2list, columns = ['meshcode'])
    code_list2 = pd.DataFrame(listpoly, columns = ['geometry'])
    code_list = pd.concat([code_list1,code_list2], axis=1)
    code_list.to_csv("lv2meshwithcode.csv", index=None)
    print("lv2 done")
    return lv2list

def create_lv3():
    """
    create lv3 mesh code based on lv2 mesh code
    """
    lv2list = create_lv2()
    lv3list = []
    listpoly = []
    for code in lv2list:
        for i in range(10):
            for j in range(10):
                lv3list.append(code+str(i)+str(j))
    for code in lv3list:
        listpoly.append(create_polygon(code))
    code_list1 = pd.DataFrame(lv3list, columns = ['meshcode'])
    code_list2 = pd.DataFrame(listpoly, columns = ['geometry'])
    code_list = pd.concat([code_list1,code_list2], axis=1)
    code_list.to_csv("lv3meshwithcode.csv", index=None)
    print("lv3 done")
    return lv3list


def create_lv4():
    """
    create lv4 mesh code based on lv3 mesh code
    """
    lv3list = create_lv3()
    lv4list = []
    listpoly = []
    for code in lv3list:
        for i in range(4):
            lv4list.append(code+str(i+1))
    for code in lv4list:
        listpoly.append(create_polygon(code))
    code_list1 = pd.DataFrame(lv4list, columns = ['meshcode'])
    code_list2 = pd.DataFrame(listpoly, columns = ['geometry'])
    code_list = pd.concat([code_list1,code_list2], axis=1)
    code_list.to_csv("lv4meshwithcode.csv", index=None)
    print("lv4 done")
    return lv4list

def create_lv5():
    """
    create lv5 mesh code based on lv5 mesh code
    """
    lv4list = create_lv4()
    lv5list = []
    listpoly = []
    for code in lv4list:
        for i in range(4):
            lv5list.append(code+str(i+1))
    for code in lv5list:
        listpoly.append(create_polygon(code))
    code_list1 = pd.DataFrame(lv5list, columns = ['meshcode'])
    code_list2 = pd.DataFrame(listpoly, columns = ['geometry'])
    code_list = pd.concat([code_list1,code_list2], axis=1)
    code_list.to_csv("lv5meshwithcode.csv", index=None)
    print("lv5 done")
    return lv5list

def create_lv6():
    """
    create lv6 mesh code based on lv5 mesh code
    """
    lv5list = create_lv5()
    lv6list = []
    listpoly = []
    for code in lv5list:
        for i in range(4):
            lv6list.append(code+str(i+1))
    for code in lv6list:
        listpoly.append(create_polygon(code))
    code_list1 = pd.DataFrame(lv6list, columns = ['meshcode'])
    code_list2 = pd.DataFrame(listpoly, columns = ['geometry'])
    code_list = pd.concat([code_list1,code_list2], axis=1)
    code_list.to_csv("lv6meshwithcode.csv", index=None)
    return print("lv6 done")

create_mesh_code = create_lv6()
print("all level done")
