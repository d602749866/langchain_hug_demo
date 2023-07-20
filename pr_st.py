import streamlit as st
import langchain_help

st.title("饭店名生成器")

cuisine = st.sidebar.selectbox("选择一个菜系", ("粤菜", "川菜", "鲁菜", "湘菜"))



if  cuisine:
    response = langchain_help.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split('，')
    st.write("****菜单****")
    for itme in menu_items:
        st.write("-", itme)