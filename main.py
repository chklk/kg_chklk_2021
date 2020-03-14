import os
import sys

def onetoone(s1, s2): 
	if len(s1)!=len(s2): 
		return False
	word_dictionary={}
	for i in range(len(s1)): 
		if s1[i] in word_dictionary: 
			if word_dictionary[s1[i]]!=s2[i]: 
				return False 
		else: 
			word_dictionary[s1[i]]=s2[i]
	return True

if __name__ == '__main__':
	s1=str(sys.argv[1])
	s2=str(sys.argv[2])
	print(onetoone(s1, s2))