#Kerwin Aguilar
#CMP131-86520
#Week-06
#Lab-01
#Software Discount
#10/01/26
pack=99
amount=int(input('Enter quantity amount: '))
Total=amount*pack
twenty=Total*0.20
thirty=Total*0.30
forty=Total*0.40
fifty=Total*0.50
print(f'Price per package: ${pack}')
print(f'Original cost ${Total}')
if amount==0:
    print('Must buy something')
elif amount<10:
    print('No Discount')
elif 10<=amount<=19:
    print('Total discount: $',Total*0.20)
    print("Final cost: $",Total-twenty)
elif 20<=amount<=49:
    print('Total discount: $',Total*0.30)
    print('Final cost: $',Total-thirty)
elif 50<=amount<=99:
    print('Total discount: $',Total*0.40)
    print('Final cost: $',Total-forty)
else:
    print('Total discount: $',Total*0.50)
    print('Final Cost',Total-fifty)




