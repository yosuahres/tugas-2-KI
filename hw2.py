key = "1110"

s0 = [[1, 0, 3, 2],
	[3, 2, 1, 0],
	[0, 2, 1, 3],
	[3, 1, 3, 2]]

def getSboxEntry(binary,sbox):
		row = binary[0] + binary[3]
		col = binary[1] + binary[2]
		row = int(row,2)
		col = int(col,2)
		binary = bin(s0[row][col])[2:]
		if len(binary) == 1:
			binary = "0" + binary
		return binary
		
def fFunction(key, k):
		XOR = bin((int(key,2)^int(k,2)))[2:]
		XOR = padding(XOR,4)
		S0 = getSboxEntry(XOR, s0)
		return S0

def padding(string,length):
	if len(string) == length:
		return string
	while(len(string) < length):
		string = "0" + string
	return string

values = []
for i in range(0,16):
	temp = i ^ 7
	values.append((i,temp))
print(values)

results = []
for (a,b) in values:
	binary = padding(bin(a)[2:],4)
	binary2 = padding(bin(b)[2:],4)
	output1 = int(getSboxEntry(binary, s0),2)
	output2 = int(getSboxEntry(binary2, s0),2)
	result = output1 ^ output2
	results.append(result)
print(results) 


output1 = fFunction(key, padding(bin(8)[2:],4))
output2 = fFunction(key, padding(bin(15)[2:],4))
int1 = int(output1,2)
int2 = int(output2,2)
XOR = int1^int2

keys =set()
As =  [0,1,2,3,4,5,6,7,10,13]
for val in As:
	XOR = val ^ 8
	keys.add(XOR)
print(keys)
#possible keys = [8, 9, 10, 11, 12, 13, 14, 15, 2, 5]

output1 = fFunction(key, padding(bin(6)[2:],4))
output2 = fFunction(key, padding(bin(1)[2:],4))
print(output1)
print(output2)
int1 = int(output1,2)
int2 = int(output2,2)
XOR = int1^int2
print(XOR)

keys2 = set()
Bs =  [0,1,2,3,4,5,6,7,10,13]
for val in Bs:
	XOR = val ^ 6
	keys2.add(XOR)
print(keys2)

intersection = keys.intersection(keys2)
print(intersection)
