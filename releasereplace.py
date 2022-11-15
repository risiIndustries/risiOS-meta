import sys

amount = int(sys.argv[2])
new_file = []

with open(sys.argv[1], "r") as f:
	for line in f.readlines():
		new_int = ""
		old_int = ""
		if line.startswith("Release:"):
			release = line
			for i in release:
				if i.isnumeric():
					old_int += i
			new_int = str(int(old_int) + amount)
			release = release.replace(old_int, new_int)
			new_file.append(release)
		else:
			new_file.append(line)
with open(sys.argv[1], "w") as f:
	for line in new_file:
		f.write(line)
