'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

'''


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dic = {}
for i in handle:
    if i.startswith("From") and len(i.split()) > 2:
        line = i.split()
        line2 = line[5][:2].split(":")
		
        for k,v in dic.items():
			if line2[0] == k:
				dic[line[0]] = 1
			else:
				dic[line[0]] += 1

for k in sorted(dic.items()):
    print(k)
