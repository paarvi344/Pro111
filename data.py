import csv
from cv2 import mean 
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("medium_article.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
standard_deviation = statistics.stdev(data)
print("Mean of the sampling:",population_mean)
print("Standard Deviation: " ,standard_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range (0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(0,30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

def show_fig(mean_list ):
    df =  mean_list 
    fig = ff.create_distplot([df],["reading score"],show_hist = False)
    fig.show()

mean_list = []
for i in range(0,1000):
       set_of_means= random_set_of_mean(100)
       mean_list.append(set_of_means)


#calculating mean and standard_deviation of the sampling distribution.
std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ", std_deviation)


first_standard_deviation_start , first_standard_deviation_end = population_mean - standard_deviation , population_mean + standard_deviation
second_standard_deviation_start , second_standard_deviation_end = population_mean -(2*standard_deviation), population_mean + (2*standard_deviation)
third_standard_deviation_start , third_standard_deviation_end = population_mean - (3*standard_deviation) , population_mean + (3*standard_deviation)

print("Standard deviation 1:", first_standard_deviation_start,first_standard_deviation_end)
print("Standard deviation 2:", second_standard_deviation_start,second_standard_deviation_end)
print("Standard deviation 3:", third_standard_deviation_start,third_standard_deviation_end)

df = pd.read_csv("sample2.csv")
data  = df["reading_time"].tolist()
mean_of_sample2 = statistics.mean(data)
print("Mean of sample 2 : ",mean_of_sample2)
fig = ff.create_distplot(df[mean_list],["reading_time"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], name = "Mean "))
fig.add_trace(go.Scatter(x = [mean_of_sample2,mean_of_sample2], y = [0,0.17], name = "Mean of the sample: "))
fig.add_trace(go.Scatter(x = [first_standard_deviation_start , first_standard_deviation_end], y = [0,0.17], name = "Mean "))
fig.add_trace(go.Scatter(x = [second_standard_deviation_start ,second_standard_deviation_end], y = [0,0.17], name = "Mean "))
fig.add_trace(go.Scatter(x = [third_standard_deviation_start , third_standard_deviation_end], y = [0,0.17], name = "Mean "))
fig.show()

z_score = (mean_of_sample2  - mean)/standard_deviation
print("Z SCORE = ", z_score)








