def transform(legacy_data):
    legacy_data = { 
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"],
    }
    for row in legacy_data:
        for letter in row:
            letter = letter.lower()  
            if letter in legacy_data:
                legacy_data[letter].append(col.index(letter))
    return data
