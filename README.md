# Don't Just watch Youtube, <font color="#c00000">READ IT!</font>
## Concepts 


Deepen your knowledge by reading books related to your videos! 
![](https://i.imgur.com/vInRAva.png)

## Prerequisitions 
1. Your own <font color="#1f497d">OpenAI</font> API Key 
2. Your Favorite <font color="#c00000">Youtube</font> Link

## How Can I Use It?  
1. Clone this repository and Run the app.py in your Terminal
```python 
python app.py    
```
2. Click on the URL. 
   ( You can run the program locally, but because it uses the GPU, it will recommend books to you faster if you run it in Colab or in an environment with a GPU.)
![](https://i.imgur.com/yYmTyaS.png)
3.  Paste Your Own OpenAI API Key 
   (We would have loved to provide a public API key, but due to cost considerations, we unfortunately implemented it to use a private API key. )![](https://i.imgur.com/05TGGGe.png)
3. Paste Your Favorite Youtube Link
   
4. Select the Categories
5. Discover the book you want!

## How did you create it? 
- We summarized YouTube using the STT model and Map-Reduce. 
- Use the GPT API and the Book API to search for books based on keywords in the video from the summarized content. 


- - -
## Reference 
[빵형의 개발도상국 - 유튜브 보는 것도 지겹다 - 유튜브 영상 요약 인공지능 만들어볼까요?](https://www.youtube.com/watch?v=g77Ob5_hPKE)
