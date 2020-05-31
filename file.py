f = open("Sample.txt", 'w')
print(f.name)
print("closed or not", f.closed)
print("read", f.readable())
print("write", f.writable())
f.close()


print("closed or not", f.closed)
f = open("Sample.txt", 'r')
Read = f.readlines()
print(Read)
f.close()


'''file modes'''
# r,w, r+, w+, a, a+, x
