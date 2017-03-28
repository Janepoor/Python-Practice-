##bst

def BST(nums, target):

    low = 0
    high = len(nums)-1

    while(low<=high):
        mid=(low+high)//2

        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            low=mid+1
        else:
            high=mid-1
    return False



a= BST([1,2,3,4,5,23,213,3],23)
print (a)