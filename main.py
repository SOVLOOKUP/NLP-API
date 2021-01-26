import httpx
from icecream import ic

class NLPAPI(httpx.AsyncClient):
    """
    see docs in https://github.com/SOVLOOKUP/NLP-API
    """
    def __init__(
        self,
        *,
        headers = httpx.Headers({
            "Host": "nlp.datahorizon.cn",
            "Connection": "keep-alive",
            # "Content-Length": "",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "Content-Type": "application/json",
            "Origin": "https://nlp.datahorizon.cn",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://nlp.datahorizon.cn/semantic.cgi.html",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "pgv_pvi=4672268288; pgv_si=s2550309888; Hm_lvt_f11bdbcccc1fe5e246f1e0e83cb7f4a3=1610531945,1610716599,1611640942; Hm_lpvt_f11bdbcccc1fe5e246f1e0e83cb7f4a3=1611642759"
        }),
        base_url = "https://nlp.datahorizon.cn/api/",
        ):
            super().__init__(
                headers = headers,
                base_url = base_url,
                timeout=10,
            )

    def err(self,resp:dict) -> str:
        ic(resp)
        return resp["errormsg"]

    async def event_triple(self,text:str) -> list:
        """### 主谓宾三元组提取
        
        *给定文本，得到该文本中的主谓宾三元组*
        
        #### return list[dict]

        [Object] 主语
        [Predicate] 谓语
        [Subject] 宾语
        """
        resp = (await self.post("ie/event_triple",json={"text":text})).json()
        if resp["errorcode"] != 0:
            self.err(resp)
        return resp["items"][0]


    async def num_triple(self,text:str) -> list:
        """### 数据元组提取
        
        *给定文本，识别出文本中的数据指标元组*

        #### return list[dict]

        [company] 主体
        [index] 指标名称
        [time] 时间
        [value] 数据
        """
        resp = (await self.post("ie/num_triple",json={"content":text})).json()
        if resp["errorcode"] != 0:
            self.err(resp)
        return resp["items"]

    async def causal_triple(self,text:str) -> list:
        """### 逻辑三元组提取
        
        *给定文本，识别出文本中的因果事件对*

        #### return list[dict]

        [cause] 原因
        [effect] 影响
        [label] 关系
        [sent] 事件
        """
        resp = (await self.post("ie/causal_triple",json={"content":text})).json()
        if resp["errorcode"] != 0:
            self.err(resp)
        return resp["items"]

    async def keyword(self,text:str) -> list:
        """### 关键词提取
        
        *给定文本，得到该文本的关键词集合*

        #### return list[dict]

        [keyword] 关键词
        [score] 权重
        """
        resp = (await self.post("ie/keyword",json={"text":text})).json()
        if resp["errorcode"] != 0:
            self.err(resp)
        return resp["items"][0]

    async def abstract(self,text:str) -> list:
        """### 摘要提取
        
        *给定文本，得到该文本的摘要片段*

        #### return list[dict]

        [score] 置信度
        [sentence] 摘要
        """
        resp = (await self.post("ie/abstract",json={"text":text})).json()
        if resp["errorcode"] != 0:
            self.err(resp)
        return resp["items"][0]

    async def chunck(self,text:str) -> list:
        """### 短语组块识别
        
        *给定文本，识别出文本中短语组块集合*

        #### return list[dict]

        [主谓短语]
        [动词短语]
        [名词短语]
        """
        resp = (await self.post("ie/chunck",json={"text":text})).json()
        if resp["errorcode"] != 0:
            self.err(resp)
        return resp["items"][0]["chunck_result"]

    async def ner(self,text:str) -> list:
            """### 实体识别
            
            *给定文本，识别文本中的人物、地点、组织机构和公司类实体。*

            #### return list[dict]

            [end_id] 结束位置
            [entity] 实体
            [start_id] 开始位置
            [type] 类型
            """
            resp = (await self.post("ie/ner",json={"text":text})).json()
            if resp["errorcode"] != 0:
                self.err(resp)
            return resp["items"][0]

    async def similarity(self,text1:str,text2:str) -> float:
        """### 文本相似性
        
        *给定两个文本，给出两个文本可判定为同指的概率值*

        #### return float

        相似概率值
        """
        resp = (await self.post("sc/similarity",json={"text1":text1,"text2":text2})).json()
        if resp["errorcode"] != 0:
            self.err(resp)
        return float(resp["items"][0]["content"])

    async def abstract_word(self,text:str) -> list:
            """### 概念抽象
            
            *给定一个词，输出该词对应的抽象概念路径*

            #### return list[str]

            """
            resp = (await self.post("sc/abstract_word",json={"word":text})).json()
            if resp["errorcode"] != 0:
                self.err(resp)
            return resp["items"]["paths"]

    async def semantic_word(self,text:str) -> dict:
            """### 语义联想
            
            *给定一个词，输出该词对应的近义词、反义词、 相关词*

            #### return dict

            [antiwords] 反义词
            [relatedwords] 相关词
            [simwords] 近义词
            """
            resp = (await self.post("sc/semantic_word",json={"word":text})).json()
            if resp["errorcode"] != 0:
                self.err(resp)
            return resp["items"]["words"]

    async def doc_sentiment(self,text:str) -> float:
            """### 情感分析
            
            *给定文本，识别出该文本的情感倾向*

            #### return float

            积极倾向概率
            """
            resp = (await self.post("ta/doc_sentiment",json={"content":text})).json()
            if resp["errorcode"] != 0:
                self.err(resp)
            return resp["items"][0]["score"]

    async def entity_sentiment(self,text:str) -> list:
            """### 情感对提取
            
            *给定文本，识别出该文本中存在的情感对*

            #### return list[dict]

            [entity] 实体
            [polar] 情感方向
            [score] 情感概率
            [stiwd] 趋势
            """
            resp = (await self.post("ta/entity_sentiment",json={"content":text})).json()
            if resp["errorcode"] != 0:
                self.err(resp)
            return resp["items"]
    
    async def attr_sentiment(self,text:str) -> list:
            """### 实体属性情感提取
            
            *给定文本，识别出该文本中存在的情感对*

            #### return list[dict]

            [entity] 实体
            [attr] 指标
            [polar] 情感方向
            [score] 情感概率
            [stiwd] 趋势
            """
            resp = (await self.post("ta/attr_sentiment",json={"content":text})).json()
            if resp["errorcode"] != 0:
                self.err(resp)
            return resp["items"]

    async def subjective_detect(self,text:str) -> float:
            """### 主观性得分
            
            *给定文本，返回该文本的主观性得分*

            #### return float

            主观性得分
            """
            resp = (await self.post("ta/subjective_detect",json={"text":text})).json()
            if resp["errorcode"] != 0:
                self.err(resp)
            
            return resp["items"]["score"]
    
    async def fetch_news(self,url:str) -> dict:
            """### 网页正文解析
            
            *给定URL，识别出该页面下的标题、发布时间和正文内容*

            #### return dict

            [news_content] 正文内容
            [news_pubtime] 发布时间
            [news_title] 标题
            """
            resp = (await self.post("ft/fetch_news",json={"url":url})).json()
            if resp["errorcode"] != 0:
                self.err(resp)
            return resp["items"][0]
    
    async def fetch_table(self,url:str) -> list:
            """### 网页表格解析
            
            *给定包含表格的 url，识别出该页面下的表格解析结果*

            #### return list

            表格
            """
            resp = (await self.post("ft/fetch_table",json={"url":url})).json()
            if resp["errorcode"] != 0:
                self.err(resp)
            return resp["items"]
    
if __name__ == "__main__":
    import time
    def p(name:str,task):
        print(name,"\t\t->\t\t" ,task)
        time.sleep(0.5)

    async def main():
        async with NLPAPI() as api:
            p( "主谓宾三元组提取", await api.event_triple("路透社24日援引英国《金融时报》消息称"))
            p( "逻辑三元组提取", await api.causal_triple("我们谨慎预测由于需求旺盛,公司产能扩大,公司配线系统产品收入有望由上年的3.53亿元提高到今年的5亿元以上"))
            p( "数据元组提取", await api.num_triple("截至2017年末，公司总资产26.55亿元，负债总额16.17亿元，所有者权益10.38亿元。2017年度，公司实现主营业务收入10.58亿元，净利润1.36亿元。"))
            p("关键词提取",await api.keyword("文章认为，美国金钱政治后果恶劣，剥夺了普通民众的政治权利；政府官职成为富人和上层阶级的禁脔；明目张胆地向富人输送利益；增加了解决枪支暴力等紧迫政治社会问题的难度。"))
            p("摘要提取",await api.abstract("国家卫健委今天（12月26日）上午举行例行发布会介绍我国冬春季常见病防控和节日健康信息，冬春季是流感、诺如病毒等所致的感染性腹泻等传染病的高发季节。根据最新监测，目前我国部分省份开始进入流感流行季节，今年主要以甲型（H3N2）和乙型维多利亚系（Victoria）为主。诺如病毒导致的感染性腹泻聚集性疫情有所增加，与往年同期基本持平。专家研判认为，未来随着学校和托幼机构放寒假，流感和感染性腹泻等聚集性疫情将逐渐减少。总的来看，目前我国传染病疫情形势总体平稳。"))
            p("短语组块识别",await api.chunck("教育部鼓励获得高中和中等职业学校毕业证的台商子女参加高职院校的分类考试招生"))
            p("实体识别",await api.ner("教育部鼓励获得高中和中等职业学校毕业证的台商子女参加高职院校的分类考试招生"))
            p("文本相似性",await api.similarity("你是猪","我是猪"))
            p("概念抽象",await api.abstract_word("香蕉"))
            p("语义联想",await api.semantic_word("苹果"))
            p("情感分析",await api.doc_sentiment("我觉得你很开心"))
            p("情感对提取",await api.entity_sentiment("铁矿石进口量之所以上涨,铁矿石价格走低，铁矿石总体行情是上涨。"))
            p("实体属性情感提取",await api.attr_sentiment("铁矿石进口量之所以上涨,铁矿石价格走低，铁矿石总体行情是上涨。"))
            p("主观性得分",await api.subjective_detect("元芳怎么看"))
            p("网页正文解析",await api.fetch_news("http://www.xinhuanet.com/politics/xxjxs/2019-12/23/c_1125376133.htm"))
            p("网页表格解析",await api.fetch_table("http://stock.eastmoney.com/a/201912181327460146.html"))
            pass

    import asyncio
    asyncio.run(main())
    
