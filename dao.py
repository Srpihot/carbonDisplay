#coding=utf-8
from decimal import Decimal
from db import DBconnect
def judgeZero(x):
    if x is None:
        return 0
    else:
        return x

def getSum():
    resTemplate={"status":200,"code":0,"msg":"成功~","data":{}}
    res = resTemplate
    db = DBconnect()
    cursor = db.cursor()
    sql = "SELECT * FROM budgetsum"
    cursor.execute(sql)
    temp = cursor.fetchall()
    fdata = []
    ludata = []
    agdata = []
    osdata = []
    lsdata = []
    bidata = []
    for t in temp:
        fdata.append(Decimal(t[1]).quantize(Decimal("0.00")))
        ludata.append(Decimal(t[2]).quantize(Decimal("0.00")))
        agdata.append(Decimal(t[3]).quantize(Decimal("0.00")))
        osdata.append(Decimal(t[4]).quantize(Decimal("0.00")))
        lsdata.append(Decimal(t[5]).quantize(Decimal("0.00")))
        bidata.append(Decimal(t[6]).quantize(Decimal("0.00")))
    res["msg"] = "查询成功~"
    res["data"].update({"fname":"化石燃料排放","fdata":fdata})
    res["data"].update({"luname":"陆地变化排放","ludata":ludata})
    res["data"].update({"agname":"大气活动排放","agdata":agdata})
    res["data"].update({"osname":"海洋下沉排放","osdata":osdata})
    res["data"].update({"lsname":"陆地下沉排放","lsdata":lsdata})
    res["data"].update({"biname":"差值","bidata":bidata})
    
    sql = "SELECT * FROM `Historical Budget`"
    cursor.execute(sql)
    temp = cursor.fetchall()
    fdata = []
    ludata = []
    agdata = []
    osdata = []
    lsdata = []
    bidata = []
    for t in temp:
        fdata.append(Decimal(judgeZero(t[1])).quantize(Decimal("0.0000")))
        ludata.append(Decimal(judgeZero(t[2])).quantize(Decimal("0.0000")))
        agdata.append(Decimal(judgeZero(t[3])).quantize(Decimal("0.0000")))
        osdata.append(Decimal(judgeZero(t[4])).quantize(Decimal("0.0000")))
        lsdata.append(Decimal(judgeZero(t[5])).quantize(Decimal("0.0000")))
        bidata.append(Decimal(judgeZero(t[6])).quantize(Decimal("0.0000")))
    res["msg"] = "查询成功~"
    res["data"].update({"ftotal":fdata})
    res["data"].update({"lutotal":ludata})
    res["data"].update({"agtotal":agdata})
    res["data"].update({"ostotal":osdata})
    res["data"].update({"lstotal":lsdata})
    res["data"].update({"bitotal":bidata})
    totalyear = []
    for i in range(1750,2021):
        totalyear.append(str(i)+'年')
    res["data"].update({"yeartotal":totalyear})

    # sql = "SELECT SUM(Coal),SUM(Oil),SUM(Gas),SUM(CementEmission),SUM(Flaring),SUM(Other) FROM `Fossil Emissions by Category`"
    # cursor.execute(sql)
    # temp = cursor.fetchall()
    fossileYear = ['fossileEYear']
    Coal = ['Coal']
    Oil = ['Oil']
    Gas = ['Gas']
    Cement = ['Cement Emission']
    Flaring = ['Flaring']
    Other = ['Other']
    # for t in temp:
    #     fossileYear.append(9999)
    #     Coal.append(Decimal(judgeZero(t[0])).quantize(Decimal("0.00")))
    #     Oil.append(Decimal(judgeZero(t[1])).quantize(Decimal("0.00")))
    #     Gas.append(Decimal(judgeZero(t[2])).quantize(Decimal("0.00")))
    #     Cement.append(Decimal(judgeZero(t[3])).quantize(Decimal("0.00")))
    #     Flaring.append(Decimal(judgeZero(t[4])).quantize(Decimal("0.00")))
    #     Other.append(Decimal(judgeZero(t[5])).quantize(Decimal("0.00")))

    sql = "SELECT * FROM `Fossil Emissions by Category`"
    cursor.execute(sql)
    temp = cursor.fetchall()
    fdatasource = []
    for t in temp:
        fossileYear.append(str(t[0]))
        Coal.append(float(Decimal(judgeZero(t[1])).quantize(Decimal("0.00"))))
        Oil.append(float(Decimal(judgeZero(t[2])).quantize(Decimal("0.00"))))
        Gas.append(float(Decimal(judgeZero(t[3])).quantize(Decimal("0.00"))))
        Cement.append(float(Decimal(judgeZero(t[4])).quantize(Decimal("0.00"))))
        Flaring.append(float(Decimal(judgeZero(t[5])).quantize(Decimal("0.00"))))
        Other.append(float(Decimal(judgeZero(t[7])).quantize(Decimal("0.00"))))
    fdatasource.append(fossileYear)
    fdatasource.append(Coal)
    fdatasource.append(Oil)
    fdatasource.append(Gas)
    fdatasource.append(Cement)
    fdatasource.append(Flaring)
    fdatasource.append(Other)
    res["data"].update({"fdatasource":fdatasource})

    treedata={
        "name":"Global Carbon Budget",
        "children":[
            {
                "name":"Historical Budget",
                "children":[
                    {
                        "name":"Year",
                        "value":271
                    },
                    {
                        "name":"FossilEmissions",
                        "value":271
                    },
                    {
                        "name":"Land-useEmissions",
                        "value":271
                    },
                    {
                        "name":"Atmospheric Growth",
                        "value":271
                    },
                    {
                        "name":"OceanSink",
                        "value":271
                    },
                    {
                        "name":"CementCarbonationSink",
                        "value":271
                    },
                    {
                        "name":"Budgetlmbalance",
                        "value":271
                    },
                    {
                        "name":"StatisticsType",
                        "value":271
                    },
                ]
            },
            {
                "name":"Land-Use Change Emissions Models",
                "children":[
                    {
                        "name":"Year",
                        "value":62
                    },
                    {
                        "name":"CABLE-POP",
                        "value":62
                    },
                    {
                        "name":"CLASSIC",
                        "value":62
                    },
                    {
                        "name":"CLM5.0",
                        "value":62
                    },
                    {
                        "name":"DLEM",
                        "value":62
                    },
                    {
                        "name":"ISAM",
                        "value":62
                    },
                    {
                        "name":"IBIS",
                        "value":62
                    },
                    {
                        "name":"ISBA-CTRIP",
                        "value":62
                    },
                    {
                        "name":"JSBACH",
                        "value":62
                    },
                    {
                        "name":"JULES-ES",
                        "value":62
                    },
                    {
                        "name":"LPJ-GUESS",
                        "value":62
                    },
                    {
                        "name":"LPJ",
                        "value":62
                    },
                    {
                        "name":"LPX-Bern",
                        "value":62
                    },
                    {
                        "name":"OCNv2",
                        "value":62
                    },
                    {
                        "name":"ORCHIDEE-v3",
                        "value":62
                    },
                    {
                        "name":"SDGVM",
                        "value":62
                    },
                    {
                        "name":"VISIT",
                        "value":62
                    },
                    {
                        "name":"YIBs",
                        "value":62
                    },
                ]
            },
            {
                "name":"Terrestrial Sink Models",
                "children":[
                    {
                        "name":"Year",
                        "value":62
                    },
                    {
                        "name":"CABLE-POP",
                        "value":62
                    },
                    {
                        "name":"CLASSIC",
                        "value":62
                    },
                    {
                        "name":"CLM5.0",
                        "value":62
                    },
                    {
                        "name":"DLEM",
                        "value":62
                    },
                    {
                        "name":"ISAM",
                        "value":62
                    },
                    {
                        "name":"IBIS",
                        "value":62
                    },
                    {
                        "name":"ISBA-CTRIP",
                        "value":62
                    },
                    {
                        "name":"JSBACH",
                        "value":62
                    },
                    {
                        "name":"JULES-ES",
                        "value":62
                    },
                    {
                        "name":"LPJ-GUESS",
                        "value":62
                    },
                    {
                        "name":"LPJ",
                        "value":62
                    },
                    {
                        "name":"LPX-Bern",
                        "value":62
                    },
                    {
                        "name":"OCNv2",
                        "value":62
                    },
                    {
                        "name":"ORCHIDEE-v3",
                        "value":62
                    },
                    {
                        "name":"SDGVM",
                        "value":62
                    },
                    {
                        "name":"VISIT",
                        "value":62
                    },
                    {
                        "name":"YIBs",
                        "value":62
                    },
                ]
            },
            {
                "name":"Cement Carbonation Sink Models",
                "children":[
                    {
                        "name":"Year",
                        "value":62
                    },
                    {
                        "name":"Cao",
                        "value":62
                    },
                     {
                        "name":"Guo",
                        "value":62
                    }
                ]
            },
            {
                "name":"Fossil Emissions by Category",
                "children":[
                    {
                        "name":"Year",
                        "value":62
                    },
                    {
                        "name":"Coal",
                        "value":62
                    },
                    {
                        "name":"Oil",
                        "value":62
                    },
                    {
                        "name":"Gas",
                        "value":62
                    },
                    {
                        "name":"CementEmission",
                        "value":62
                    },
                    {
                        "name":"Flaring",
                        "value":62
                    },
                    {
                        "name":"Year",
                        "value":62
                    },
                    {
                        "name":"Per.Capita",
                        "value":62
                    },
                    {
                        "name":"Other",
                        "value":62
                    },
                ]
            },
            {
                "name":"Ocean Sink Models",
                "children":[
                    {
                        "name":"Year",
                        "value":62
                    },
                    {
                        "name":"CESM-ETH",
                        "value":62
                    },{
                        "name":"FESOM2-RECOM2",
                        "value":62
                    },{
                        "name":"NEMO-PISCES (CNRM)",
                        "value":62
                    },{
                        "name":"NEMO-PISCES (IPSL)",
                        "value":62
                    },{
                        "name":"NEMO-PlankTOM12",
                        "value":62
                    },{
                        "name":"NorESM-OC",
                        "value":62
                    },{
                        "name":"MOM6-COBALT (Princeton)",
                        "value":62
                    },{
                        "name":"MPIOM-HAMOCC",
                        "value":62
                    },
                ]
            },
        ]
    }
    res["data"].update({"treedata":treedata})

    sql = "SELECT * from `fossilemissionsmax`"
    cursor.execute(sql)
    temp = cursor.fetchall()
    fmaxyear = []
    fmaxdata = []
    for t in temp:
        fmaxyear.append(str(t[1]))
        fmaxdata.append(float(Decimal(judgeZero(t[2])).quantize(Decimal("0.00"))))
    res["data"].update({"fmaxyear":fmaxyear,"fmaxdata":fmaxdata})

    sql = "SELECT * from `land-useemissionsmax`"
    cursor.execute(sql)
    temp = cursor.fetchall()
    lumaxyear = []
    lumaxdata = []
    for t in temp:
        lumaxyear.append(str(t[1]))
        lumaxdata.append(float(Decimal(judgeZero(t[2])).quantize(Decimal("0.00"))))
    res["data"].update({"lumaxyear":lumaxyear,"lumaxdata":lumaxdata})

    sql = "SELECT * from `atmospheric growthmax`"
    cursor.execute(sql)
    temp = cursor.fetchall()
    agmaxyear = []
    agmaxdata = []
    for t in temp:
        agmaxyear.append(str(t[1]))
        agmaxdata.append(float(Decimal(judgeZero(t[2])).quantize(Decimal("0.00"))))
    res["data"].update({"agmaxyear":agmaxyear,"agmaxdata":agmaxdata})

    sql = "SELECT * from `oceansinkmax`"
    cursor.execute(sql)
    temp = cursor.fetchall()
    osmaxyear = []
    osmaxdata = []
    for t in temp:
        osmaxyear.append(str(t[1]))
        osmaxdata.append(float(Decimal(judgeZero(t[2])).quantize(Decimal("0.00"))))
    res["data"].update({"osmaxyear":osmaxyear,"osmaxdata":osmaxdata})

    sql = "SELECT * from `landsinkmax`"
    cursor.execute(sql)
    temp = cursor.fetchall()
    lsmaxyear = []
    lsmaxdata = []
    for t in temp:
        lsmaxyear.append(str(t[1]))
        lsmaxdata.append(float(Decimal(judgeZero(t[2])).quantize(Decimal("0.00"))))
    res["data"].update({"lsmaxyear":lsmaxyear,"lsmaxdata":lsmaxdata})

    sql = "SELECT * from `cementcarbonationsinkmax`"
    cursor.execute(sql)
    temp = cursor.fetchall()
    csmaxyear = []
    csmaxdata = []
    for t in temp:
        csmaxyear.append(str(t[1]))
        csmaxdata.append(float(Decimal(judgeZero(t[2])).quantize(Decimal("0.00"))))
    res["data"].update({"csmaxyear":csmaxyear,"csmaxdata":csmaxdata})
    cursor.close()
    return res

# print(getSum())