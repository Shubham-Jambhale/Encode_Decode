# Encode_Decode

# Question 

Given a string s, write a function ‘encode‘ that returns the Huffman encoding of that string as a
string of 0s and 1s and the Huffman dictionary as a tuple. Write another function ‘decode‘ which
takes the encoded string and a Huffman dictionary and returns the original string. Note that the
composition of encode and decode should be the identity function, i.e decode(*encode(s)) = s.
You can use that fact to test your code.

# Example 1

  s = ‘aabc’
  
  encode(s)
  
  (‘001011’, {‘a’: ‘0’, b: ‘10’, c: ‘11’})
  
  decode(‘001011’, {‘a’: ‘0’, b: ‘10’, c: ‘11’})
  
  ‘Aabc’
