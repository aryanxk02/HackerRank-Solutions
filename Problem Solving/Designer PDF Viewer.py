def designerPDFviewer(heights, string):
    heights_of_string = [heights[ord(i)-ord('a')] for i in string]
    base = len(string)
    max_height_of_rectangle = max(heights_of_string)
    print(base * max_height_of_rectangle)

heights = list(map(int, input().split()))
string = list(input())

designerPDFviewer(heights, string)


