running_hour = input("Please input running hour")
running_hour = int(running_hour)
if running_hour < 3000:
	print("no need any action")
elif running_hour >= 3000 and running_hour < 6000:
    print("please check equipment condition weekly")
elif running_hour >= 6000 and running_hour < 8000:
    print("please prepare for overhaul")
else:
	print("please carry out overhaul")