def asc2(): 
	for i in range(256):
		c = chr(i)
		print("[",i,"=",c,"]",end="")
		if (i % 10 == 0):
				print("\n",end="")
				

def main():
	asc2()

main()
