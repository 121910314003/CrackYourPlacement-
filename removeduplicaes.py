 def removeDuplicates(self, nums: List[int]) -> int:
        prev=None
        ln=len(nums)
        i=0
        while i<ln:
            if(nums[i]==prev):
                prev=nums[i]
                nums.remove(prev)
                ln=len(nums)
                i=i-1
            else:
                prev=nums[i]
            i+=1
        print(len(nums))
