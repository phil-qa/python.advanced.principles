#!/usr/local/bin/python3
# Python 3
class Country:

    index = {'cname':0,'population':1,'capital':2,'citypop':3,'continent':4,
             'ind_date':5,'currency':6,'religion':7,'language':8}
    
    def __init__(self, row):
        self.__attr = row.split(',')
        
        # Added to support + and -
        self.__attr[Country.index['population']] = \
            int(self.__attr[Country.index['population']])

    def __str__(self):
        return "{:<10} {:<10} {:>010}".format(self.cname, self.capital, self.population)
        
    def __add__(self,amount):
        self.__attr[Country.index['population']] += amount
        return self
        
    def __sub__(self,amount):
        self.__attr[Country.index['population']] -= amount
        return self
        
    def __eq__(self, key):
        return (key == self.cname)

    # TODO: implement an attribute get function
    def __getattr__(self, attr):
        if attr in Country.index:
            return self.__attr[Country.index[attr]]
        else:
            raise(AttributeError)
 
    # TODO: implement an attribute delete function
    def __delattr__(self, attr):
        if attr in Country.index:
            if isinstance(self.__attr[Country.index[attr]], int):
                self.__attr[Country.index[attr]] = 0
            else:
                self.__attr[Country.index[attr]] = ""
        else:
            raise(AttributeError)    

    # JSON exercise
    def convert_to_std_type(self, obj):
    
         retn = {}
         for k, v in Country.index.items():
             retn[k] = obj.__attr[v]
         print(retn)
         return retn
 

def dict_to_country(inp):
    rlist = list(range(0, 9))
    print(inp)
    print(rlist)
    for k, v in inp.items():
        field_pos = Country.index[k]
        rlist[int(field_pos)] = str(v)
    
    return Country(','.join(rlist))

######################################################################################
if __name__ == "__main__":
    
    
    belgium = Country("Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German")
    japan   = Country("Japan,127920000,Tokyo,31139900,Orient,-660,Yen,Shinto;Buddhism,Japanese")
    myanmar = Country("Myanmar,42909464,Yangon,4344100,Asia,1948,Kyat,Buddhism,Burmese")
    sweden  = Country("Sweden,9001774,Stockholm,1622300,Europe,1523,Swedish Krona,Lutheran,Swedish")
   
    import json

    fo = open('belgium.json', 'w')
    json.dump(belgium, fo, default=belgium.convert_to_std_type)
    fo.close()
    
    fi = open('belgium.json', 'r')
    obj = json.load(fi, object_hook=dict_to_country)
    print(obj)