# initializing list
test_list = [[5,3,2], [8,6,3], [3,5,3],
             [3,6], [3,7,4], [2,9]]

# printing original list
print("The original list is "+ str(test_list))

#initializing k
k = 3

res = []

for idx, ele in enumerate(test_list):
    
    # checking for k multiple
    if (idx+1) % k == 0:
        
        # reversing using reversed
        res.append(list(reversed(ele)))
    
    else:
        res.append(ele)

# printing result
print("After reversing every kth row : " + str(res))
