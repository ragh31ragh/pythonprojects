
nums = [10, 9, 2, 5, 3, 7, 101, 18]
temp_list = []
sub_sequence_count = 0;
for i in range(len(nums)+1):
    print(nums[i])
    #if ()
    if (nums[i] < nums[i + 1]):
        sub_sequence_count = sub_sequence_count + 1;
        print(sub_sequence_count)

print(sub_sequence_count)



