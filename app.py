import streamlit as st 
import random 
from collections import Counter 
 
st.set_page_config(page_title="Random A/B Generator", 
layout="centered") 
 
st.title("
🎲
 Random A/B Generator") 
st.write("Generate 1,000 random 'A' and 'B' values and count them in 
one click.") 
 
if st.button("Generate & Count", type="primary"): 
    items = random.choices(['A', 'B'], k=1000) 
    counts = Counter(items) 
     
    count_a = counts.get('A', 0) 
    count_b = counts.get('B', 0) 
     
    col1, col2 = st.columns(2) 
col1.metric(label="Total 'A'", value=count_a, 
delta=f"{(count_a/1000)*100:.1f}%") 
col2.metric(label="Total 'B'", value=count_b, 
delta=f"{(count_b/1000)*100:.1f}%") 
st.bar_chart({"A": count_a, "B": count_b})
