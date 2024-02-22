
import os
import logging
import sys

os.environ["OPENAI_API_KEY"] = "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"

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)



