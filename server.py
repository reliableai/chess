import streamlit as st
import chess
import base64

# base64.b64decode('c3RyZWFtbGl0LmFkZC5zdHJpbmcocmVxdWlyZSgnY2hlc3MnKSk=')






st.title("ML for Everybody")

st.write("Chess Board")


board = chess.Board()


img = board._repr_svg_() #chess.svg.board( board)._repr_svg_() 
def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)

render_svg(img)
