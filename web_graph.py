from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

def inc_dec(c, o):
    if c > o:
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = "Equal"
    return value


start_time = datetime.datetime(2015,3,1)
end_time = datetime.datetime(2019,9,10)

df = data.DataReader(name = "AAPL", data_source = "yahoo", start = start_time , end = end_time)

date_increase = df.index[df.Close > df.Open]
date_decrease = df.index[df.Close < df.Open]

df["Status"] = [inc_dec(c,o) for c, o in zip(df.Close, df.Open)]
df["Middle"] = (df.Open + df.Close)/2
df["Height"] = abs(df.Close - df.Open)

p = figure(x_axis_type = 'datetime', width = 1000, height = 300, title = "Candlestick Chart")
p.grid.grid_line_alpha = 0

hours_12 = 12*60*60*100

p.segment(df.index, df.High, df.index, df.Low, color = "black")

p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"], hours_12*10, df.Height[df.Status == "Increase"],
fill_color = "#7CFC00", line_color = "black")

p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"], hours_12*10, df.Height[df.Status == "Decrease"],
fill_color = "#FF3333", line_color = "black")

script1, div1 = components(p)

cdn_js = CDN.js_files
cdn_css = CDN.css_files

# output_file("CS.html")
# show(p) ---- only to output localy
