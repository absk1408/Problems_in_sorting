#https://www.geeksforgeeks.org/sort-elements-by-frequency/
di={}
def i_s(arr):
    for x in range(1,len(arr)):
        for y in range(x,0,-1):
            if arr[y]<arr[y-1]:
                arr[y],arr[y-1]=arr[y-1],arr[y]
    return arr[::-1]



def dict_create(arr):
    for x in arr:
        if x not in di:
            di[x]=1
        else:
            di[x]+=1


def get_key(val):
	for key, value in di.items():
		if val == value:
			return key
def fin(arr):
    arr=dict_create(arr)
    arr1=[]
    arr2=[]
    for x in di.values():
        arr1.append(x)
    arr1=i_s(arr1)
    for x in arr1:
        c=get_key(x)
        for y in range(x):
            arr2.append(c)
        di.pop(c)
    return arr2

print(fin([2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]))
