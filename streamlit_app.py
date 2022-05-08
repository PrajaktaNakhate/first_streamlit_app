import streamlit
import pandas

streamlit.title('My mom\'s new healthy diner')
streamlit.header('🍽 Breakfast menu')
streamlit.text('🍛 Omega 3 and blueberry oatmeal')
streamlit.text('🌯 dosa')
streamlit.text('🥚 hard boiled free-range egg')
streamlit.header('🍌🍒 Build your own fruit smoothie 🍐🍏')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


