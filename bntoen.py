bengali_to_english = {
    '০': '0',
    '১': '1',
    '২': '2',
    '৩': '3',
    '৪': '4',
    '৫': '5',
    '৬': '6',
    '৭': '7',
    '৮': '8',
    '৯': '9'
}

def convert_bengali_to_english(bengali_number):
    english_number = ''
    for char in bengali_number:
        if char in bengali_to_english or char.isdigit():
            if char in bengali_to_english:
                english_number += bengali_to_english[char]
            else:
                english_number += char
    return english_number