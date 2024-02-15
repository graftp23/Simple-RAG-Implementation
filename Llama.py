from llama_index import StorageContext, load_index_from_storage,VectorStoreIndex,SimpleDirectoryReader
import openai
import os
import key

openai.api_key = key.openai_key

class database():
    def __init__(self,file):
        self.file = file
        self.query_engine = None
    
    def createload(self):
            current_directory = os.getcwd()  
            file_path = os.path.join(current_directory, "vectordb")

            if not os.path.isdir(file_path):
                    documents = SimpleDirectoryReader(input_files=[self.file]).load_data()
                    index = VectorStoreIndex.from_documents(documents)
                    query_engine = index.as_query_engine()
                    index.storage_context.persist("vectordb")
                    self.query_engine = query_engine
            else:
                    storage_context = StorageContext.from_defaults(persist_dir="vectordb")
                    new_index = load_index_from_storage(storage_context)
                    query_engine = new_index.as_query_engine()
                    self.query_engine = query_engine
            
    def query(self,q):
            if self.query_engine is not None: 
                response = self.query_engine.query(q)
                print(response)
            else:
                print("Initialize database first")

db = database("s70.txt")
db.createload()
db.query("how much is the price of s70")
          
 

                 
                 
                 




