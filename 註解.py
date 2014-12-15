import random#取用random.randint()函式


def get_int(msg, minimum, default):
    while True:
        try:
            #判斷rows,columns,minimum的值
			line = input(msg)
            #若使用者未輸入minimum,則值為default
			if not line and default is not None:
                return default
            i = int(line)
            #rows,columns的最小值需>=minimum,minimum的最小值需>=minimum的minimum
			if i < minimum:
                print("must be >=", minimum)
            else:
                return i
        except ValueError as err:
            print(err)


rows = get_int("rows: ", 1, None)
columns = get_int("columns: ", 1, None)
minimum = get_int("minimum (or Enter for 0): ", -1000000, 0)

#minimum如果>=default,則maximum=minimum*2
default = 1000
if default < minimum:
    default = 2 * minimum
maximum = get_int("maximum (or Enter for " + str(default) + "): ",
                  minimum, default)

row = 0
# 讓rows在輸出時不會超出使用者輸入的值
while row < rows:
    line = ""
    column = 0
    # 讓columns在輸出時不會超出使用者輸入的值
	while column < columns:
        #i=minimum~maximum間的隨機值
		i = random.randint(minimum, maximum)
        s = str(i)
        #在每個被輸出的值用空格補滿十個字元
		while len(s) < 10:
            s = " " + s
        line += s
        column += 1
    print(line)
    row += 1