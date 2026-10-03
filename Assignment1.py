
# ADD, UPDATE, DELETE (lIST)
namelist = ["Ayush","Lokesh","Arjun","Shubham","Aditya"]
print(namelist)
#ADD
namelist.append("Aryan")
print(namelist)
namelist.insert(1,"Raju")
print(namelist)
#UPDATE
namelist[4] = "Saharsh"
print(namelist)
#DELETE
namelist.pop(3)
print(namelist)
namelist.remove("Lokesh")
print(namelist)
del namelist


# In[2]:


# ADD, UPDATE, DELETE (TUPLE)
tuple1 = ("Ayush","Lokesh","Arjun","Shubham","Aditya")
print(tuple1[2])
z = ("Jayesh",)
tuple1 += z
print(tuple1)
y = list(tuple1)
y.append("Aryan")
y.insert(1,"Raju")
y[0] = "Saharsh"
y.pop(3)
tuple1 = tuple(y)
print(tuple1)


# In[3]:


# ADD, UPDATE, DELETE (DICTIONARY)
dict1 = {"Ayush" : 1,
         "Lokesh" : 2,
         "Arjun" : 3,
         "Shubham" : 4}
print(dict1)
print(dict1["Shubham"])
dict1["Arjun"] = 5
print(dict1)
dict1.update({"Lokesh" : 6})
print(dict1)
print(dict1.get("Ayush"))
dict1["Saharsh"] = 9
print(dict1)
dict1.pop("Ayush")
print(dict1)
dict1.popitem()
print(dict1)

