class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1=(ax2-ax1)*(ay2-ay1)
        area2=(bx2-bx1)*(by2-by1)
        if bx2<ax1 or bx1>ax2 or by1>ay2 or by2<ay1:
            return area1+area2
        return (area1+area2)-(min(ax2,bx2)-max(ax1,bx1))*(min(by2,ay2)-max(by1,ay1))
