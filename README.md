# Don't Just watch Youtube, <font color="#c00000">READ IT!</font>
# Concepts 
People usually fall for the YouTube algorithm, and I'm just repeating that you should read the book. 
But is the YouTube algorithm keeping people from reading books? 
Why don't people read books? 

1. YouTube or SNS is more fun. 
2. videos are easier to understand and absorb information than books 

### but I thought about it more deeply. 

## Let me give you an example. 
![](https://i.imgur.com/D3VFRDW.jpg)

![](https://i.imgur.com/OXcj9CS.png)
Henry, 24, took a break from YouTube and went to the library to read a book. It's been a while since I've read a book, and I'm not sure what to read, so let's take a look at the new book section first. 

There are a lot of different books, but they all have colorful covers, and they all look interesting. I pick up a novel among them. As I read the front, I glance over and see an economics book with a "buy now to succeed" tagline. I decide that reading an economics book will be much more progressive than reading a novel. After reading a few chapters, I realize I am not interested and put the book down. 

Still, since I'm in the library, I think I should take a look at the books in my major. Henry is majoring in computer science, so I go to the engineering section and see that it's stacked with books again. I think I need to learn this, I think I need to learn that. In the end, I leave the library without picking a book.

What do you think, haven't we all had this experience? 

The above example is something I often experience whenever I go to the school library.

If you don't go in with an idea of what you want to read, those 30-40 minutes will go by quickly.


# This is what I focused on. 


What if people could get book recommendations from their favorite YouTube videos?
Wouldn't that make it easier for them to decide which books they wanted to read more? 
 
When people are asked what books or authors they've been reading lately, they don't have a good answer. But if you ask them to name their favorite YouTubers, they'll probably tell you right away. 

There's a lot to be said for recommending a book based on a video they've recently watched that they found interesting.

## 1. you don't get confused about which book to read.
## 2. you can deepen the shallow knowledge you have gained through YouTube with a book. 

SO! Add the video you want, choose the category you want !

Expand your interests beyond YouTube to books !
Expand your knowledge with our programs !
![](https://i.imgur.com/vInRAva.png)
- - - 

# Prerequisitions 
1. Your own <font color="#1f497d">OpenAI</font> API Key 
2. Your Favorite <font color="#c00000">Youtube</font> Link

# How Can I Start It?  
## If you want to use a single click ! 
[READ THE YOUTUBE GRADIO LINK](https://8d07a9368ff0146472.gradio.live)

This link is a public URL that is working on my personal computer. 

It will be up for 3 days, so I will be constantly modifying it. 😄

(Current uploaded link time: 12/10 19:35 ~ 12/13 19:35) 


## If You Want to use in Local! 
1. Clone this repository and Run the app.py in your Terminal

( I Made this with Python 3.9 if your python version is lower than 3.9, than you can get an error.. )
```python
git clone https://github.com/kmj0825/read_the_youtube.git
pip install -q gradio requests
pip install -q openai tiktoken langchain
pip install -q openai-whisper pytube
cd read_the_youtube 
python app.py    
```
2. Click on the URL. 
   ( You can run the program locally, but because it uses the GPU, it will recommend books to you faster if you run it in Colab or in an environment with a GPU.)
![](https://i.imgur.com/KxlyigP.png)

# How Can I Use it? 
1.  Paste Your Own OpenAI API Key 
   (We would have loved to provide a public API key😢, but due to cost considerations, we unfortunately implemented it to use a private API key. )!
2. Paste Your Favorite Youtube Link
![](https://i.imgur.com/p0Rasiy.png)
3. Select the Categories
![](https://i.imgur.com/ZiWbTN0.png)
4. Discover the book you want!
![](https://i.imgur.com/gqHY8Ix.png)

# Suggested examples

- 과학
![](https://i.imgur.com/JkTk63d.png)

- 소설 
![](https://i.imgur.com/1xIkmAq.png)

- 사회
![](https://i.imgur.com/pqfFTmy.png)

- 금융 
![](https://i.imgur.com/bakSf8A.png)

# How did you create it? 
- We used the Whisper model to characterize the downloaded YouTube speech.
- We adjusted the transcribed text through Map-Reduce so that it doesn't go beyond the tokens that GPT can accept as input.
- We used the GPT API to summarize the text and tuned the prompt to select one keyword from that summary. 
- We implemented the Aladdin Book Search API to search for books with those keywords and get the information 
- We used the Gradio library to make the course available on the web.

# Limitation 
The current whisper model takes a lot of time to convert audio to text
It takes between 40-80 seconds for a 2-3 minute YouTube video, and between 240-300 seconds for a 10+ minute YouTube video. 
After the project is over, we will think about how to solve this bottleneck and improve it.

We wanted to make it easy for everyone to use through Gradio Space, but due to the lack of GPU capacity of Free Acount, we were unable to run the program because it requires server maintenance fees. 
We plan to continue further development through Colab or other cloud services. 
[Gradio Space Link](https://huggingface.co/spaces/raphael825/read_the_youtube)

It is not free because it uses GPT to continuously use the API.
We are planning to change the program to be available for free through a different language model other than using the API.
- - -
# Reference 
[빵형의 개발도상국 - 유튜브 보는 것도 지겹다 - 유튜브 영상 요약 인공지능 만들어볼까요?](https://www.youtube.com/watch?v=g77Ob5_hPKE)


[Gradio 공식 Documents](https://www.gradio.app/docs)


[Aladin API](https://docs.google.com/document/d/1mX-WxuoGs8Hy-QalhHcvuV17n50uGI2Sg_GHofgiePE/edit)

# License 
Our Project is Apache License 2.0 

Below are the license descriptions for the ones we used

[Whisper](https://github.com/openai/whisper/blob/main/LICENSE) : MIT License 

[Langchain](https://github.com/langchain-ai/langchain/blob/master/LICENSE) : MIT License

[gradio](https://github.com/gradio-app/gradio/blob/main/LICENSEv) : Apache License 2.0

[tiktoken](https://github.com/openai/tiktoken/blob/main/LICENSE) : MIT License 

[openai-openapi] (https://github.com/openai/openai-openapi/blob/master/LICENSE) : MIT License 
