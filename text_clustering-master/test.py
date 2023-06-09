from pprint import pprint
from paddlenlp import Taskflow

# -*- coding:utf-8 -*-

schema = ['位置', '街道', '机构', '公司', '小区', '地名', '商场', '道路地区', '位置信息']  # Define the schema for entity extraction
ie = Taskflow('information_extraction', schema=schema, model='uie-base')
sentence1 = "来话人2020年12月28日，在高新区益州大道中段1918号南城2栋负1楼（中影100都市影城）支付73.8" \
           "元购两张电影票，但今其去该影院，影院负责人表示该厅已经满了，为其换其他厅，但其他厅也是无位，联系商家协商未得到解决，其不满，请处理。 "
sentence2 = '尊敬的市长：我是吴晓霞，是一名初中英语老师。我投诉武警警官学院电子技术系教师周梓鑫。1、她因为个人利益，这半年来不断对我进行诽谤、恐吓、骚扰并索要巨额赔偿，对我身心造成了极大的创伤；2' \
            '、她还骚扰我工作的学校和诸多同事，严重影响了学校和同事们的正常教育教学工作；3、她的上述行为已经违反了一名教师的基本道德，请贵校彻查她的师德师风问题。我于2020年4月租住了周梓鑫位于高新区科华南路316号3' \
            '栋1单元29层2901号的房子，房子应于2021年7月25日正式租赁到期。在合约到期前的6月2' \
            '日，我母亲从租房窗户不幸堕楼身亡，在租赁到期依约退房之际，周以我母亲坠楼造成房屋不好出租出售为由拒不收房，要求我再续租2年，经多次沟通后她决定减到1年，最后又要我自己提出赔偿方式由她决定是否接受。我提出给予4' \
            '个月的房租总计18800即实际多付3个月的房租+不退租房押金的方式解决，但周的丈夫（孔祥瑞）予以拒绝。我和孩子于2021年6月8' \
            '日搬离所租房屋，在此之前多次告知收房，但均被拒。我在交清了水、电、物管费等费用后，拍了视频和照片给她丈夫孔祥瑞，孔通知物管阻止我搬出由本人添置的家具，我于房屋租赁合同期第二天，即2021年7月26' \
            '日，在四川省成都市高新公证处办理了终止租赁合同的公证书，正式将房屋完好无损的退还给孔祥瑞、周梓鑫。可没想到，周梓鑫自9' \
            '月开始先后给我所在学校的领导和党组织写信，要求我补偿房屋损失费，扬言若学校领导不解决或无法解决，将在建党百年之际继续向上一级党组织反映。的确他们也这样做了。从9'
pprint(ie(sentence2))  # Better print results using pprint
