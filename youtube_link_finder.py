# Takes a youtube link and outputs only the video ID


link = input("Youtube link goes here > ")
print("Video ID: " + link[len(link)-11:])