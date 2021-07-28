# STUKAS 1

print("hafizh")
# nums = [1,3,4,2,2]
nums = [3, 1, 3, 4, 2]
nums2 = []
Hitungan_sama = 0
for i in nums:
    nums2.append(i)
nums2.pop(0)
print(nums2)
print(nums)

a = len(nums)-1
for x in range(a):
    for y in nums2:

        if nums[x] == y:
            Hitungan_sama = Hitungan_sama+1
            print("angka sama ke", Hitungan_sama, "pada angka", y)
    nums2.pop(0)


# #  cara 2
# nums = [1,3,4,2,2]

# def findDuplicate(nums):

#   for y in range  (len(nums)+1) :
#     if x == nums[y]:
#         print(x, nums[y])

# findDuplicate(nums)


# STUKAS 2
kondisi_awal = 1
kondisi_kedua = 2
komb = []
n = 6

if 1 == n:
    kondisi_akhir = kondisi_awal
elif 2 == n:
    kondisi_akhir = kondisi_kedua
elif n > 2:
    for i in range(n-2):
        kondisi_akhir = kondisi_awal + kondisi_kedua

        kondisi_awal = kondisi_kedua
        kondisi_kedua = kondisi_akhir
print(str(n), kondisi_akhir)
