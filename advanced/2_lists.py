# Slicing Lists in Python
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(fruits[2:5])  # Output: ['cherry', 'orange', 'kiwi']
print(fruits[:4])   # Output: ['apple', 'banana', 'cherry', 'orange']
print(fruits[3:])   # Output: ['orange', 'kiwi', 'melon', 'mango']
print(fruits[-4:-1]) # Output: ['orange', 'kiwi', 'melon']
print(fruits[::2])  # Output: ['apple', 'cherry', 'kiwi', 'mango']
print(fruits[::-1]) # Output: ['mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple']
print(fruits[-1::-1]) # Output: ['mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple']
print(fruits[1:5:2]) # Output: ['banana', 'orange']
print(fruits[-3::-1]) # Output: ['melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple']
print(fruits[-5:-2:2]) # Output: ['cherry', 'kiwi']
print(fruits[:])    # Output: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

'''
| Code | What it does | Resulting list | Why it works |
|------|--------------|----------------|--------------|
| `fruits[2:5]` | Start at index 2, stop before index 5 | `['cherry', 'orange', 'kiwi']` | Picks items 2, 3, 4. |
| `fruits[:4]` | Start at 0 (default), stop before 4 | `['apple', 'banana', 'cherry', 'orange']` | First four items. |
| `fruits[3:]` | Start at 3, go to the end | `['orange', 'kiwi', 'melon', 'mango']` | From index 3 onward. |
| `fruits[-4:-1]` | Start 4th from end (index 3), stop before last | `['orange', 'kiwi', 'melon']` | Equivalent to `fruits[3:6]`. |
| `fruits[::2]` | All items, every 2nd (step 2) | `['apple', 'cherry', 'kiwi', 'mango']` | Skips every other item. |
| `fruits[::-1]` | Reverse the whole list (step -1) | `['mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple']` | Step of –1 walks backward. |
| `fruits[-1::-1]` | Start at last element, step back | Same as above | `-1` is the last item; same reverse logic. |
| `fruits[1:5:2]` | From index 1 to 4, every 2nd | `['banana', 'orange']` | Picks indices 1 and 3. |
| `fruits[-3::-1]` | Start at 3rd from end (`-3` → index 4), go backward | `['melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple']` | Walks from index 4 down to 0. |
| `fruits[-5:-2:2]` | From 5th from end (`-5` → index 2) to before 2nd from end (`-2` → index 5), step 2 | `['cherry', 'kiwi']` | Picks indices 2 and 4. |
| `fruits[:]` | No limits – copy the entire list | `['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']` | Default start = 0, stop = len(list). |
'''