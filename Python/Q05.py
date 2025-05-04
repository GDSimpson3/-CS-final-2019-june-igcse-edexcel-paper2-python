#Q05FINISHED

libraryRecord =  [
["105MS" , "Marcus" , "Smith" , 25 ],
["103AZ" , "Anthony" , "Zarrent" , 5 ],
["108MW" , "Matt" , "White" , 12 ],
["112DB" , "Denise" , "Bilton" , 58 ],
["124MK" , "Malcolm" , "Kelly" , 26 ],
["116UK" , "Uzere" , "Kevill" , 29 ],
["127AL" , "Abduraheim" , "Leahy" , 94 ],
["124LS" , "Laura" , "Sampras" , 50 ],
["121AP" , "Azra" , "Potter" , 61 ],
["115AC" , "Anthony" , "Calik" , 10 ],
["117PI" , "Pablo" , "Iilyas" , 49 ],
["113MM" , "Mark" , "Montgomerie" , 68 ],
["130FH" , "Felicity" , "Heath" , 11 ],
["132JA" , "Jill" , "Alexander" , 61 ],
["123SG" , "Sara" , "Grimstow" , 9 ],
["134KD" , "Kevin" , "Dawson" , 74 ],
["122AB" , "Andrew" , "Bertwistle" , 42 ],
["125JF" , "Jaide" , "Feehily" , 55 ],
["128JS" , "Justin" , "Slater" , 68 ],
["126CG" , "Colleen" , "Grohl" , 39 ]
]
# ----------------------------------------------
# Write your code below this line

# Variables
TotalNumberOfBooksRead = 0
averageNumberofBooksRead = 0 

GoldMedal = ["","","",0]
SilverMedal = ["","","",0]
BronzeMedal = ["", "","", 0]

listOfUnderTen = []

# Global Loop

for student in libraryRecord:
    TotalNumberOfBooksRead = TotalNumberOfBooksRead + student[3]
    if student[3] < 10:
        listOfUnderTen.append(student[0]) # If we wanted to we could also send the names

    # Now 1st 2nd 3rd logic

    if student[3] > GoldMedal[3]:
        GoldMedal = student
    elif student[3] > SilverMedal[3]:
        SilverMedal = student
    elif student[3] > BronzeMedal[3]:
        BronzeMedal = student


averageNumberofBooksRead = TotalNumberOfBooksRead / len(libraryRecord)


print(f'The Gold Medal Goes to {GoldMedal[1]} {GoldMedal[2]} who read {GoldMedal[3]} Books!! (UserID: {GoldMedal[0]})')
print(f'The Silver Medal Goes to {SilverMedal[1]} {SilverMedal[2]} who read {SilverMedal[3]} Books!! (UserID: {SilverMedal[0]})')
print(f'The Bronze Medal Goes to {BronzeMedal[1]} {BronzeMedal[2]} who read {BronzeMedal[3]} Books!! (UserID: {BronzeMedal[0]})')

print("\n Here's a list of all those who have read less than 10 books")
for i in listOfUnderTen:
    print(f'   {i}')


print(f"\n The total Number of books read was: {TotalNumberOfBooksRead} \n and the Average number of books read is {averageNumberofBooksRead}")
