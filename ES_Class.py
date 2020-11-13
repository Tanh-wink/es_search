from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch import helpers
import json
import time


class ElasticSearchClient(object):
    # 实例和事务化单个node，若需要多个node，需要重构代码
    def __init__(self, host="localhost", port=9200):
        self.host = host
        self.port = port

        self.es_servers = [{
            "host": self.host,
            "port": self.port
        }]
        # http_auth是对设置了安全机制的es库需要写入 账号与密码，如果没有设置则不用写这个参数
        try:
            self.es_client = Elasticsearch(hosts=self.es_servers)
        except Exception as e:
            print(e)
            print('连接es失败，请查看是否连接。')

    # 进行创建一个数据库，即index
    def create_index(self, index_name, settings=None):
        """
        创建Index
        :param index_name:
        :param settings:
        setting = {
        "settings": {
            "number_of_replicas": 1,
            "number_of_shards": 1
            },
            "mappings": {
                "properties": {
                    "docid": {
                        "type": "text"
                    },
                    "doc": {
                        "type": "text"
                    },
                }
            }
        }
        :return:
        """
        if not self.es_client.indices.exists(index=index_name, ignore=[400, 404]):
            if settings is not None:
                self.es_client.indices.create(index=index_name, body=settings)
            else:
                self.es_client.indices.create(index=index_name)

    # 进行删除一个数据库，即index
    def delete_es_index(self, index_name):
        if self.es_client.indices.exists(index=index_name, ignore=[400, 404]):
            self.es_client.indices.delete(index=index_name)

    def set_index_mapping(self, index, mappings):
        # 设置mapping结构
        """
        设置index的mapping，类似于表结构。
        注意！！！！现在仅仅对mapping中的properties参数，其他的参数还很多
        前提为：已有index，并且已自定义分词器，详情见https://blog.csdn.net/u013905744/article/details/80935846
        输入参数举例说明：
            mapping = {
                'properties': {
                    'doc': {
                        'type': 'text',
                        'analyzer': 'whitespace',
                        'search_analyzer': 'whitespace',
                    },
                    'docid': {
                        'type': 'keyword',
                    }
                }
            }
        """
        self.es_client.indices.put_mapping(index=index, body=mappings)

    def add_date(self, index, data):
        """
        单条插入ES
        """
        self.es_client.index(index=index, body=data)

    def add_date_bulk(self, index, data, batch_size=2000):
        """
        批量插入ES,输入文本格式为单条插入的list格式
        """
        actions = []
        success_num = 0
        fail_num = 0
        start = time.time()
        batch_step = 1
        for idx, data_dict in enumerate(data):
            action = {
                "_index": index,
                "_id": idx,
                "_source": data_dict
            }
            actions.append(action)
            # 批量处理
            if len(actions) == batch_size or idx == len(data) - 1:
                success, failed = bulk(self.es_client, actions, raise_on_error=True)
                actions = []
                success_num += success
                fail_num += len(failed)
                print(f'{batch_step}: 成功插入了{success}条数据, 失败{len(failed)}条数据')
                batch_step += 1
        end = time.time()
        print(f'一共成功插入了{success_num}条数据, 失败{fail_num}条数据， 共花费{end - start}秒时间')

    def update_by_id(self, index, idx, data):
        """
        根据给定的_id,更新ES文档
        :return:
        """
        self.es_client.update(index=index, body={"doc": data}, id=idx)

    def delete_by_id(self, index, idx):
        """
        根据给定的id,删除文档
        :return:
        """
        self.es_client.delete(index=index, id=idx)

    def search_by_query(self, index, query, return_list=False):
        '''
        根据查询的query语句，来搜索查询内容
        '''
        search_result = self.es_client.search(index=index, body=query)
        if return_list:
            search_result = self.get_result_list(search_result)
        return search_result
	# 将查询返回处理成list
    def get_result_list(self, es_response):
        final_result = []
        result_items = es_response['hits']['hits']
        for item in result_items:
            final_result.append({
                    "score": item['_score'],
                    "result": item['_source']
                 }
            )
        return final_result
	# scan查询
    def search_by_scan(self, index, query, scroll='5m', timeout="1m", threshold=100):
        es_result = helpers.scan(
            client=self.es_client,
            query=query,
            scroll=scroll,
            index=index,
            timeout=timeout,
            preserve_order=True
        )

        final_result = []
        for item in es_result:
            if item['_score'] < threshold:
                break
            final_result.append({
                "score": item['_score'],
                "result": item['_source']
                }
            )

        return final_result


if __name__ == '__main__':

    es = ElasticSearchClient(host="localhost", port=9200)
    print(es)
    # # 创建索引
    # index = "test"
    # es.delete_es_index(index_name=index)
    # es.create_index(index_name=index)
