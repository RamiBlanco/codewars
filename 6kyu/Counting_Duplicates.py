#Write a function that will return the count of distinct case-insensitive 
#alphabetic characters and numeric digits that occur more than once in the 
#input string. The input string can be assumed to contain only alphabets 
#(both uppercase and lowercase) and numeric digits.


#Examples

#"abcde" -> 0 # no characters repeats more than once
#"aabbcde" -> 2 # 'a' and 'b'
#"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
#"indivisibility" -> 1 # 'i' occurs six times
#"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
#"aA11" -> 2 # 'a' and '1'
#"ABBA" -> 2 # 'A' and 'B' each occur twice
import re

def duplicate_count(text):
    if(bool(re.match('^[a-zA-Z0-9]*$',text))==True):
        text = text.upper()
        dup_count=0
        while len(text) > 1:
            if len(''.join(re.findall(text[0],text))) > 1:
                dup_count = dup_count + 1
            text = ''.join(re.split(text[0],text))
    else:
        return "Error"
    return dup_count
  
    
print(duplicate_count("aA11%"))