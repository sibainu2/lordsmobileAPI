import json
mapo=open(r"C:\Users\waon-pc\Desktop\discord\lordsmobileAPI\dete\map.json")
mapl=json.load(mapo)
maps=json.dumps(mapl)
mapdata=json.loads(maps)
print(mapdata["x0y0"])
mapo.close()