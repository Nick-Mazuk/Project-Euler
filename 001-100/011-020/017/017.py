#starts with onethousand because 1000 is an outlier
string = 'onethousand'

singles = 'onetwothreefourfivesixseveneightnine'
teens = 'teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen'
tens = 'twentythirtyfortyfiftysixtyseventyeightyninety'

#get all the instances of 100
for i in range(0,900):
    string += 'hundred'

#singles (100 for the hundreds which totals 100: five hundred, 9 for each within each hundred which totals to 90: five hundred and 1)
for i in range(0,190):
    string += singles

#teens (should be once for each hundred, so 10)
for i in range(0,10):
    string += teens

#tens (should be 10 for each hundred, so 100)
for i in range(0,100):
    string += tens

#and (should be 99 for each hundred after the 000s not counting the round hundreds, so 891)
for i in range(0,891):
    string += 'and'

print(len(string))
