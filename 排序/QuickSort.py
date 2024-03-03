class QuickSort:
    def quick_sort(self, arr):
        if len(arr) <= 1:  # 修正了条件检查
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        # 修正了方法调用的语法
        return self.quick_sort(left) + middle + self.quick_sort(right)

# 创建 QuickSort 类的一个实例
qs = QuickSort()
arrlist = [1,3,4,5,0,10,39,49,20]

# 使用这个实例来调用 quick_sort 方法
sorted_list = qs.quick_sort(arrlist)
print(sorted_list)
