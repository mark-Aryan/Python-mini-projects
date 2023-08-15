import streamlit as st
from pytube import YouTube
from io import BytesIO

# Set the Streamlit title and header
st.title("YouTube Video Downloader")
st.header("Download YouTube Videos by URL")

# Input box for entering the YouTube URL
video_url = st.text_input("Enter the YouTube URL:", "")

if st.button("Download"):
    if video_url:
        try:
            # Create a YouTube object
            yt = YouTube(video_url)

            # Get the highest resolution stream
            stream = yt.streams.get_highest_resolution()

            # Get the video title for the downloaded file
            video_title = yt.title
            video_title = video_title.replace(" ", "_") + ".mp4"

            # Create a BytesIO buffer and write the video content to it
            buffer = BytesIO()
            stream.stream_to_buffer(buffer)
            buffer.seek(0)  # Reset the buffer's position

            # Provide a download link for the video content
            st.download_button(
                label="Click to download",
                data=buffer,
                file_name=video_title,
                key="download_button",
            )
            st.success(f"Video '{video_title}' downloaded successfully!")
        except Exception as e:
            st.error("An error occurred. Please check the URL and try again.")
            st.error(str(e))

# Display some instructions
st.markdown("Enter a YouTube URL above and click the 'Download' button to download the video.")
