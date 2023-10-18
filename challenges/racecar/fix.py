import re

raw_flag = input("Enter the raw data: ")

print(raw_flag)

raw_flag = raw_flag.split()[::-1] # split the string of hex by spaces, then reverse the list

print(raw_flag)


for i in range(len(raw_flag)):
	raw_flag[i] = re.findall('..', raw_flag[i]) # for each element in the list, split every byte and save the list of bytes at the index

print(raw_flag)

flag = []
for chars in raw_flag:
	word = ""
	for char in chars[::-1]: # reverse the byte array, so the least signifficate byte goes first
		if char != '0x':
			#word += chr(int(char, 16))
			word += char
	flag.append(word)

#flag.reverse() # reverse the flag
print(''.join(flag))
