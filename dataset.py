import json

normal = {"tiles":None}#,"Lvel":None,"name":None,"guild":None,"kills":None,"power":None
Nest = {"tiles":"Nest","Lvel":None,"power":None}
player ={"tiles":"player","Lvel":None,"name":None,"guild":None,"kills":None,"power":None}

Coordinates={"x0y0":"value1",}
for y in range(1024):#1024
    for x in range(512):#

        Coordinates["x{}y{}".format(x,y)]=normal


a =json.dumps(Coordinates)#,indent=4

with open(r"C:\Users\waon-pc\Desktop\discord\lordsmobileAPI\dete\map.json","w") as f:
    f.write(a)

#class data:
#    def __init__(self,position,tile,name,guild,power) -> None:
#        self.position=position
#        self.tile=tile
#        self.name=name
#        self.guild=guild
#        self.power=power
    
