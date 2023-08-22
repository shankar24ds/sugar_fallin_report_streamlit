import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def revenue():
    df = pd.read_csv('data/raw/sales_enriched2.csv')
    # 2021
    value1 = df[df['Year']==2021]['price'].sum()
    # 2022
    value2 = df[df['Year']==2022]['price'].sum()
    return value1, value2

def sales_line_chart():
    df = pd.read_csv('data/raw/sales_enriched2.csv')
    # Define a dictionary to map month numbers to month names
    month_map = {
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec'
    }

    # Map the month numbers to month names
    df['month_name'] = df['month_'].map(month_map)

    # Define the correct order of month names
    ordered_month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Group the data by month and calculate the total sales for each month and year
    grouped_data = df.groupby(['Year', 'month_'])['price'].sum().reset_index()

    # Create a line chart using Plotly Express
    fig = px.line(grouped_data, x='month_', y='price', color='Year',
                labels={'month_': 'Month', 'price': 'Total Sales'}
                )

    # Set the ordered category for x-axis month names
    fig.update_xaxes(categoryorder='array', categoryarray=ordered_month_names)

    # Set custom tick values and labels for x-axis
    tickvals = list(range(1, 13))  # Month numbers
    ticktext = ordered_month_names  # Corresponding month names
    fig.update_xaxes(tickvals=tickvals, ticktext=ticktext)

    # Set custom tick values and labels for y-axis
    y_tickvals = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]  # Custom tick values
    y_ticktext = ['0', '10k', '20k', '30k', '40k', '50k', '60k', '70k', '80k', '90k', '100k']  # Corresponding tick labels
    fig.update_yaxes(tickvals=y_tickvals, ticktext=y_ticktext)

    # Set the y-axis range
    fig.update_yaxes(rangemode='normal', range=[0, 100000])

    # Increase the height of the graph
    fig.update_layout(width=800, height=600)  # You can adjust the height as needed


    # Show the plot
    return fig

def product_wise_sales_line_chart(prod):
    df = pd.read_csv('data/raw/sales_enriched2.csv')
    if prod == 'cake':
        # Define a dictionary to map month numbers to month names
        month_map = {
            1: 'Jan',
            2: 'Feb',
            3: 'Mar',
            4: 'Apr',
            5: 'May',
            6: 'Jun',
            7: 'Jul',
            8: 'Aug',
            9: 'Sep',
            10: 'Oct',
            11: 'Nov',
            12: 'Dec'
        }

        # Map the month numbers to month names
        df = df[df['product']==prod].copy()
        df['month_name'] = df['month_'].map(month_map)

        # Define the correct order of month names
        ordered_month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        # Group the data by month and calculate the total sales for each month and year
        grouped_data = df.groupby(['Year', 'month_'])['price'].sum().reset_index()

        
        # Create a line chart using Plotly Express
        fig = px.line(grouped_data, x='month_', y='price', color='Year',
                    labels={'month_': 'Month', 'price': 'Total Sales'}
                    )

        # Set the ordered category for x-axis month names
        fig.update_xaxes(categoryorder='array', categoryarray=ordered_month_names)

        # Set custom tick values and labels for x-axis
        tickvals = list(range(1, 13))  # Month numbers
        ticktext = ordered_month_names  # Corresponding month names
        fig.update_xaxes(tickvals=tickvals, ticktext=ticktext)

        # Set custom tick values and labels for y-axis
        y_tickvals = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000]  # Custom tick values
        y_ticktext = ['0', '10k', '20k', '30k', '40k', '50k', '60k', '70k', '80k']  # Corresponding tick labels
        fig.update_yaxes(tickvals=y_tickvals, ticktext=y_ticktext)

        # Set the y-axis range
        fig.update_yaxes(rangemode='normal', range=[0, 80000])

        # Increase the height of the graph
        fig.update_layout(width=800, height=600)  # You can adjust the height as needed


        # Show the plot
        return fig
    else:
        # Define a dictionary to map month numbers to month names
        month_map = {
            1: 'Jan',
            2: 'Feb',
            3: 'Mar',
            4: 'Apr',
            5: 'May',
            6: 'Jun',
            7: 'Jul',
            8: 'Aug',
            9: 'Sep',
            10: 'Oct',
            11: 'Nov',
            12: 'Dec'
        }

        # Map the month numbers to month names
        df = df[df['product']==prod].copy()
        df['month_name'] = df['month_'].map(month_map)

        # Define the correct order of month names
        ordered_month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        # Group the data by month and calculate the total sales for each month and year
        grouped_data = df.groupby(['Year', 'month_'])['price'].sum().reset_index()

        
        # Create a line chart using Plotly Express
        fig = px.line(grouped_data, x='month_', y='price', color='Year',
                    labels={'month_': 'Month', 'price': 'Total Sales'}
                    )

        # Set the ordered category for x-axis month names
        fig.update_xaxes(categoryorder='array', categoryarray=ordered_month_names)

        # Set custom tick values and labels for x-axis
        tickvals = list(range(1, 13))  # Month numbers
        ticktext = ordered_month_names  # Corresponding month names
        fig.update_xaxes(tickvals=tickvals, ticktext=ticktext)

        # Set custom tick values and labels for y-axis
        y_tickvals = [0, 10000]  # Custom tick values
        y_ticktext = ['0', '10k']  # Corresponding tick labels
        fig.update_yaxes(tickvals=y_tickvals, ticktext=y_ticktext)

        # Set the y-axis range
        fig.update_yaxes(rangemode='normal', range=[0, 10000])

        # Increase the height of the graph
        fig.update_layout(width=800, height=600)  # You can adjust the height as needed


        # Show the plot
        return fig
    
def product_wise_top_flavour_bar_chart(prod):
    df = pd.read_csv('data/raw/sales_enriched2.csv')
    df = df[df['product']==prod].copy()
    grouped_data = df.groupby(['Year', 'flavour'])['price'].sum().reset_index()

    
    df = px.data.tips()
    fig = px.histogram(grouped_data, x="flavour", y="price",
                color='Year', barmode='group',
                width = 800,
                height=600,
                labels={'flavour': 'Flavour', 'price': 'flavour sales'}
                    )
                
    return fig