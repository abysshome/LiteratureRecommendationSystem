'''
Author: flwfdd
Date: 2024-05-07 20:57:23
LastEditTime: 2024-05-07 21:18:04
Description: 
_(:з」∠)_
'''

import csv

import faiss
import torch

EMBEDDING_DIM = 64
ARTICLES_PATH = './articles.csv'
ARTICLE_EMBEDDINGS_PATH = './article_embeddings_200.pt'
USER_EMBEDDINGS_PATH = './user_embeddings_200.pt'


class VectorDB_Faiss:
    def __init__(self, dim: int):
        self.dim = dim
        self.index = faiss.IndexFlatIP(dim)
        self.data = {}
        self.ids = []

    # 搜索点积TOP-K
    def search(self, vector, top_k: int = 10):
        _, I = self.index.search(vector.unsqueeze(0).detach().cpu().numpy(), top_k)
        return [self.ids[i] for i in I[0]]

    # 加载数据
    def load(self, path):
        self.data = torch.load(path, map_location=torch.device('cpu'))
        self.ids = list(self.data.keys())
        vectors = torch.stack(list(self.data.values()))
        self.index = faiss.IndexFlatIP(self.dim)
        self.index.add(vectors.detach().cpu().numpy())


# 文章类
class Article:
    def __init__(self, id: str, title: str, abstract: str, keywords: str, authors: str, url: str, timestamp: int,
                 doi: str):
        self.id = id
        self.title = title
        self.abstract = abstract
        self.keywords = keywords
        self.authors = authors
        self.url = url
        self.timestamp = timestamp
        self.doi = doi


# 初始化向量数据库
print('Loading embeddings...')
user_vector_db = VectorDB_Faiss(EMBEDDING_DIM)
article_vector_db = VectorDB_Faiss(EMBEDDING_DIM)
user_vector_db.load(USER_EMBEDDINGS_PATH)
article_vector_db.load(ARTICLE_EMBEDDINGS_PATH)

# 加载文章数据
print('Loading articles...')
article_dict = {}
with open(ARTICLES_PATH, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        article = Article(row['id'], row['title'], row['abstract'], row['keywords'],
                          row['authors'], row['url'], row['timestamp'], row['doi'])
        article_dict[article.id] = article


def recommend(user_id: str, top_k: int = 10):
    user_vector = user_vector_db.data[user_id]
    article_ids = article_vector_db.search(user_vector, top_k)
    return [article_dict[article_id] for article_id in article_ids]


# 测试
for i in recommend('1120190044'):
    print(i.title)
    print(i.authors)
    print(i.url)
    print()
