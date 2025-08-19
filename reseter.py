import time
import subprocess
print("в качестве диска для форматирования указан /dev/sda\nесли у вас он называется по другому то замените в коде /dev/sda на ваш")
timeee = int(input("На сколько поставить таймер?\nВ секундах:"))
b = 0
warningg = 10

while b <= timeee:
    subprocess.run(['clear'])
    print(b, "секунд прошло от", timeee)
    b += 1
    time.sleep(1)
subprocess.run(['spd-say','"start"'])
while warningg != 0:
    warningg -= 1
    warnings = str(warningg)
    subprocess.run(['spd-say',warnings])
    warningg = int(warnings)
    time.sleep(1)
    if warningg == 0:
        subprocess.run(['dd', 'if=/dev/zero', 'of=/dev/sda', 'oflag=sync', 'status=progress']) #В этой стоке  нужно заменить диск
