"""
Given a number n as input, write it In words. Note that n is between 0 and 99.
Input-> 14
Output-> Fourteen
"""

once = [' ','One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ',
        'Eight ', 'Nine ', 'Ten ', 'Eleven ', 'Twelve ', 'Thirteen ', 'Fourteen ',
        'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ', 'Nineteen ']

tens = ['',' ','Twenty ', 'Thirty ', 'Forty ', 'Fifty ',
        'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']

n = int(input("Enter Number: "))
output = " "

if (n==0):
  output = "Zero"

elif (n<=19):
  output = once[n]

elif (n<=99):
  output = tens[n//10]+""+ once[n%10]

else:
  print("Enter Number between 0 to 99")

print(output)

