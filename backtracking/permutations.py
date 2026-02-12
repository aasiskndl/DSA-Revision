"""
Docstring for dsa.backtracking.permutations
Backtracking for permutation is a systemaic, recursive algorithm that generates all possible ordering of a set of element by building candidates incrementally.
It explores potential sequences, and upon reaching a full permutaion or invalid state,
it undoes the last choicee (backtracks) to try alternative options, creating a tree of possibilities.

goal is to generate all possible ordered arrangements (permutation) of a given set of distinct elements.

"""


def permute(nums):
    result = []
    path = []
    used = [False] * len(nums)

    def backtrack():
        # if permutation is complete
        if len(path) == len(nums):
            result.append(path.copy())
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            # choose
            used[i] = True
            path.append(nums[i])

            # explore
            backtrack()

            # un-choose backtrack
            path.pop()
            used[i] = False

    backtrack()
    return result


nums = [4, 5, 6]
ans = permute(nums)

print("Permutations:")
for p in ans:
    print(p)
