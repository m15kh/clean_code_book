print('code1')
a = [1, 2, 3, 4]
if (len(a)) > 3:
	print(f"List is too long ({len(a)} elements, expected <= 3)")
print('--------------------------------')
print('code2')
a = [1, 2, 3, 4]
if (n := len(a)) > 3:
	print(f"List is too long ({n} elements, expected <= 3)")
print('--------------------------------')
print('code3')
a = [1, 2, 3, 4]
n = len(a)
if n > 3:
	print(f"List is too long ({n} elements, expected <= 3)")

