def vowel_count(str):
	count = 0
	vowel = set("aeiou")
	
	
	for alphabet in str:
		if alphabet in vowel:
			count = count + 1
	
	print("No. of vowels :", count)
	
str = "Rose is a beautiful girl"

vowel_count(str)
