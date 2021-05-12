# 一行代码，轻松绘制动态关系网络图（`Jaal` 库）

## What is Jaal ?

`Jaal` 是基于`Dash`和`Visdcc`构建的交互式的`Python`网络图绘制库，导入数据后，只需要一行代码，便可绘制精美的网络图。与此同时，`Jaal`也提供了一些对网络图进行修改优化的操作，如：搜索、过滤、给节点（边）上色等。而且，所有操作只需简单的2-3行代码。

## 安装

`Jaal`依赖于`python`包：`Dash, dash_bootstrap_components, visdcc, pandas`等，安装也非常简单，只需（依赖包会自动安装）：

```python
pip install jaal
```

## 小试牛刀

我们知道，网络图本质上是由节点、边组成的，其他特征都是在节点和边的基础上建立的。如节点有不同的属性（如，类别，量值，重要性等），这些可以通过节点的颜色、大小、形状来进行区分，同样的边也是如此，另外边还有方向，环向等。`Jaal`包也是据此基本逻辑编写的，画图之前，我们需要准备两个文件（这里拿`Jaal`包自带数据--《权利的游戏》人物关系数据进行演示）：

```python
# 导入依赖包
from jaal import Jaal
from jaal.datasets import load_got
# 加载Jaal包自带数据
edge_df, node_df = load_got()
```

1. ### 包含边关系数据框

   ```python
   edge_df.head(10) #查看前10行数据
   ```

   | from                            | to                 | weight | strength |
   | ------------------------------- | ------------------ | ------ | -------- |
   | Aemon-Targaryen-(Maester-Aemon) | Jeor-Mormont       | 13     | medium   |
   | Aemon-Targaryen-(Maester-Aemon) | Jon-Snow           | 34     | medium   |
   | Aerys-II-Targaryen              | Robert-Baratheon   | 12     | medium   |
   | Aggo                            | Daenerys-Targaryen | 11     | medium   |
   | Alliser-Thorne                  | Jon-Snow           | 32     | medium   |
   | Alyn                            | Eddard-Stark       | 11     | medium   |
   | Arya-Stark                      | Bran-Stark         | 14     | medium   |
   | Arya-Stark                      | Cersei-Lannister   | 12     | medium   |
   | Arya-Stark                      | Eddard-Stark       | 30     | medium   |
   | Arya-Stark                      | Joffrey-Baratheon  | 39     | medium   |

   我们可以看到，`edge_df`包含`4`列：`from`是起点，`to`是终点，`weight`是两节点的权重值，`strength`是关系强弱程度（可看作是分类属性）。

2. ### 包含节点关系数据框

   ```python
   node_df.head(10) 
   ```

   | id                | gender |
   | ----------------- | ------ |
   | Illyrio-Mopatis   | male   |
   | Jory-Cassel       | male   |
   | Viserys-Targaryen | male   |
   | Mirri-Maz-Duur    | female |
   | Jhogo             | male   |
   | Halder            | male   |
   | Jeor-Mormont      | male   |
   | Robert-Baratheon  | male   |
   | Jaremy-Rykker     | male   |
   | Robb-Stark        | male   |

   `node_df`包含`2`列：`id`是节点的名字，`gender`是性别（也可是节点的其他属性，在生物领域也可为基因、蛋白的分类等）

介绍完数据格式后，我们开始绘图：

```python
Jaal(edge_df, node_df).plot()  #一行代码画图
```

运行代码后，会生成一个本地服务链接（默认为http://127.0.0.1:8050/ ），点击链接，就会弹出浏览器网页：![img](https://github.com/imohitmayank/jaal/raw/main/jaal/assest/dashboard.png)

那么，初版的网络图就做成了。

## 功能

为了美化网络图，该包也提供一些功能：

**设置面板**	大家可能也注意到了弹出的画图网页的左侧的控制面板了，对的，它目前有三个方面的功能块：

**搜索**	可以高亮搜索到的节点

**过滤**	支持`pandas`的`query`语法

**上色**	基于类别，对节点、边上色。 默认最多支持`20`个类别，即节点、边数据允许有`20`种属性，对于平时我们使用足够了。但如果不够，则需要修改源代码了（增加一些颜色接口），小伙伴后面有需要，可联系我。

## 演示

1. ### 搜索功能

   我们可以在`Search`栏下，输入需要查看的特定节点名称（`id`），这里输入`“arya”`，它支持字符逐一搜索高亮：

   <img src="https://github.com/imohitmayank/jaal/raw/main/jaal/assest/jaal_search.gif" style="zoom: 100%" />

   

2. ### 过滤功能

   在`Filter`栏下有两个窗口，分别对节点和边进行控制，支持`pandas`语法，这里在过滤节点窗口输入`gender=='male'`，可以看到网络图只保留`male`的节点；另外，在过滤边窗口输入`weight>20`，则只会保留`weight>20`的边：

   <img src="https://github.com/imohitmayank/jaal/raw/main/jaal/assest/jaal_filter.gif" style="zoom: 100%" />

3. ### 修改颜色

   在`Color`栏下也有对应的两个窗口，对应节点和边的颜色修改，这里节点属性列只有`gender`，根据`gender`进行分类上色（如果想对特殊点上色，可以在原始数据中修改属性列的内容，就可以了）；对边的上色也是一样的：

   <img src="https://github.com/imohitmayank/jaal/raw/main/jaal/assest/jaal_color.gif" style="zoom: 100%" />

以上就完成了，对网络图修改美化，比`cytoscape`等软件操作简单，有么有`~.~`

## 更上一层楼

有伙伴就问了，我想对增加边标签、边的方向，又该怎么弄了？

这里就需要修改一下代码了，也很简单：

### **加边标签**：

给边的数据框加一列就好了，注意的是，该列需要是字符串`（string）`的数据类型。

```python
# add edge labels
edge_df.loc[:, 'label'] = edge_df.loc[:, 'weight'].astype(str)
```

### 加方向：

只需在`Jaal`  `plot`函数中修改`directed`参数为`True`即可：

```python
Jaal(edge_df, node_df).plot(directed=True)
```

其他更多修改，就稍微需要一些编程能力了，我们可以对源代码进行修改。

## 最后说一点

如果小伙伴想用自己的数据进行网络图绘制该怎么办呢？可以先按前面介绍的数据格式准备节点和边的信息文件，值得提一点的是，我们是可以在属性列（`gender`这种）后面增加一些属性内容，可以达到对节点和边的更多修饰与美化。当然，`Jaal`也有些许缺点，如没有自定义颜色选择窗口、结果文件保存格式单一等，不过这些都可优化源代码解决的。总体来说，还是很不错的工具，关键是操作简单、代码少，动图还比较美观。所以，感兴趣的小伙伴们，可以快快探索起来吧~！





