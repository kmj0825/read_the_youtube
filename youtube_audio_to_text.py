import time
import pickle
from pytube import YouTube
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
import whisper


def youtube_audio_to_text(link):
    yt = YouTube(link)
    yt.streams.filter(only_audio=True).first().download \
        (output_path=".", filename="test.mp3")

    start = time.time()
    model = whisper.load_model("small")
    text = model.transcribe("test.mp3")
    end = time.time()

    print(text["text"])
    print(f"{end - start:.2f}sec")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=50,
        length_function=len, )

    full_docs = text["text"]
    docs = [Document(page_content=x) for x in text_splitter.split_text(text["text"])]

    split_docs = text_splitter.split_documents(docs)

    with open("split_example_small.pkl", "wb") as f:
        pickle.dump(split_docs, f)

    return split_docs, full_docs
