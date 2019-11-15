def bubble_sort(entry):

    shuffled_items = 0

    for cnt, val in enumerate(entry):

        if cnt > 0 and entry[cnt] < entry[cnt-1]:

                # Swap values
                entry[cnt], entry[cnt-1] = entry[cnt-1], entry[cnt]
                shuffled_items += 1

    if shuffled_items > 0:

        bubble_sort(entry)

    return entry


entry = [2, 1, 4, 3, 5]
target = bubble_sort(entry)
print(target)
