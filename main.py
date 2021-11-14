from pytube import YouTube

link = input("Paste a youtube video link here: ")

path = input(" Please insert a path to save your video: ")

yt = YouTube(link)

result = {
    
    "Title": yt.title,
    "Views": yt.views,
    "Length": yt.length, 
    "Rating": yt.rating

}

print(result)

ys = yt.streams.get_highest_resolution()

print ("Downloading your file... Please wait!")

ys.download(path)

print("Your file is ready to use! Thanks for using the app! Follow me on my GitHub.")

# A basic YouTube Video Downloader with python!
# My GitHub: https://github.com/Madeline-Lea
