h = float(input(("Введите Ваш рост: ")))
w = float(input(("Введите Ваш вес: ")))
c = float(input(("Введите Ваше количество шагов: ")))
t = float(input(("Введите Ваше время в движении: ")))
dlina_shaga = (h/4)+0.37
K = dlina_shaga*c
V = K/(t*60)
#
cal = 0.035*w+(V**2)/h*0.029*w
K = round(K,3)
cal = round(cal,3)
print()
print()
print(f'Пройденная дистанция : {K}')
print(f'Кол-во соженных калорий в минуту : {cal}')
km=K/1000
print(f'Кол-во пройденных км : {km}')
if km<2:
    print("Вы прошли меньше двух километров, необходимо работать усерднее!")
elif km<4:
    print("Вы прошли больше двух километров, неплохо, но можно лучше!")
else:
    print("Прекрасно! Вы прошли больше 4 километров")
