import sys

if len(sys.argv)==1:
    print "Please provide the filename as the first argument.\nUsage: python ipsort.py [filename]"
    exit()

f = open(sys.argv[1], 'r')
iplist = []
for line in f:
    iplist.append(''.join(line.split()))

# Takes list of numbers and returns it sorted via bubble sorting algo
def bubble_sort(nums):
    swaps = 0;
    for i in range(len(nums)-1):
        if int(nums[i]) > int(nums[i+1]):
            nums[i],nums[i+1] = nums[i+1],nums[i]
            swaps = swaps+1
    if swaps == 0:
        return nums
    else:
        return bubble_sort(nums)
       
# Takes a list of IP addresses, and sorts them by index, or nth dot-seperated byte
def sort_by_order(array, index):
    uniqueIndexes = []
    unsortedArrs = []
    for item in array:
        sortIndex = item.split('.')[index]
        if not sortIndex in uniqueIndexes:
            uniqueIndexes.append(sortIndex)
            newArr = []
            newArr.append(item)
            unsortedArrs.append(newArr)
        elif sortIndex in uniqueIndexes:
            target = uniqueIndexes.index(sortIndex)
            unsortedArrs[target].append(item)

    bubble_sorted = bubble_sort(list(uniqueIndexes))
    sortedArrs = [None] * len(uniqueIndexes)
    for i in range(len(unsortedArrs)):
        sortedArrs[bubble_sorted.index(uniqueIndexes[i])] = unsortedArrs[i]

    return sortedArrs

# Takes a list of lists, runs them through sort_by_order, and returns as a single list of lists, not a list of multiple-nested lists
def next_sort(array, index):
    newList = []
    for item in array:
        neo = sort_by_order(item,index)
        for i in neo:
            newList.append(i)
    return newList

prelimsort = sort_by_order(iplist, 0)
secsort = next_sort(prelimsort,1)
trisort = next_sort(secsort,2)
lastsort = next_sort(trisort,3)

# Combine all lists into one list
finalArr = []
for item in lastsort:
    finalArr = finalArr + item

# print to STDOUT
for IP in finalArr:
    print IP
