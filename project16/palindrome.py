
words = ["level", "civic", "Python", "refer", "Java", "madam"]
print("list of strings:")
print(words) 
palindrome = list(filter(lambda x: (x == "".join(reversed(x))), words)) 
print("\n palindrome words:")
print(palindrome) 
