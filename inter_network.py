
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         inter_network
# Description:  
# Author:       Duan xiaoqian
# Date:         2021/5/11
# -------------------------------------------------------------------------------

from jaal import Jaal
from jaal.datasets import load_got
# load the data
edge_df, node_df = load_got()
# init Jaal and run server
Jaal(edge_df, node_df).plot()

edge_df.head(10)

node_df.head(10)


