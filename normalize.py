import sys 
import re 
def normalize(path): 
	if (re.search('/./', path )):
		normalizedPath="" 
		sub_path_length=len(path.split("/./"))
		for index, val in enumerate(path.split("/./")):
			if ((index+1)!=sub_path_length):
				normalizedPath+=val+"/"
			else:
				normalizedPath+=val	
		print 	normalizedPath


	elif (re.search('/../', path )):
		normalizedPath="" 
		for i in path.split("/../"):
			if (re.search('/', i)):
				print "iii", i
				try:
					sub_path_length=len(i.split("/"))
					for index, val in enumerate(i.split("/")):
						if (index+1==sub_path_length):
							pass
						else:	
							normalizedPath+=val+"/"
				except:
					pass

			else:
				normalizedPath+=i

		print 	"normalizedPath",normalizedPath	
if __name__=="__main__":
	if ( len(sys.argv)==2):
		path=sys.argv[1]
		normalize(path)
	else:
		print "Please pass in a string argument"
					
