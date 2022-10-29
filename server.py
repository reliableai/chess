from numpy import place
import streamlit as st
import chess
import base64


st.title("ML for Everybody")

st.write("Chess Board")
placeholder =  None

# img = board._repr_svg_()
def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    placeholder = st.write(html, unsafe_allow_html=True)
    return placeholder


def handle_move():
    global placeholder
    placeholder.empty()
    board.push(chess.Move.from_uci(move))
    render_svg(board._repr_svg_())


board = chess.Board()
new = True
if new:
    placeolder = render_svg(board._repr_svg_())
    new = False

# placeholder= st.image('loading4.gif')
# #call mode
# placeholder = st.empty()


# st.write("Moves")
move = st.text_input("Enter move")
st.button('Make my move',  on_click=handle_move)


# img = board._repr_svg_()
# render_svg(img)

