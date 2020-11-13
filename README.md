# es_search
elasticsearch 在 python 中的使用demo。
# 一、运行条件:
1.elasticsearch安装
elasticsearch在ubuntu中的docker安装与启动，非常简单。
https://blog.csdn.net/Thanours/article/details/109592219
也可以到官方网址参考安装教程https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html
2. python环境：
python3.6
pip install elasticsearch==7.9.1

# 二、实现
1. 使用python实现elasticsearch的封装类，包括了增删改查， 以及批量入库， helpers scan查询方法。
2. elasticsearch mappings配置对中文使用ik分词器，elasticsearch如何配置ik分词器请参考：https://blog.csdn.net/Thanours/article/details/109619013
3. elasticsearch mappings配置查询使用BM25得分
4. 维基百科数据入库到elasticsearch， 并实现多种查询，包括match和multi_match、复合查询。
5. 可使用多个关键词查询，或整个句子问题去查询。可以指定返回结果数量。

# 三、使用
1. 完成 一 中的环境配置
2. 下载维基百科数据：https://github.com/brightmart/nlp_chinese_corpus/
3. 将下载回来的维基百科数据解压并放在data文件夹下。
4. 运行python Retrieve.py即可，查询结果将写入到文件中并保存到data文件夹下




