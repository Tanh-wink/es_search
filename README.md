English | [中文](README_zh.md)

# es_search
A demo of elasticsearch in python.  
Implement additions, deletions, changes, and queries, as well as batch storage, match, multi_match and compound queries, and helpers scan query methods.
For more details on elasticsearch search query methods, please check https://blog.csdn.net/Thanours/article/details/109625553
## 一、Running conditions:
1.Install elasticsearch   

  The installation and startup of elasticsearch in ubuntu and docker is very simple. 
  https://blog.csdn.net/Thanours/article/details/109592219  
  You can also go to the official website to refer to the installation tutorial: https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html

2.python：   

  python3.6  
  pip install elasticsearch==7.9.1

## 二、Implement
1. Implement the encapsulation python class of elasticsearch, including addition, deletion, modification, query, batch storage, and helpers scan query methods.
2. The Elasticsearch mappings configuration uses the ik tokenizer for Chinese. For how to configure the ik tokenizer in elasticsearch, please refer to: https://blog.csdn.net/Thanours/article/details/109619013
3. Elasticsearch mappings configure query to use BM25 score
4. Wikipedia data is stored in elasticsearch, and a variety of queries are implemented, including match and multi_match, and compound queries.
5. You can use multiple keyword queries, or whole sentence questions to query. The number of returned results can be specified.

## 三、Running
1. Complete the environment configuration in (1);

2. Download Wikipedia data：https://github.com/brightmart/nlp_chinese_corpus/;

3. Unzip the downloaded Wikipedia data and put it in the data folder;

4. Run python Retrieve.py, and the query results will be written to a file and saved to the data folder

## 四、Reference
https://zhuanlan.zhihu.com/p/95532596

## CSDN Blog  
https://blog.csdn.net/Thanours?spm=1011.2124.3001.5113

