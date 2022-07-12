import os, time

def clear_folder(folder_name):
    images = os.listdir(folder_name)
    for image in images:
        os.remove(f'{folder_name}/{image}')

def lock_system():
    os.system('xdotool key Super+l')

def unlock_system():
    time.sleep(1)
    os.system('xdotool key 6')
    os.system('xdotool key 0')
    os.system('xdotool key 2')
    os.system('xdotool key 4')
    os.system('xdotool key 8')
    os.system('xdotool key 8')
    os.system('xdotool key Return')