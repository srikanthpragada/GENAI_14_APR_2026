# Load document from Text File

from langchain_community.document_loaders.text import TextLoader

# Load the text file
loader = TextLoader("./docs/mlk.txt")
# Load the documents
docs = loader.load()
print("Document Count : ", len(docs))
print("Length of doc  : ", len(docs[0].page_content))

print(docs[0].page_content[:50])

