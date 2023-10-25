import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from trends import plot_trends
import json 
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

if __name__ == "__main__":
    
    # Plot trends and save for backtesting
    print("Plotting trends...")
    symbol_1 = "1000LUNCUSDT"
    symbol_2 = "FXSUSDT"
    with open("1_price_list.json") as json_file:
        price_data = json.load(json_file)
        if len(price_data) > 0:
            plot_trends(symbol_1, symbol_2, price_data)

# Load the data from the CSV file
data = pd.read_csv('3_backtest_file.csv', skiprows=20, usecols=[0, 1, 2, 3], names=['Pair1', 'Pair2', 'Spread', 'ZScore'])

# Create a scatter plot for Spread
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=data.iloc[:, 0], y=data.iloc[:, 2], mode='markers',
                          name='Spread', hovertemplate='%{text}<br>Spread: %{y:.2f}'))
fig1.update_layout(xaxis=dict(title='Trading Pairs'), yaxis=dict(title='Spread'))

# Add the pair names to the hover text
fig1.data[0].update(text=[f'{pair1}<br>{pair2}' for pair1, pair2 in zip(data['Pair1'], data['Pair2'])])

# Set the x-axis labels for the Spread plot
fig1.update_xaxes(type='category', tickmode='array', tickvals=data.iloc[:, 0], ticktext=data.iloc[:, 0]+data.iloc[:, 1])

# Create a scatter plot for ZScore
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=data.iloc[:, 0], y=data.iloc[:, 3], mode='markers',
                          name='Z-Score', hovertemplate='%{text}<br>Z-Score: %{y:.2f}'))
fig2.update_layout(xaxis=dict(title='Trading Pairs'), yaxis=dict(title='Z-Score'))

# Add the pair names to the hover text
fig2.data[0].update(text=[f'{pair1}<br>{pair2}' for pair1, pair2 in zip(data['Pair1'], data['Pair2'])])

# Set the x-axis labels for the ZScore plot
fig2.update_xaxes(type='category', tickmode='array', tickvals=data.iloc[:, 0], ticktext=data.iloc[:, 0]+data.iloc[:, 1])

# Create a subplots with 2 rows and 1 column
fig = make_subplots(rows=2, cols=1)

# Add the two scatter plots to the subplots
fig.add_trace(fig1.data[0], row=1, col=1)
fig.add_trace(fig2.data[0], row=2, col=1)

# Update the layout of the subplots
fig.update_layout(height=600, width=800, title_text="Spread and Z-Score")

# Show the subplots
fig.show()
fig.write_image('4_backtest_plot.png')