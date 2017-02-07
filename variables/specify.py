def asort(answer, data):  # DROP DOWN LIST IN INTERFACE VER
    if 'most' in answer.lower():  # Shows wifi spots by most -> least
        data.sort(reverse=True, key=lambda x: x[1])

    elif 'least' in answer.lower():  # Shows wifi spots by least -> most
        data.sort(key=lambda x: x[1])

    elif 'alpha' in answer.lower():  # Shows wifi spots in alphameric order - Default
        data.sort(key=lambda x: x[0])

    elif 'best' in answer.lower() or 'wifi' in answer.lower():  # Shows wifi spots with smallest person/connection ratio
        data.sort(key=lambda x: x[2])

    elif 'relative' in answer.lower():  # Shows buildings with highest words in common
        data.sort(reverse=True, key=lambda x: x[3])


def show(answer, data):  # TOGGLE IN INTERFACE VER
    if 'only' in answer.lower() or 'lib' in answer.lower():  # Only shows Libraries alphabetically
        data.sort(key=lambda x: x[0])
        for items in data.copy():
            if not 'library' in items[0].lower():
                data.remove(items)


def search(answer, data):  # ENTRY BOX IN INTERFACE VER
        ### Probably each word the same = +5 and each letter the same = +1 or something would be better
        words = answer.split()

        for sorted_words in data.copy():
            count = 0
            for single_words in words:
                if single_words.lower() in sorted_words[0].lower():
                    # once found in it
                    count += sorted_words[0].lower().count(single_words.lower())

            if count == 0:  # If no words matching the sort
                data.remove(sorted_words)
            else:  # Appends the count of common word instances
                data[data.index(sorted_words)].append(count)


def range(answer, data):  # ENTRY BOX IN INTERFACE VER
    # in range of 5-1000
    boundary = answer.split('-')
    data.sort(key=lambda x: x[1])
    for items in data.copy():
        if not int(boundary[0]) <= items[1] <= int(boundary[1]):
            data.remove(items)