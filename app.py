import os
import requests
import json
import re
import gradio as gr
from pytube import YouTube
import whisper
import time
import pickle
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain.chains.mapreduce import MapReduceChain
from langchain.chains import ReduceDocumentsChain, MapReduceDocumentsChain
from langchain.chat_models import ChatOpenAI
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from PIL import Image
from io import BytesIO

openai_api_key = ""


# for API

# # ==

def youtube_text(link):
    yt = YouTube(link)
    yt.streams.filter(only_audio=True).first().download(output_path=".", filename="test.mp3")

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

    with open("../../Desktop/23-2-Local/OS/temp/split_example_small.pkl", "wb") as f:
        pickle.dump(split_docs, f)

    return split_docs, full_docs


def youtube_sum(split_docs, full_docs, API_KEY):
    openai_key = API_KEY
    llm = ChatOpenAI(temperature=0.7, openai_api_key=openai_key)

    # Map prompt
    map_template = """The following is a set of documents
    {docs}
    Based on this list of docs, please identify the main themes
    Helpful Answer:"""

    map_prompt = PromptTemplate.from_template(map_template)

    # Reduce prompt
    reduce_template = """The following is set of summaries:
    {doc_summaries}
    You need to output two things from the above Video. 
    1. Write an executive summary 
    Read the following documents and write a summary that integrates them to quickly identify the main topics of the Video.
    Your summary should. 
    - Must be written in Korean 
    - Be a single paragraph
    - Be descriptive and detailed so that you can tell at a glance what is being said without having to look at the original Video. 
    2. Choose your keyword 
    The keywords have the following conditions 
    - Must be written in Korean 
    - Must be a single word 
    - Must be a noun 
    - Must be a word that appears in the Video 
    - Must be a word that is not a stopword 
    - Must be a word that is not a proper noun 
    - Must be a word that is not a number 
    - Must be a word that is not a verb 
    - Must be a word that is not a pronoun 
    - Must be a word that is not a preposition 
    - Must be a word that is not a conjunction 
    - Must be a word that is not an interjection 
    - Must be a word that is not an adjective 
    - Must be a word that is not an adverb 
    - Must be a word that is not a determiner 
    - Must be a word that is not a particle 
    - Must be a word that is not a numeral 
    - Output only one keyword

    Here is an example of the final output
    Summary: Document_summary
    Keyword: keyword

    Helpful Answer:"""

    reduce_prompt = PromptTemplate.from_template(reduce_template)

    reduce_chain = LLMChain(llm=llm, prompt=reduce_prompt)
    combine_documents_chain = StuffDocumentsChain(
        llm_chain=reduce_chain, document_variable_name="doc_summaries"
    )

    # Combines and iteravely reduces the mapped documents
    reduce_documents_chain = ReduceDocumentsChain(
        # This is final chain that is called.
        combine_documents_chain=combine_documents_chain,
        # If documents exceed context for `StuffDocumentsChain`
        collapse_documents_chain=combine_documents_chain,
        # The maximum number of tokens to group documents into.
        token_max=4000,
    )

    # 2. Map chain
    map_chain = LLMChain(llm=llm, prompt=map_prompt)

    # Combining documents by mapping a chain over them, then combining results
    map_reduce_chain = MapReduceDocumentsChain(
        # Map chain
        llm_chain=map_chain,
        # Reduce chain
        reduce_documents_chain=reduce_documents_chain,
        # The variable name in the llm_chain to put the documents in
        document_variable_name="docs",
        # Return the results of the map steps in the output
        return_intermediate_steps=False,
    )
    # Run
    result = map_reduce_chain.run(split_docs)
    print(result)
    with open("../../Desktop/23-2-Local/OS/temp/result.txt", "w") as f:
        f.write(result)
    return result


def text_to_arr(result):
    text = result

    # Regular expression to find the keyword
    match = re.search(r"Keyword:\s*(\w+)", text)

    if match:
        keyword = match.group(1)
        print("Keyword:", keyword)  # The keyword is in the first capturing group
    else:
        match = re.search(r"키워드:\s*(\w+)", text)
        keyword = match.group(1)  # No keyword found
        print("Keyword:", keyword)

    return keyword


def aladin_api(keyword, selected_option):
    aladin_key = 'ttbkangmj08250027001'
    keyword = keyword
    all_data = []
    if selected_option == "사회":
        key = keyword
        print(key)
        url = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={aladin_key}&Query={key}&QueryType=Keyword&Cover=Big&MaxResults=5" \
              "&start=1&SearchTarget=Book&output=js&Sort=SalesPoint&Version=20131101&CategoryId=798&outofStockFilter=1"
        response = requests.get(url)
        response_json = json.loads(response.text)
        all_data.append(response_json)

    elif selected_option == "과학":
        key = keyword
        print(key)
        url = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={aladin_key}&Query={key}&QueryType=Keyword&Cover=Big&MaxResults=5" \
              "&start=1&SearchTarget=Book&output=js&Sort=SalesPoint&Version=20131101&CategoryId=987&outofStockFilter=1"
        response = requests.get(url)
        response_json = json.loads(response.text)
        all_data.append(response_json)

    elif selected_option == "소설":
        key = keyword
        print(key)
        url = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={aladin_key}&Query={key}&QueryType=Keyword&Cover=Big&MaxResults=5" \
              "&start=1&SearchTarget=Book&output=js&Sort=SalesPoint&Version=20131101&CategoryId=1&outofStockFilter=1"
        response = requests.get(url)
        response_json = json.loads(response.text)
        all_data.append(response_json)

    elif selected_option == "금융":
        key = keyword
        url = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={aladin_key}&Query={key}&QueryType=Keyword&Cover=Big&MaxResults=5" \
              "&start=1&SearchTarget=Book&output=js&Sort=SalesPoint&Version=20131101&CategoryId=170&outofStockFilter=1"
        response = requests.get(url)
        response_json = json.loads(response.text)
        all_data.append(response_json)
        # request 보내기
    all_data = json.dumps(all_data, ensure_ascii=False, indent=4)
    with open("../../Desktop/23-2-Local/OS/temp/book.json", "wb") as f:
        f.write(all_data.encode("utf-8"))
    print(type(all_data))
    print(all_data)
    return all_data


def book_output(book_json):
    data = json.loads(book_json)

    if len(data[0]['item'][0]) != 0:
        title1 = data[0]['item'][0]['title']
        book_link1 = data[0]['item'][0]['link']
        cover_link1 = data[0]['item'][0]['cover']
        response1 = requests.get(cover_link1)
        image1 = Image.open(BytesIO(response1.content))
    else:
        title1 = "No Data"
        book_link1 = "No Data"
        image1 = Image.open("NO DATA.jpeg")

    if len(data[0]['item'][1]) != 0:
        title2 = data[0]['item'][1]['title']
        book_link2 = data[0]['item'][1]['link']
        cover_link2 = data[0]['item'][1]['cover']
        response2 = requests.get(cover_link2)
        image2 = Image.open(BytesIO(response2.content))
    else:
        title2 = "No Data"
        book_link2 = "No Data"
        image2 = Image.open("NO DATA.jpeg")

    if len(data[0]['item'][2]) != 0:
        title3 = data[0]['item'][2]['title']
        book_link3 = data[0]['item'][2]['link']
        cover_link3 = data[0]['item'][2]['cover']
        response3 = requests.get(cover_link3)
        image3 = Image.open(BytesIO(response3.content))
    else:
        title3 = "No Data"
        book_link3 = "No Data"
        image3 = Image.open("NO DATA.jpeg")

    return title1, image1, title2, image2, title3, image3, book_link1, book_link2, book_link3


def get_title(API_KEY, link, selected_option):
    docs, split_docs = youtube_text(link)
    result = youtube_sum(docs, split_docs, API_KEY)
    keywords = text_to_arr(result)
    all_data = aladin_api(keywords, selected_option)
    title1, image1, title2, image2, title3, image3, link1, link2, link3 = book_output(all_data)
    return result, title1, image1, title2, image2, title3, image3, link1, link2, link3


# Define the list of options for the Dropdown
options_list = ["사회", "과학", "소설", "금융"]

with gr.Blocks() as demo:
    gr.Markdown("Paste your Youtube Link and get the book recommandation")
    with gr.Column():
        with gr.Row():
            inp1 = gr.Textbox(label="Your OpenAI KEY")
            inp2 = gr.Textbox(label="Input Link")
        inp3 = gr.Dropdown(choices=options_list, label="Select a category")
        btn = gr.Button("Find the book")

    with gr.Column():
        out1 = gr.Textbox(label="Summary")
        with gr.Row():
            out2 = gr.Textbox(label="Title1")
            out4 = gr.Textbox(label="Title2")
            out6 = gr.Textbox(label="Title3")
        with gr.Row():
            out3 = gr.Image(label="Image1")
            out5 = gr.Image(label="Image2")
            out7 = gr.Image(label="Image3")
        with gr.Row():
            out8 = gr.HTML(label="Book Link1")
            out9 = gr.HTML(label="Book Link2")
            out10 = gr.HTML(label="Book Link3")
    btn.click(fn=get_title, inputs=[inp1, inp2, inp3],
              outputs=[out1, out2, out3, out4, out5, out6, out7, out8, out9, out10])

demo.launch()
