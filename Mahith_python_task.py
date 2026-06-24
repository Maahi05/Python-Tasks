a = [{"employee_id":101,"name":"Maahi","age":22,"department":"CSE"}]
print("current dictionary:",a)
a.append({"employee_id":102,"name":"Rohith","age":22,"department":"CSE"})
print("All Employee details:",a)
a[0]= {"employee_id":101,"name":"Mahith","age":23,"department":"ECE"}
print("After Update:",a)
a.pop()
print("After deleting a employee:",a)
