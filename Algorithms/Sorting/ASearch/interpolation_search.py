# interpolation_search.py

class InterpolationSearch:
    def __init__(self, data):
        self.data = sorted(data)  # Ensure data is sorted

    def search(self, target):
        low = 0
        high = len(self.data) - 1
        
        while low <= high and self.data[low] <= target <= self.data[high]:
            if low == high:
                if self.data[low] == target:
                    return low
                return -1
            
            # Estimate the position of the target value
            pos = low + ((target - self.data[low]) * (high - low) // (self.data[high] - self.data[low]))
            
            if self.data[pos] == target:
                return pos
            if self.data[pos] < target:
                low = pos + 1
            else:
                high = pos - 1
                
        return -1
