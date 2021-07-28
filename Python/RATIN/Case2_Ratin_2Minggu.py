nums = [2, 7, 8]
target = 10


def caracariindex(nums, target):
    for i in nums:
        print(i, "fase1")
        a = nums.index(i)
        coba = target-i
        print(coba, "hasil kurang 1")
        for j in nums:
            b = nums.index(j)
            print(j, "fase2")
            if a != b:
                coba = coba-j
                print(coba, "hasil kurang 2")
                if coba == 0:
                    listurut = [a, b]
                    listurut.sort()

                    return(listurut)
                    pass
    return(0, 0)


caracariindex(nums, target)
print(caracariindex(nums, target))
