#Kerwin Aguilar
#CMP131-86520
#Week-06
#Lab-01
#Mobile bill
#10/01/26
print("Package 'A': For $39.99 per month 450 minutes are provided. Additional minutes are $0.45 per minute.")
print("Package 'B': For $59.99 per month 900 minutes are provided. Additional minutes are $0.40 per minute.")
print("Package 'C': For $69.99 per month unlimited minutes provided.")
pack=input('Which package would you choose?: ')
if pack=='A':
    minutes=int(input('How many minutes used this month?: '))
    additional=minutes-450
    charge=additional*0.45
    total=39.99+charge
    print(f"Total with package 'A' is ${total}")
elif pack=='B':
    minutes=int(input('How many minutes used this month?: '))
    additional=minutes-900
    charge=additional*0.40
    total=59.99+charge
    print(f"Total with package 'B' is ${total}")
elif pack=='C':
     minutes=int(input('How many minutes used this month?: '))
     print("Total with package 'C' is $69.99")
else:
    print('Invalid Package')
