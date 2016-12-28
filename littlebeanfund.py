# coding=utf-8

import urllib2

# dt = Data Type?  kf = '开放式基金'?
# ft = Fund Type?
# st=asc 升序排序
# sd=2015-12-08&ed=2016-12-08
# URL='http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&st=asc&pi=1&pn=1'


def convert_content_to_raw_data(content):
    begin = content.find('[')
    end = content.find(']')
    return content[begin + 2 : end - 1]


def convert_raw_data_to_top10(fund_type, raw_data):
    result = []
    for fund_str in raw_data.split('","'):
        fund = fund_str.split(',')
        # fund[0] = fund id, fund[1] = fund name, fund[3] = 日期, fund[14] = 今年涨幅
        result.append((fund[0], fund[1], fund[14]))
    return {fund_type: result}


def convert_raw_data_to_funds(raw_data):
    result = []
    for fund_str in raw_data.split('","'):
        fund = fund_str.split(',')
        # fund[0] = fund id, fund[1] = fund name
        result.append((fund[0], fund[1]))
    return result


def build_top10_by_type(fund_type):
    url_template = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft={0}&sc=jnzf&st=desc&pi=1&pn=10&dx=1'
    url = url_template.format(fund_type)
    content = urllib2.urlopen(url).read()
    raw_data = convert_content_to_raw_data(content)
    return convert_raw_data_to_top10(fund_type, raw_data)


# The following are exported APIs
def get_top10():
    """
    hh = 混合型基金
    gp = 股票型基金
    all = 所以类型基金
    """
    return [build_top10_by_type('hh'),
            build_top10_by_type('gp'),
            build_top10_by_type('all')]


def get_funds():
    url = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&st=asc&pi=1&pn=5000'
    content = urllib2.urlopen(url).read()
    raw_data = convert_content_to_raw_data(content)
    return convert_raw_data_to_funds(raw_data)


def get_fund(fund_id):
    pass


if __name__ == '__main__':
    print get_funds()
    # print get_top10()
