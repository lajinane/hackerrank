'''
https://www.hackerrank.com/challenges/py-the-captains-room/problem
'''

from collections import Counter

K = int(input())
entries = list(map(int, input().split()))
rooms = set(entries)  # unique values

# num_of_families = (len(entries) - 1) // K

# method 1 - Counter()
counter = Counter(entries)
print(counter.most_common()[-1][0])

# method 2 - sum()
total_entries = sum(entries)
total_rooms = sum(rooms) * K
captain_room = (total_rooms - total_entries) // (K-1)
print(captain_room)
