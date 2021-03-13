
# from pytube import YouTube

# youtube_video_url = 'https://www.youtube.com/watch?v=DkU9WFj8sYo'

# try:
#     yt_obj = YouTube(youtube_video_url)

#     filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

#     # download the highest quality video
#     filters.get_highest_resolution().download()
#     print('Video Downloaded Successfully')
# except Exception as e:
#     print(e)



# from pytube import YouTube
 
# youtube_video_url = 'https://youtu.be/RAwntanK4wQ?list=PLwgFb6VsUj_lQTpQKDtLXKXElQychT_2j'
 
# try:
#     yt_obj = YouTube(youtube_video_url)
 
#     yt_obj.streams.get_audio_only().download(output_path='C:/Users/Jigs/Desktop', filename='audio')
#     print('YouTube video audio downloaded successfully')
# except Exception as e:
#     print(e)



# from pytube import Playlist
 
# try:
#     playlist = Playlist('https://www.youtube.com/watch?v=RAwntanK4wQ&list=PLwgFb6VsUj_lQTpQKDtLXKXElQychT_2j')
 
#     playlist.download_all(download_path='D:\Py3')
 
# except Exception as e:
#     print(e)


from pytube import YouTube

url = input("Enter Targetted URL :")
youtube_video_url = url

types = input("Select file types, Press 'A' for Audio or Press 'V for Vidoe : ").lower()
# types = types.lower()
if(types == "v"):
        try:
            yt_obj = YouTube(youtube_video_url)

            filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

            # download the highest quality video
            filters.get_highest_resolution().download()
            print(f'{yt_obj.title} Video is downloaded successfully')
        except Exception as e:
            print(e)


elif(types == "a"):
        try:
            yt_obj = YouTube(youtube_video_url)

            yt_obj.streams.get_audio_only().download(
                output_path='C:/Users/Jigs/Desktop', filename=yt_obj.title)
            print(f'{yt_obj.title} audio is downloaded successfully')
        except Exception as e:
            print(e)
else:
    print("Plaese input valid file types")
