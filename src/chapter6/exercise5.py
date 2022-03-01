string = 'X-DSPAM-Confidence:0.8475'
colon_position = string.find(':')
print(float(string[colon_position + 1:]))
