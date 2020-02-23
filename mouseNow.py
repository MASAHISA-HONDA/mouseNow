import pyautogui
print("中断するにはCtrーCを押してください")

try:
    while True:
        #マウス座標を取得
        x,y = pyautogui.position()
        position_str = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)

except KeyboardInterrupt:
    print('\n終了')