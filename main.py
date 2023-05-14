import csv
import os
import sys
import subprocess

def main():
    args = sys.argv
    del(args[0])

    if len(args) > 0 and args[0] == '-h':
        subprocess.run(['yt-dlp', '-h'])
        exit(0)

    argstr = ' '.join(str(x) for x in args)


    with open('subscriptions.csv', newline='') as subs:
        reader = csv.reader(subs)
        for row in reader:
            if len(row) == 0:
                continue
            print(f'Downloading {row[2]}')
            cmd = f'yt-dlp https://youtube.com/channel/{row[0]} {argstr}'
            print(cmd)

if __name__ == '__main__':
    main()