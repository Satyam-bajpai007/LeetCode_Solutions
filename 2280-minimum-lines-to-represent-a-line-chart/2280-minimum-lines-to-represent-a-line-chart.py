class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        #find lenght of the aray
        #sort the array on the basis of set
        if len(stockPrices) == 1 :
            return 0
        elif len(stockPrices) == 2:
            return 1
        else:
            number = 1
            stockPrices.sort()
            print(stockPrices)
            for i in range(2, len(stockPrices)):
                if int((stockPrices[i][1]-stockPrices[i-1][1])*(stockPrices[i-1][0]-stockPrices[i-2][0])) !=\
                   int((stockPrices[i-1][1]-stockPrices[i-2][1])*(stockPrices[i][0]-stockPrices[i-1][0])):
                    number = number + 1

            return number