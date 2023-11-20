import os
import sys
import json
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

def reshape_text(text):
    summary = text.rsplit("[", 1)[0]
    summary = summary.replace('Summary:', "")
    summary = summary.replace('summary:', "")
    summary = summary.replace('Keyword:', "")
    summary = summary.replace('keyword:', "")

    keyword = text.rsplit("[", 1)[1]
    keyword = keyword.replace("]", "")
    keyword = keyword.replace('"', "")
    keyword = keyword.replace(" ", "")
    keyword = list(keyword.split(","))
    result = {
        "summary": summary,
        "keyword": keyword
    }
    return result


with open ("/Users/a11/PycharmProjects/OSS_Project/data/split_example_small.pkl", "rb") as f:
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
You need to output two things from the above Video. 
1. Write an executive summary 
Read the following documents and write a summary that integrates them to quickly identify the main topics of the Video.
Your summary should. 
- Must be written in Korean 
- Be a single paragraph of 100 words or less 
- Be descriptive and detailed so that you can tell at a glance what is being said without having to look at the original Video. 
2. Choose your keywords 
The keywords have the following conditions 
- One-word expressions in Korean 
- Avoid adjectives and other expressions
- Output as a Python array (ex: [keyword1,keyword2,keyword3] )
- Output a total of 3 keywords 
You MUST make keyword as a python array!

Here is an example of the final output 
Summary : Document_summary 
Keyword : [ Keyword1,Keyword2,Keyword3 ]
Helpful Answer:"""

reduce_prompt = PromptTemplate.from_template(reduce_template)

# 1. Reduce chain
reduce_chain = LLMChain(llm=llm, prompt=reduce_prompt)

# Takes a list of documents, combines them into a single string, and passes this to an LLMChain
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

sum_result = map_reduce_chain.run(split_docs)
print(sum_result)
result_json = reshape_text(sum_result)

print(result_json)
result_json = json.dumps(result_json, ensure_ascii=False, indent=4)

with open("/Users/a11/PycharmProjects/OSS_Project/data/result.json", "w", encoding="utf-8") as f:
    f.write(result_json)

