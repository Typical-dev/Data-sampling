import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go
df = pd.read_csv("average.csv")
data = df["average"].tolist()
population_mean = statistics.mean(data)
population_SD = statistics.stdev(data)
#print(f"Mean-sample: {mean}, Standard-deviation: {stdev}")
print(f"mean: {population_mean}, SD: {population_SD}")
#fig = ff.create_distplot([data],["average"], show_hist = False)
#fig.add_trace(go.Scatter(x = [population_mean,population_mean], y = [0,1.25], mode = "lines", name = "MEAN"))
#fig.show()
def random_mean(counter):
    data_set = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        data_set.append(value)
    mean = statistics.mean(data_set)
    stdev = statistics.stdev(data_set)
    return(mean)
def show_figure(mean_list):
    df = mean_list
    fig = ff.create_distplot([data],["average"], show_hist = False)
    fig.show()
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_mean(100)
        mean_list.append(set_of_means)
    sample_mean = statistics.mean(mean_list)
    sample_SD = statistics.stdev(mean_list)
    print(f"Sample-Mean: {sample_mean}, Sample-SD: {sample_SD}")
    #print(mean_list)
    show_figure(mean_list)
setup()

