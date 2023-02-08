dy = {}
print(type(dy))
dy1 = {"riya" : 21, "pramodh" :56 }
print(dy1)
print(dy1["riya"]) #case sensitive
dy2 = {"riya": "bread", "pramodh":"rice", "preethi":{"weekdays":"fruits", "holidays":"rice"}} #preethi is an example for a dictionary within a dictionary
print(dy2["pramodh"])
print(dy2["preethi"])
print(dy2["preethi"]["weekdays"])
dy2["anu"] = "chicken"
dy2["ajay"] = "fish"
print(dy2)

del dy2["riya"] #del function removes
print(dy2)

#dy3 = dy2 doesnt form a anew disctionary dy3 but is a pointer so dy3 not a copy of dy2
#del dy3["riya"] will delete directly from dy2 when smtg deleted from dy3

dy3 = dy2.copy()#copy function
del dy3["preethi"] #doesnt delete the elemet from the dy2 original as only a copy has benn made in dy3 not the original
print(dy2)
print(dy3)
print(dy3.get("ajay"))

dy3.update({"latha":"egg"})
print(dy3)
print(dy3.keys()) #lhs of the key value pair
print(dy3.items())#prints all the key value pairs in a dictionary
