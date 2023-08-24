import streamlit as st
from streamlit_modules import graph
from streamlit_modules import heatmap
from streamlit_folium import st_folium

def main():
    page_options = ["Sample of Sugar Fallin Sales Report for 2021 & 2022", "Orders Heat Map"]
    selected_page = st.sidebar.radio("Go to", page_options)

    if selected_page == "Sugar Fallin Sales Report for 2021 & 2022":
        page_1()
    elif selected_page == "Orders Heat Map":
        page_2()
#
#
def page_1():
    # st.image("data/images/vanakam_thala.gif")
    st.title("Sugar Fallin Sales Report for 2021 & 2022")
    st.write("")
    st.write("")

    # Total Revenue
    a, b = graph.revenue()
    st.header("Total Revenue:")
    st.write("**Year 2021 :** " + 'Rs.' + str(round(a)))
    st.write("**Year 2022 :** " + 'Rs.' + str(round(b)))
    st.write("")
    st.write("")

    # sales_line_chart
    st.header("Comparison of Sales for 2021 and 2022")
    fig = graph.sales_line_chart()
    st.plotly_chart(fig)
    st.write("")
    st.write("")

    # product_wise_sales_line_chart
    st.header("Product-wise Sales Comparison for 2021 and 2022")
    option1 = st.selectbox('Select a Product', ('cake', 'brookie', 'fruit_cake', 'brownie', 'cupcake',
       'cheesecake', 'bento', 'entremet', 'cookie',
       'moulded_ganache_cake', 'misc_&_combo', 'hamper', 'eclair',
       'cakepops', 'cakesicle', 'jarcake', 'macaron', 'donut', 'jam'), key=1)
    fig = graph.product_wise_sales_line_chart(option1)
    st.plotly_chart(fig)
    st.write("")
    st.write("")

    # product_wise_top_flavour_bar_chart
    st.header("Product-Flavour-wise Sales Comparison for 2021 and 2022")
    option2 = st.selectbox('Select a Product', ('cake', 'brookie', 'fruit_cake', 'brownie', 'cupcake',
       'cheesecake', 'bento', 'entremet', 'cookie',
       'moulded_ganache_cake', 'misc_&_combo', 'hamper', 'eclair',
       'cakepops', 'cakesicle', 'jarcake', 'macaron', 'donut', 'jam'), key=2)
    fig = graph.product_wise_top_flavour_bar_chart(option2)
    st.plotly_chart(fig)

    # st.image("data/images/thank_you.gif")

def page_2():
    st.title("Heat Map of Orders in Coimbatore")
    st.write("The map only has data for recorded latitudes and longitudes")
    map_ = heatmap.cbe_map()
    st_folium(map_)


if __name__ == '__main__':
    main()