import faiss
import numpy as np

dimension = 384
index = faiss.IndexFlatL2(dimension)

def store_vector(embedding):
    vector = np.array(embedding).astype('float32')
    index.add(vector)