# Cute Wallpaper Scraper

![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

I love the customization vscode's extensions allow, specifically: Background by Katsute.

However, I have a really old laptop, that can't let katsute cycle more than 5 backgrounds at a time. <br>
So, I thought, why not make this a coding project!

I have three pinterest boards: <br>

* [Editor backgrounds](https://in.pinterest.com/coderlisha/vscode-editor/)
* [Sidebar backgrounds](https://in.pinterest.com/coderlisha/vscode-sidebar/)
* [Panel backgrounds](https://in.pinterest.com/coderlisha/vscode-panel/)

This project randomly chooses 1 from each (2 from sidebar) and saves them to this repository using Github Actions, every 30 minutes.

So now I have infinite cute backgrouds!

## How it works
It scrapes my pinterest boards, downloads some to cache, then pushes 1 pg and 1 gif per category to this repository. My global settings.json's background images point to the png and gifs store in the repo.

Since the names never change, I don't have to do anything except occasionally add more pins to my boards
