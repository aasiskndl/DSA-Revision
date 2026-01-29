'''
Docstring for core_dsa.binary_search_on_answer.capacity_to_ship_packages
You are given weights of packages on a conveyor belt
You must ship them in order within D days

Each day you load packages until the ship reaches its weight capacity.
Return the minimum ship capacity needed.

We are searching for the minimum capacity such that we can ship all packages in <= D days
'''

def ship_within_days(weights, D):
    def can_ship(capacity):
        days = 1
        current_load = 0 
        
        for w in weights:
            if current_load + w > capacity:
                days += 1 
                current_load = 0 
            current_load += w
        return days <= D
    left = max(weights)
    right = sum(weights)
    answer = right
    
    while left <= right:
        mid = (left + right) //2
        
        if can_ship(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

weights = [1,2,3,4,5,6,7,8,9,10]
D = 2
print("Minimum ship capacity:", ship_within_days(weights, D))

