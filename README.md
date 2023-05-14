# dl-subs

Uses `yt-dlp` to download the videos of every channel you're subbed to.

WARNING! THIS MAY USE A LOT OF STORAGE SPACE

## Installing

### Prerequisites

- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- The .csv file with your subs from [Google Takeout](https://takeout.google.com)
  - Deselect all, select YouTube and YouTube Music, All YouTube data included, deselect all, select `subscriptions` (towards the bottom)

### Using

- Clone this repo
- Run `main.py` with `subscriptions.csv` in the same directory

NOTE: All command-line arguments are passed into yt-dlp
I.E. `python main.py --recode mp4 --add-metadata` will run `yt-dlp https://youtube.com/channel/UChIs72whgZI9w6d6FhwGGHA --recode mp4 --add-metadata`

## License

Licensed under the MIT License, Christopher Fore 2023