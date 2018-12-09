from data import dataset
from task1 import *

import plotly
import plotly.graph_objs as go


#Вивести кругову діаграму: якого товару на яку суму продано.
data= dict()
for name_auto in list (dataset.keys()):

    for race, race_list in (dataset[name_auto]).items():

        if race in data:

            data[race] += sum(race_list)

        else:

            data[race] = sum(race_list)
print(data)


diagram =go.Pie((labels=list(data.keys()), values=list( data.values())))

plotly.offline.plot([diagram], filename = "auto.html")