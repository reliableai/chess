
import streamlit as st

if 'i' not in st.session_state:
    st.session_state['i'] = 0

i = 0
def handle_move():
    st.session_state['i'] += 1  
    st.write('in handle move:' + str(st.session_state['i'])) 
    # + str(st.session_state['moves']) + str(st.session_state['refresh_counter']))

# i+=1 

# st.write(i)
# st.write(st.session_state['i'])
st.button('Make my move',  on_click = handle_move)
