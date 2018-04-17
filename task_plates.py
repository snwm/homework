plate = int(input())
detergent = int(input()) * 2

limit = plate if plate < detergent else detergent

i = 0
while i < limit:
	plate -= 1
	detergent -= 1
	i += 1

if(plate > detergent):
    print('Моющее средство закончилось. Осталось', plate, 'тарелок')
elif(detergent > plate):
    print('Все тарелки вымыты. Осталось', detergent / 2, 'ед. моющего средства')
else:
    print('Все тарелки вымыты, моющее средство закончилось')