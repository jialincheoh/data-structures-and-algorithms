def merge_sort(my_list): 
	if len(my_list) == 1:
		return my_list
	mid = int(len(my_list)/2)
	left = my_list[:mid]
	right = my_list[mid:]
	return merge(merge_sort(left), merge_sort(right))

print(merge_sort([3, 1, 4, 2]))


