import requests
import re

from tools.ConfigSingleton import ConfigSingleton


class TestVerb:
    '''测试几个普通动词的使用'''
    def setup(self):
        print(1)

    def teardown(self):
        print(2)

    # def test_get(self):
    #     # 只要有一个assert错误，这个用例就错误
    #     print(ConfigSingleton.getInstance().config.url)
    #     r = requests.get('http://httpbin.org/get')
    #     # print(r.text)
    #     # print(r.json()['headers']['Accept'])
    #     # print(r.json()['origin'])
    #     # print(r.status_code)
    #     assert r.status_code == 200
    #     assert r.json()['origin'] == '106.8.149.84,10.100.91.201'


    # def test_get_have_params(self):
    #     params = {'a': 'b', 'c': 'd'}
    #     r = requests.get('http://httpbin.org/get',params=params)
    #     # print(r.text)
    #     # print(r.json()['headers']['Accept'])
    #     # print(r.json()['origin'])
    #     assert r.json()['args']['a'] == 'b'
    #     print(r.status_code)
    #     assert r.status_code == 200
    #     assert r.json()['origin'] == '106.8.149.84,10.100.91.201'


    def test_post(self):
        # data和json的默认content-type不一样。data是表单，json是json
        data = {'a': 'b'}
        # json = {'json': 'json1'}
        # json = str(json)
        r = requests.post('http://httpbin.org/post', data=data)

        # print(r.json()['headers']['Accept'])
        # print(r.json()['origin'])
        # print(r.status_code)

        print(r.status_code)
        print(r.text)

        assert r.status_code == 200
        assert re.search(r'"origin": "(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})"', r.text)


if __name__ == '__main__':
    # t = TestVerb()
    # t.test_post()
    # import yaml
    # f = open('../config/config.yml', encoding='utf-8')
    # res = yaml.load(f)
    # print(res)
    print(1)