English | [中文](README_zh.md)

# es_search
A demo of elasticsearch in python.  
Implement additions, deletions, changes, and queries, as well as batch storage, match, multi_match and compound queries, and helpers scan query methods.
For more details on elasticsearch search query methods, please check https://blog.csdn.net/Thanours/article/details/109625553
## 一、Running conditions:
1.Install elasticsearch   

  elasticsearch在ubuntu中的docker安装与启动，非常简单。  
  https://blog.csdn.net/Thanours/article/details/109592219  
  也可以到官方网址参考安装教程https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html

2.python：   

  python3.6  
  pip install elasticsearch==7.9.1

## 二、Implement
1. 使用python实现elasticsearch的封装类，包括了增删改查， 以及批量入库， helpers scan查询方法。
2. elasticsearch mappings配置对中文使用ik分词器，elasticsearch如何配置ik分词器请参考：https://blog.csdn.net/Thanours/article/details/109619013
3. elasticsearch mappings configure query to use BM25 score
4. Wikipedia data is stored in elasticsearch, and a variety of queries are implemented, including match and multi_match, and compound queries.
5. You can use multiple keyword queries, or whole sentence questions to query. The number of returned results can be specified.

## 三、Running
1. Complete the environment configuration in (1);

2. Download Wikipedia data：https://github.com/brightmart/nlp_chinese_corpus/;

3. Unzip the downloaded Wikipedia data and put it in the data folder;

4. Run python Retrieve.py, and the query results will be written to a file and saved to the data folder

## 四、Reference
https://zhuanlan.zhihu.com/p/95532596

## csdn博客  
https://blog.csdn.net/Thanours?spm=1011.2124.3001.5113

