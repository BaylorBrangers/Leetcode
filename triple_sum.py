##Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
class Solution:
    def searchTriplets(self, arr):
        arr.sort()  # Sort the array to handle duplicates and to make skipping duplicates easier
        triplets = []
        for i in range(len(arr) -2):
          current = arr[i]
          start, stop = i +1, len(arr) -1
          while start < stop:
            _sum_pair = -1 * (arr[start] + arr[stop])
            if current == _sum_pair:
              if [current, arr[start], arr[stop]] not in triplets:
                triplets.append([current, arr[start], arr[stop]])
            if current < _sum_pair:
              start += 1
            elif current > _sum_pair:
              stop -= 1
            else:
              start += 1
              stop -= 1

        return triplets
