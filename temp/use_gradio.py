import gradio as gr
import re

from youtube_audio_to_text import youtube_sum
from text_summarize import gpt_summarize
from temp.api_link import call_api

def extract_video_id(url):
    youtube_regex = (r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    youtube_pattern = re.compile(youtube_regex)
    match = youtube_pattern.match(url)
    if not match:
        return None
    return match.group(6)

def summarize(url):
    split_docs = youtube_sum(url)
    result_json = gpt_summarize(split_docs)
    video_id = extract_video_id(url)
    embed = f"""<iframe width='560' height='315' src='https://www.youtube.com/embed/{video_id}' frameborder='0' allowfullscreen></iframe>"""
    api_data = call_api("../data/result.json", "data/book.json")
    return result_json , embed, api_data

demo = gr.Interface(
    fn=summarize,
    inputs=gr.Textbox(label="URL"),
    outputs=[gr.TextArea(label="Summary"), gr.HTML()],
)

demo.launch(debug=True, share=True)#


def extract_video_id(url):
    youtube_regex = (r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    youtube_pattern = re.compile(youtube_regex)
    match = youtube_pattern.match(url)
    if not match:
        return None
    return match.group(6)

# def summarize(url):
#     split_docs = youtube_sum(url)
#
#     result_json = gpt_summarize(split_docs)
#
#     video_id = extract_video_id(url)
#     embed = f"""<iframe width='560' height='315' src='https://www.youtube.com/embed/{video_id}' frameborder='0' allowfullscreen></iframe>"""
#     api_data = call_api("data/result.json", "data/book.json")
#     return result_json , embed, api_data

demo = gr.Interface(
    inputs=gr.Textbox(label="URL"),
    outputs=[gr.TextArea(label="Summary"), gr.HTML()],
    # outputs=gr.TextArea(label="Summary"),
)

demo.launch(debug=True, share=True)