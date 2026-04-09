def reverse(number):
    #Reverse the string
    reversed_number = str(number)[::-1]
    reversed_chunks = [reversed_number[index: index + 3] for index in range(0, len(reversed_number), 3)]
    return [int(chunk[::-1]) for chunk in reversed_chunks]
    

def say(number):

    #Zero is a problematic case for code's logic
    if number == 0:
        return "zero"

    #Error handling
    if number > 999999999999 or number < 0:
        raise ValueError("input out of range")
    
    basic_values = {
    # 0-20
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",

    # Tens
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}
    scales = ["", " thousand ", " million ", " billion "]
    
    chunks = reverse(number)
    #Work with chunks
    result = []
    for degree, chunk in enumerate(chunks):
        tens_ones = ""
        hundreds = ""
        
        #Scale
        scale = scales[degree]
        
        #Hundreds
        if chunk // 100:
            hundreds = basic_values[chunk // 100] + " hundred "
        
        #Tens_ones
        if chunk % 100 in basic_values and chunk != 0:
            tens_ones = basic_values[chunk % 100] + scale
        elif chunk != 0: 
            ones = basic_values[chunk % 10]
            tens = basic_values[chunk % 100 - chunk % 10]
            tens_ones = tens + "-" + ones + scale
    
        result.insert(0, f"{hundreds}{tens_ones}")

    result = "".join(result)
    return result.rstrip()