# # Replace (overwrite) the file
# with open("myfile.txt", "w") as f:
# 	f.write("Poonam\n")

# # Add/append to the file
# with open("myfile.txt", "a") as f:
# 	f.write("Yatin\n")

# Write with user input and newline
# text = input("Please Enter anyhing to add: ")
# with open("myfile.txt", "a") as f:
# 	f.write(text + "\n")
	
# f= open("myfile.txt", "r")
# data=f.read()
# print(data)
# f.close()


from pathlib import Path

# Open myfile.txt located next to this script, regardless of cwd
data_file = Path(__file__).parent / 'myfile.txt'
with data_file.open('r', encoding='utf-8-sig') as f:
    lines = f.readlines()

print(lines, type(lines))
print(''.join(lines))