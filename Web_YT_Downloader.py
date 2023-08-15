import streamlit as st
from pytube import YouTube

def download(url):
    youtubeObject = YouTube(url)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except Exception:
        print("An error has occurred")
    st.success("Download is completed successfully")


st.title("Youtube Video Downloader created by Aryan Kumar Upadhyay")
st.warning("For educational purpose only.")

try:
    link = st.text_input('The URL link')
    download(link)
except Exception as e:
    pass

