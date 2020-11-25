import os
import time

def main():
    print(os.getpid())
    time.sleep(60)
    file = open("pz4.txt", 'a')
    file.write("STRING --------------------------\n")
    time.sleep(60* 3)
    #--------with
    time.sleep(6)
    with open("pz4.txt",'a') as file:
        file.write("STRING ++++++++++++++++++++++\n")
    time.sleep(60*3)
    print('fin')

    print(os.path.curdir)
    print(os.path.join(os.path.curdir, 'level1'))
    os.path.curdir = os.path.join('level1')
    print(os.path.join(os.path.curdir, 'level2'))








if __name__ == '__main__':
    main()