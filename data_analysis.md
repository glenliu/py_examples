# Data analysis process
[Reference](https://mp.weixin.qq.com/s?__biz=MzAxMjUyNDQ5OA==&mid=2653556933&idx=1&sn=283e9a04de0734743c90898803b72495&chksm=806e3e78b719b76e6ede9ec6ac7a7376e3255191ad3ffc180d4c126ed1722a635589e566fde7&mpshare=1&scene=1&srcid=09135t9mN8icnfz3dQsRB6DH&pass_ticket=fNZEAa0VpZ0hpDCvIn0ITCA%2B58I0zv%2Be9yfSsGCpQ1jNxx9Db30pZzRuDGuSVAtq#rd)

## Index
- [Data collecting](#Data--collecting)

 
- [Public data sources](#Public--data--sources)

 
- [Crawlers](#Crawlers)

 
- [Data Storage and Load](#Data--Storage--and--Load)

- [Storage](#Storage)

- [Load](#Load)

- [Pre-process & Mangling](#[Pre-process--Mangling)

- [Modeling & analysis](#Modeling--analysis)

- [Statistics basics](#Statistics--basics)

- [Metris](#Metrics)

- [Test](#Test)

- [Common regression](#)

- [Basic classifying, categorising](#Basic--classifying--categorising)

- [Feature Engineering](#Feature--Engineering)

- [Data Visualization](#Data--Visualization)

- [Put into Practice](#Put--into--Practice)

## Data Collecting

### Public data sources
UCI：加州大学欧文分校开放的经典数据集，被很多数据挖掘实验室采用。

http://archive.ics.uci.edu/ml/datasets.html



国家数据：数据来源于中国国家统计局，包含了我国经济民生等多个方面的数据。

http://data.stats.gov.cn/



CEIC：超过128个国家的经济数据，能精确查找GDP、进出口零售，销售等深度数据。

http://www.ceicdata.com/zh-hans



中国统计信息网：国家统计局官方网站，汇集了国民经济和社会发展统计信息。

http://www.tjcn.org/


### Crawlers
比如你可以通过爬虫获取招聘网站某一职位的招聘信息，爬取租房网站上某城市的租房信息，爬取豆瓣评分评分最高的电影列表，获取知乎点赞排行、网易云音乐评论排行列表。基于互联网爬取的数据，你可以对某个行业、某种人群进行分析。



常用的的电商网站、问答网站、二手交易网站、婚恋网站、招聘网站等，都可以爬到非常有价值的数据。

## Data Storage and Load

### Storage

### Load

## Pre-process & Mangling
很多时候我们拿到的数据是不干净的，数据的重复、缺失、异常值等等，这时候就需要进行数据的清洗，把这些影响分析的数据处理好，才能获得更加精确地分析结果。



比如缺失值，我们是直接去掉这条数据，还是用临近的值去补全，比如异常的值，如何设置合理数据区间进行取舍……



对于数据预处理，学会 pandas （Python包）的用法，应对一般的数据清洗就完全没问题了。需要掌握的知识点如下：


- 选择：数据访问（标签、特定值、布尔索引等）

- 缺失值处理：对缺失数据行进行删除或填充

- 重复值处理：重复值的判断与删除

- 异常值处理：清除不必要的空格和极端、异常数据

- 相关操作：描述性统计、Apply、直方图等

- 合并：符合各种逻辑关系的合并操作

- 分组：数据划分、分别执行函数、数据重组

- Reshaping：快速生成数据透视表

## Modeling & analysis

### Statistics basics
数据整体分布是怎样的？什么是总体和样本？中位数、众数、均值、方差等基本的统计量如何应用？如何在不同的场景中做假设检验？数据分析方法大多源于统计学的概念，所以统计学的知识也是必不可少的。


### Metrics
需要掌握的知识点如下：



- 基本统计量：均值、中位数、众数、百分位数、极值等

- 其他描述性统计量：偏度、方差、标准差、显著性等

- 其他统计知识：总体和样本、参数和统计量、ErrorBar

- 概率分布与假设检验：各种分布、假设检验流程

- 其他概率论知识：条件概率、贝叶斯等



有了统计学的基本知识，你就可以用这些统计量做基本的分析了。通过可视化的方式来描述数据的指标，其实可以得出很多结论了：比如排名前100的是哪些，平均水平是怎样的，近几年的变化趋势如何……



你可以使用 Seaborn、matplotlib 等（python包）做一些可视化的分析，通过各种可视化统计图，并得出具有指导意义的结果。
### Test

### Common regression


比如掌握回归分析的方法，通过线性回归和逻辑回归，其实你就可以对大多数的数据进行回归分析，并得出相对精确地结论。这部分需要掌握的知识点如下：



- 回归分析：线性回归、逻辑回归





在数据分析的这个阶段，重点了解回归分析的方法，大多数的问题可以得以解决，利用描述性的统计分析和回归分析，你完全可以得到一个不错的分析结论。




### Basic classifying, categorising

- 基本的分类算法：决策树、随机森林、朴素贝叶斯……

- 基本的聚类算法：k-means……

### Feature engineering

- 特征工程基础：如何用特征选择优化模型

Python 数据分析包：scipy、numpy、scikit-learn等

然后你会知道面对不同类型的问题的时候更适合用哪种算法模型，对于模型的优化，你需要去学习如何通过特征提取、参数调节来提升预测的精度。这就有点数据挖掘和机器学习的味道了，其实一个好的数据分析师，应该算是一个初级的数据挖掘工程师了。

## Data Visualization

## Put into Practice


到这个时候，你就已经具备了数据分析的基本能力了。但是还要根据不同的案例、不同的业务场景进行实战，练习解决实际问题的能力。



上面提到的公开数据集，可以找一些自己感兴趣的方向的数据，尝试从不同的角度来分析，看看能够得到哪些有价值的结论。



你也可以从生活、工作中去发现一些可用于分析的问题，比如上面说到的电商、招聘、社交等平台等数据中都有着很多可以挖掘的问题。



开始的时候，你可能考虑的问题不是很周全，但随着你经验的积累，慢慢就会找到分析的方向，有哪些一般分析的维度，比如Top榜单、平均水平、区域分布、同比环比、相关性分析、未来趋势预测等等。随着经验的增加，你会有一些自己对于数据的感觉，这就是我们通常说的数据思维了。





零基础学习数据分析，坑确实比较多，总结如下：

1.环境配置，工具安装、环境变量，对小白太不友好；

2.缺少合理的学习路径，上来 Python、HTML 各种学，极其容易放弃；

3.Python有很多包、框架可以选择，不知道哪个更友好；

4.遇到问题找不到解决办法，学习停滞不前；

5.网上的资料非常零散，而且对小白不友好，很多看起来云里雾里；

6.懂得技巧，但面对具体问题无法系统思考和分析；

……………………