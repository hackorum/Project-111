import statistics
from random import randint

import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("csv/data1.csv")

data = df["claps"].tolist()

population_mean = statistics.mean(data)
population_stdev = statistics.stdev(data)

print(f"Population Mean is: {population_mean}")
print(f"Standard Deviation Population is: {population_stdev}")


def takeSamples(no_of_samples):
    dataset = []
    for i in range(no_of_samples):
        random_index = randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    sample_mean = statistics.mean(dataset)
    return sample_mean


mean_list = []

for i in range(100):
    set_of_means = takeSamples(30)
    mean_list.append(set_of_means)

sample_mean = statistics.mean(mean_list)
sample_stdev = statistics.stdev(mean_list)

print(f"Sampling Mean is: {sample_mean}")
print(f"Standard Deviation is: {sample_stdev}")

df = pd.read_csv("csv/data2.csv")
data = df["claps"].tolist()

mean_of_sample1 = statistics.mean(data)
print(f"Mean of sample 1 is: {mean_of_sample1}")

zscore = (mean_of_sample1 - sample_mean) / sample_stdev
print(f"Z-Score is: {zscore}")


def plotFig():
    first_stdev_start, first_stdev_end = (
        sample_mean - sample_stdev,
        sample_mean + sample_stdev,
    )
    second_stdev_start, second_stdev_end = (
        sample_mean - (2 * sample_stdev),
        sample_mean + (2 * sample_stdev),
    )
    third_stdev_start, third_stdev_end = (
        sample_mean - (3 * sample_stdev),
        sample_mean + (3 * sample_stdev),
    )
    fig = ff.create_distplot([mean_list], ["Claps"], show_hist=False)
    fig.add_trace(go.Scatter(x=[sample_mean, sample_mean], y=[0, 0.2]))
    fig.add_trace(
        go.Scatter(
            x=[mean_of_sample1, mean_of_sample1], y=[0, 0.2], name="Mean of sample 1"
        )
    )
    fig.add_trace(go.Scatter(x=[first_stdev_start, first_stdev_start], y=[0, 0.2]))
    fig.add_trace(go.Scatter(x=[second_stdev_start, second_stdev_start], y=[0, 0.2]))
    fig.add_trace(go.Scatter(x=[third_stdev_start, third_stdev_start], y=[0, 0.2]))

    fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.2]))
    fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.2]))
    fig.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0, 0.2]))

    fig.show()


plotFig()
