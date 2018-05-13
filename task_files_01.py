with open('data.txt') as f:
    read_data = f.read().split()

def save(name, data):
    with open(name+'.txt', 'w') as f:
        f.write(data)

def out_1(n, read_data):
    list = []
    for v in read_data:
        if int(v) % n == 0:
            list.append(v)
    list = " ".join(list)
    save("out-1", list)
    
    
def out_2(p, read_data):
    list = []
    for v in read_data:
        list.append(str(int(v) ** p))
    list = " ".join(list)
    save("out-2", list)
    
    
out_1(int(input()), read_data)
out_2(int(input()), read_data)