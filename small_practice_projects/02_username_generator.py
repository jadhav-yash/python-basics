print("============================================")
print("             USERNAME GENERATOR             ")
print("============================================")

name = input("Enter you name: ")

username = name.lower().strip().replace(" ","_")
final_username = name.find(" ")

if final_username == -1 :
    print("Please give proper spacing in your name !!!")
else : 
    print("Generated username:", username)