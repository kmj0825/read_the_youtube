# Don't Just watch Youtube, <font color="#c00000">READ IT!</font>
# Concepts 
People usually fall for the YouTube algorithm, and I'm just repeating that you should read the book. 
But is the YouTube algorithm keeping people from reading books? 
Why don't people read books? 

1. YouTube or SNS is more fun. 
2. videos are easier to understand and absorb information than books 

but I thought about it more deeply. 

Let me give you an example. 
![](https://i.imgur.com/D3VFRDW.jpg)

![](https://i.imgur.com/OXcj9CS.png)
Henry, 24, took a break from YouTube and went to the library to read a book. It's been a while since I've read a book, and I'm not sure what to read, so let's take a look at the new book section first. 
There are a lot of different books, but they all have colorful covers, and they all look interesting. I pick up a novel among them. As you read the front, you glance over and see an economics book with a "buy now to succeed" tagline. You decide that reading an economics book will be much more progressive than reading a novel. After reading a few chapters, you realize you're not interested and put the book down. 
Still, since I'm in the library, I think I should take a look at the books in my major. Henry is majoring in computer science, so I go to the engineering section and see that it's stacked with books again. I think I need to learn this, I think I need to learn that. In the end, I leave the library without picking a book.

What do you think, haven't we all had this experience? 
The above example is something I often experience whenever I go to the school library.
If I don't go in with a book to read, I quickly get lost for 3-40 minutes. 


## This is what I focused on. 


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

# How Can I Use It?  
1. Clone this repository and Run the app.py in your Terminal
```python 
python app.py    
```
2. Click on the URL. 
   ( You can run the program locally, but because it uses the GPU, it will recommend books to you faster if you run it in Colab or in an environment with a GPU.)
![](https://i.imgur.com/KxlyigP.png)

3.  Paste Your Own OpenAI API Key 
   (We would have loved to provide a public API key, but due to cost considerations, we unfortunately implemented it to use a private API key. )!
4. Paste Your Favorite Youtube Link
![](https://i.imgur.com/p0Rasiy.png)
5. Select the Categories
![](https://i.imgur.com/ZiWbTN0.png)
6. Discover the book you want!
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
- We summarized YouTube using the STT model and Map-Reduce. 
- Use the GPT API and the Book API (Aladin)to search for books based on keywords in the video from the summarized content. 
- Use Gradio to handle the page 

# Limitation 
The current whisper model takes a lot of time to convert audio to text
It takes between 40-80 seconds for a 2-3 minute YouTube video, and between 240-300 seconds for a 10+ minute YouTube video. 
After the project is over, we will think about how to solve this bottleneck and improve it.

We wanted to make it easy for everyone to use through Gradio Space, but due to the lack of GPU capacity, we were unable to run the program because it requires server maintenance fees. 
We plan to continue further development through Colab or other cloud services. 

It is not free because it uses GPT to continuously use the API.
We are planning to change the program to be available for free through a different language model other than using the API.
- - -
# Reference 
[빵형의 개발도상국 - 유튜브 보는 것도 지겹다 - 유튜브 영상 요약 인공지능 만들어볼까요?](https://www.youtube.com/watch?v=g77Ob5_hPKE)
[Gradio 공식 Documents](https://www.gradio.app/docs)
[Aladin API](https://docs.google.com/document/d/1mX-WxuoGs8Hy-QalhHcvuV17n50uGI2Sg_GHofgiePE/edit)
