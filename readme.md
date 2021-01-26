# NLP-API

[数地工厂](https://nlp.datahorizon.cn/)NLP-API python SDK 基于 httpx  协程 类型注释 代码注释完备

- 关键词提取
- 摘要提取
- 新词发现
- 事件三元组提取
- 数据三元组提取
- 逻辑三元组提取
- 实体识别
- 短语组块识别
- 相似度计算
- 概念抽象
- 语义联想
- 情感极性判定
- 情感对提取
- 实体属性情感提取
- 主观性计算
- 网页正文解析
- 网页表格解析
- 实体链接
- 问题解析
- 概念描述

为了调用方便写下这个库，**请尊重原作者劳动成果，仅用于学习研究，切勿刷API(后果自行负责，请查阅相关法律)，商业用途请联系API作者**

## Quick start



```python
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
```

返回：

```bash
主谓宾三元组提取 		->		 [{'Object': '英国金融时报消息', 'Predicate': '援引', 'Subject': '路透社'}]
逻辑三元组提取 		->		 [{'cause': '需求旺盛,公司产能扩大', 'effect': '公司配线系统产品收入有望由上年的3.53亿元提高到今年的5亿元以上', 'label': '由于', 'sent': '我们谨慎预测由于需求旺盛,公司产能扩大,公司配线系统产品收入有望由上年的3.53亿元提高到今年的5亿元以上'}]
数据元组提取 		->		 [{'company': '公司', 'index': '总资产', 'time': '2017年末', 'value': '26.55亿元'}, {'company': '公司', 'index': '负债总额', 'time': '2017年末', 'value': '16.17亿元'}, {'company': '公司', 'index': '所有者权益', 'time': '2017年末', 'value': '10.38亿元'}, {'company': '公司', 'index': '主营业务收入', 'time': '2017年度', 'value': '10.58亿元'}, {'company': '公司', 'index': '净利润', 'time': '2017年度', 'value': '1.36亿元'}]
关键词提取 		->		 [{'keyword': '政治', 'score': 1.0}, {'keyword': '富人', 'score': 0.9237}, {'keyword': '增加', 'score': 0.6167}, {'keyword': '金钱', 'score': 0.5953}, {'keyword': '美国', 'score': 0.5953}, {'keyword': '恶劣', 'score': 0.589}, {'keyword': '成为', 'score': 0.5285}, {'keyword': '暴力', 'score': 0.5281}, {'keyword': '政治权利', 'score': 0.5257}, {'keyword': '利益', 'score': 0.5232}]
摘要提取 		->		 [{'score': 1.0, 'sentence': '根据最新监测，目前我国部分省份开始进入流感流行季节，今年主要以甲型（H3N2）和乙型维多利亚系（Victoria）为主'}, {'score': 1.0, 'sentence': '专家研判认为，未来随着学校和托幼机构放寒假，流感和感染性腹泻等聚集性疫情将逐渐减少'}, {'score': 1.0, 'sentence': '国家卫健委今天（12月26日）上午举行例行发布会介绍我国冬春季常见病防控和节日健康信息，冬春季是流感、诺如病毒等所致的感染性腹泻等传染病的高发季节'}]
短语组块识别 		->		 {'主谓短语': [['教育部', '鼓励获得高中和中等职业学校毕业证的台商子女参加高职院校的分类考试招生']], '动词短语': [['鼓励', '获得高中和中等职业学校毕业证的台商子女', '参加高职院校的分类考试招生'], ['获得', '高中和中等职业学校毕业证'], ['参加', '高职院校的分类考试招生']], '名词短语': ['获得高中和中等职业学校毕业证的台商子女', '高中和中等职业学校毕业证', '中等职业学校毕业证', '职业学校毕业证', '台商子女', '高职院校的分类考试招生', '高职院校', '分类考试招生']}
实体识别 		->		 [{'end_id': 21, 'entity': '台', 'start_id': 20, 'type': 'LOC'}, {'end_id': 3, 'entity': '教育部', 'start_id': 0, 'type': 'ORG'}]
文本相似性 		->		 0.58533424
概念抽象 		->		 ['香蕉->水果->植物标本->标本->陈列品->文物和陈列品->商品']
语义联想 		->		 {'antiwords': [], 'relatedwords': ['车厘子', '凤梨', '枣', '水蜜桃', '柚子', '果', '文旦', '火龙果', '山竹', '柠檬', '犁', '羊桃', '梨子', '脐橙', '青果', '桂圆', '沙棘', '芭蕉', '红薯', '李子'], 'simwords': ['平安果', '智慧果', '栖霞', '金帅', '红富士', '国光', '富士系', '国光', '红富士', '蛇果', '柰', '苹', '香蕉苹果']}
情感分析 		->		 0.49
情感对提取 		->		 [{'entity': '铁矿石总体行情是', 'polar': '正向情感', 'score': 0.65, 'stiwd': '上涨'}, {'entity': '铁矿石进口量', 'polar': '正向情感', 'score': 0.65, 'stiwd': '上涨'}, {'entity': '铁矿石价格', 'polar': '负向情感', 'score': -0.6, 'stiwd': '走低'}]
实体属性情感提取 		->		 [{'attr': '行情', 'entity': '铁矿石总体', 'polar': '正向情感', 'score': 0.65, 'stiwd': '上涨'}, {'attr': '进口量', 'entity': '铁矿石', 'polar': '正向情感', 'score': 0.65, 'stiwd': '上涨'}, {'attr': '价格', 'entity': '铁矿石', 'polar': '负向情感', 'score': -0.6, 'stiwd': '走低'}]
主观性得分 		->		 0.6266666666666666
网页正文解析 		->		 {'news_content': '记者潘子荻\n制图樊珊珊\n【学习进行时】2019年，习近平总书记在不同场合道出很多蕴含真理力量、思想力量、智慧力量、人格力量的“金句”，直击人心，令人难忘。新华社《学习进行时》原创品牌栏目“讲习所”通过“金句”回望全年，和您一同品味。\n“我们都在努力奔跑，我们都是追梦人。”习近平总书记在2019年新年贺词中这句振奋人心的话，成为网络上刷屏的“金句”，引发亿万人共鸣。\n这句话饱含深情，让多少人心潮起伏，热泪盈眶；这句话充满力量，激励无数人星夜兼程，砥砺前行。\n流动的中国，到处是追梦人奔跑的身影。\n60余年深藏功与名的张富清为信仰而奔跑，战争年代冲锋在前，和平时期默默奉献，一生坚守初心，不改本色。\n扶贫干部黄文秀为信念而奔跑，大城市的锦绣繁华留她不住，把双脚扎进家乡泥土，把青春和热血融入脱贫攻坚洪流。\n八步沙林场“六老汉”为共同的心愿而奔跑，凭借矢志不渝的“愚公”精神，让茫茫沙漠披上了绿装。\n……\n快递小哥为千家万户而奔走，环卫工人为城市更美丽而劳作，出租车司机为人们出行更便利而忙碌……千千万万的劳动者在自己平凡的工作岗位上努力奔跑，无数的人生“小目标”汇聚成民富国强、民族振兴的“中国梦”。\n我们都是“追梦人”！\n每一个追梦的姿态，都将被定格为历史；每一滴奔跑的汗水，都将浇灌出未来。\n2019年，面对国内外风险挑战明显上升的复杂局面，宏观经济运行总体平稳，新增就业目标超额完成，中国经济巨轮始终稳稳前行。\n2019年，防范化解重大风险、精准脱贫、污染防治三大攻坚战取得关键进展。\n2019年，粤港澳大湾区建设全面推进，深圳成为中国特色社会主义先行示范区，改革开放迈出重要步伐。\n2019年，供给侧结构性改革继续深化，全面深化改革向纵深推进。\n2019年，“嫦娥四号”探测器成功登陆月球背面，北京大兴国际机场“凤凰展翅”，我国第一艘国产航母入列。\n……\n“今天，社会主义中国巍然屹立在世界东方，没有任何力量能够撼动我们伟大祖国的地位，没有任何力量能够阻挡中国人民和中华民族的前进步伐。”\n即将到来的2020年是全面建成小康社会和“十三五”规划收官之年。船到中流浪更急、人到半山路更陡，不进则退、非进不可！\n站在新的历史起点，14亿“追梦人”将以坚如磐石的信心、坚韧不拔的毅力，跑出新征程的加速度！\n习近平年度“金句”相关链接：\n【习近平年度“金句”之二】让城市留住记忆，让人们记住乡愁\n【习近平年度“金句”之三】脱贫攻坚越到最后时刻越要响鼓重锤\n【习近平年度“金句”之四】我将无我，不负人民\n点击查看专题', 'news_pubtime': '2019-12-23 08:44:50', 'news_title': '【习近平年度“金句”之一】我们都在努力奔跑，我们都是追梦人'}
网页表格解析 		->		 [{'id': 0, 'table': {'body': [['交易日期', '代码', '简称', '融资融券余额(元)'], ['2019-12-17', '688030', '山石网科', '64,984,115.6'], ['融资余额(元)', '融资买入额(元)', '融资偿还额(元)', '融资净买额(元)'], ['53,728,397', '10,081,172', '9,601,427', '479,745'], ['融券余额(元)', '融券余量(股)', '融券卖出量(股)', '融券偿还量(股)'], ['11,255,718.6', '282,807', '19,900', '19,872']], 'title': '山石网科(688030)2019-12-17融资融券信息显示，山石网科融资余额53,728,397元，融券余额11,255,718.6元，融资买入额10,081,172元，融资偿还额9,601,427元，融资净买额479,745元，融券余量282,807股，融券卖出量19,900股，融券偿还量19,872股，融资融券余额64,984,115.6元。山石网科融资融券详细信息如下表：'}}]
```

