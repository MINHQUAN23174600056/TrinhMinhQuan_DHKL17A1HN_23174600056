 #BT 8
nums = [2,6,7,9]
def has_lucky_number(nums):
    for i in nums:
        if i % 7 == 0:
            return True
print(has_lucky_number(nums))