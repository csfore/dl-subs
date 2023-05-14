import csv

def main():
    with open('subscriptions.csv', newline='') as subs:
        reader = csv.reader(subs)
        for row in reader:
            if len(row) == 0:
                continue
            print(f'Downloading {row[2]}')
            print(f'yt-dlp https://youtube.com/channel/{row[0]}')

if __name__ == '__main__':
    main()