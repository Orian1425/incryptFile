import pickle

def encode_data(file_path):
    with open(file_path,"r") as file:
        data = file.read()
    inc_data = ""
    # for i in data:
    #     inc_data+= str(i^5)+" "
    # print(inc_data)
    # inc_data=""
    for i in data:
        inc_data += chr(ord(i)^ 5)
    with open(file_path,"w") as file:
        file.write(inc_data)



def decode_data(file_path):
    with open(file_path,"r") as file:
       inc_data = file.read()
    
    data=""
    for i in inc_data:
        data += chr(ord(i)^5)
    with open(file_path,"w") as file:
        file.write(data)
    
   

while True:
    choice = input("encrypt(e) | decrypt(d)  | quit(q)")
    if choice=='q':
        break
    elif choice == 'e':
        file_path = input("enter file path ")
        encode_data(file_path)
    elif choice == 'd':
        file_path = input("enter file path ")
        decode_data(file_path)
