
seats = []


def rshift(val, n): return (val % 0x100000000) >> n


with open("input.txt", "r") as f:
    seats = f.readlines()

highest_seat_id = 0
seat_ids = []

for seat in seats:
    seat = seat.replace("F", "0").replace("B", "1").replace(
        "L", "0").replace("R", "1").strip()
    seat_num = int(seat, 2)
    row = rshift(seat_num, 3)
    col = seat_num & 0b00000000111

    # seat_id = row * 8 + col
    seat_ids.append(seat_num)
    if highest_seat_id < seat_num:
        highest_seat_id = seat_num


def findMissing(arr, n):

    l, h = 0, n - 1
    mid = 0

    while (h > l):

        mid = l + (h - l) // 2

        # Check if middle element is consistent
        if (arr[mid] - mid == arr[0]):

            # No inconsistency till middle elements
            # When missing element is just after
            # the middle element
            if (arr[mid + 1] - arr[mid] > 1):
                return arr[mid] + 1
            else:

                # Move right
                l = mid + 1

        else:

            # Inconsistency found
            # When missing element is just before
            # the middle element
            if (arr[mid] - arr[mid - 1] > 1):
                return arr[mid] - 1
            else:

                # Move left
                h = mid - 1

    # No missing element found
    return -1


sorted_seats = sorted(seat_ids)

print(findMissing(sorted_seats, len(sorted_seats)))
