import os
import sys

import time
import pickle
from langchain.chains.mapreduce import MapReduceChain
from langchain.chains import ReduceDocumentsChain, MapReduceDocumentsChain
from langchain.chat_models import ChatOpenAI
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
openai_api_key = "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"
# ==


with open ("/Users/a11/Library/Mobile Documents/com~apple~CloudDocs/2023-2/VS/OSS/1_project/split_example_small.pkl", "rb") as f:
    split_docs = pickle.load(f)

print(split_docs)

llm = ChatOpenAI(temperature=0, openai_api_key=openai_api_key)

# Map prompt
map_template = """The following is a set of documents
{docs}
Based on this list of docs, please identify the main themes
Helpful Answer:"""

map_prompt = PromptTemplate.from_template(map_template)

# Reduce prompt
reduce_template = """The following is set of summaries:
{doc_summaries}
Take these and distill it into a final, consolidated summary of the main themes.
The final answer is a single paragraph of about 100 words and must be in Korean.
Helpful Answer:"""

reduce_prompt = PromptTemplate.from_template(reduce_template)