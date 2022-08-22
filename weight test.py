weight = float(input("Weight: "))
if weight == float:
    wtype = input("(K)G or (L)BS: ").upper()
    if wtype == "K":
        actual = weight*4.5
        print("Weight in LBs is: " + str(actual))
    elif wtype == "L":
        actual = weight/4.5
        print("Weight in KGs is: " + str(actual))
    else:
        print("Please enter a valid alphabet, (K) for kg and (L) for pound")
else:
    print("please input numbers only!")





