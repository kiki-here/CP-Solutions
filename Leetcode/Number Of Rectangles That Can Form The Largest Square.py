 class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int: 
        a=[] #to store valid square sizes
        for i in rectangles:
            a.append(min(i[0],i[1])) #minimum among rectangle's length and width that will be 
            #the atmost size of square that can be formed from that particular rectangle
            
        m=max(a) #maxlen as asked in question
        return a.count(m) #total maxlen present in a
