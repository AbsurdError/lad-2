#//////////2задачa/////////
#
# def del_rep(num):
#цикл раставляет числа в порядке возрастания
#     i = 0
#     while i < len(num):
#         x = 0
#         while x < len(num) - (i + 1):
#             if num[x] > num[x + 1]:
#                 num[x], num[x + 1] = num[x + 1], num[x]
#             x += 1
#         i += 1
#удаляет повторы
#     temp = []
#     for m in num:
#         if m not in temp:
#             temp.append(m)
#             num = temp
#     return temp
# print(del_rep([int(y) for y in input('Введите числа:  ').split()]))

#//////////3задачa/////////

# def lim_max(nums):
#     limit = int(input('Введите лимит:  '))
#цикл раставляет числа в порядке возрастания
#     i = 0
#     while i < len(nums):
#         x = 0
#         while x < len(nums) - (i + 1):
#             if nums[x] > nums[x + 1]:
#                 nums[x], nums[x + 1] = nums[x + 1], nums[x]
#             x += 1
#         i += 1
#нахожу максимальное число после лимита
#     n = 0
#     for i in range(0, len(nums)):
#         if nums[i] < limit:
#             n = nums[i]
#     return n
# print(lim_max([int(y) for y in input('Введите числа:  ').split()]))


#////////4задача///////

# def temp_cat(temp):
#
#     if temp < -20:
#         return 0 #Холодно
#     elif -20 <= temp < 0:
#         return 1 # Прохладно
#     elif 0 <= temp < 15:
#         return 2 #Зябко
#     elif 15 <= temp < 25:
#         return 3 #Тепло
#     else:
#         return 4 #Жарко
# print(temp_cat(int(input('Введите температуру:  '))))

#////////5задача///////
