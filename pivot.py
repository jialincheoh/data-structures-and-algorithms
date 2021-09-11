def pivot(my_list, pivot_index, end_index):
	swap_index = pivot_index
	for i in range(pivot_index + 1, end_index + 1):
		if my_list[i] < my_list[pivot_index]
			swap_index += 1
			swap(my_list, swap_index, i)
	swap(my_list, pivot_index, swap_index)
	return swap_index

