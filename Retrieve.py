import os
import json
import time
from ES_Class import ElasticSearchClient
import pickle
import json

project_dir = os.getcwd()
data_dir = os.path.join(project_dir, "data")


def listfiles(path):
    all_files = []
    for d in os.listdir(path):
        if os.path.isdir(os.path.join(path, d)):
            all_files.extend(listfiles(os.path.join(path, d)))
        else:
            all_files.append(os.path.join(path, d))
    return all_files


def load_docs(data_path):
    all_files = listfiles(data_path)
    all_docs = []
    for file in all_files:
        with open(file, "r", encoding="utf-8") as fin:
            for line in fin.readlines():
                doc = json.loads(line)
                all_docs.append(doc)
    print(f"loaded {len(all_docs)} number docs in {os.path.split(data_path)[-1]} directory")
    return all_docs


def save_wiki_docs(es, wiki_docs):
    # 创建维基百科索引
    mappings = {
        "properties": {
            "id": {
                "type": "long"
            },
            "url": {
                "type": "text",
                "index": True,
                "analyzer": "keyword"
            },
            "title": {
                "type": "text",
                "index": True,
                "analyzer": "ik_max_word",
                "similarity": "BM25"
            },
            "text": {
                "type": "text",
                "index": True,
                "analyzer": "ik_max_word",
                "similarity": "BM25"
            }
        }
    }
    index = "wiki_baike"
    es.delete_es_index(index_name=index)
    es.create_index(index_name=index)
    es.set_index_mapping(index=index, mappings=mappings)
    # 维基百科所有的文档存到es的索引中
    es.add_date_bulk(index, wiki_docs, batch_size=5000)



if __name__ == '__main__':
    es = ElasticSearchClient(host="localhost", port=9200)

    # loading wiki baike data
    wiki_dir = os.path.join(data_dir, "wiki_zh")
    wiki_docs = load_docs(wiki_dir)
    save_wiki_docs(es, wiki_docs)

    my_query = "交通，房地产， 电竞， 有轨电车， 体育赛事， 出行高峰 "

    query = {
        "query": {
            "match": {
                "text": {
                    "query": my_query,
                    # "operator": "or",  # 多个关键词匹配策略：or：只要匹配到一个关键词就可以返回， and：要完全匹配到所有的才返回
                    # "fields": ["text", "title"],
                }
            }
        },
        # "from": 0,  # 从 0 开始匹配
        # "size": 1000  # 返回多少条查询结果
    }
    # query = {
    #     "query": {
    #         "multi_match": {
    #             "query": my_query,
    #             "fields": ["content", "title", "desc"],
    #             "minimum_should_match": rate
    #         }
    #     },
    # #     "size": 20  # 返回多少条查询结果
    # }
    # query = {
    #     "query": {
    #         "query_string": {
    #             "query": f"text:(\"{location}\" AND \"{poi}\")",
    #             "default_operator": "and"
    #         }
    #     },
    #     "size": 20  # 返回多少条查询结果
    # }
    start = time.time()
    index = "news"
    response = es.search_by_query(index=index, query=query)  # 默认返回前10个最相关的文档， 根据匹配score已排序
    # es_result = es.search_by_scan(index, query, threshold=100)  # 使用scan查询
    result = response['hits']['hits']
    end = time.time()
    print(f"query: {my_query}")
    print(f"查询返回结果数：{len(es_result)}")
    with open("./data/search_result.json", "w") as fout:
        for re in es_result:
            t = json.dumps(re, ensure_ascii=False)
            fout.write(t + "\n")
    # i = 0
    # for re in es_result:
    #     print(f"{i} : score = {re['_score']}")
    #     print(f"result: {re['_source']}")
    #     i += 1
    print(f"each query costs time {end - start} s")



