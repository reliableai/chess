from numpy import place
import streamlit as st
import chess
import base64
from game import play_logic as pl

# st.title("ML for Everybody")
# st.write("Chess Board")

#set page title
st.set_page_config(page_title="Chess Board", page_icon="♟", layout="wide", initial_sidebar_state="auto")

if 'board' not in st.session_state:
    st.session_state['board'] = chess.Board()

if 'board_container' not in st.session_state:
    st.session_state['board_container'] = st.empty()

if 'input_container' not in st.session_state:
    st.session_state['input_container'] = st.empty()

if 'refresh_counter' not in st.session_state:
    st.session_state['refresh_counter'] = 0

if 'moves' not in st.session_state:
    st.session_state['moves'] = []

if 'move' not in st.session_state:
    st.session_state['move'] = ''

if "suggested_move" not in st.session_state:
    st.session_state['suggested_move'] = 'e2e4'

moves = st.session_state['moves']
move = st.session_state['move']
board_container = st.session_state['board_container']
input_container = st.session_state['input_container']
suggested_move = st.session_state['suggested_move']
# st.session_state['refresh_counter'] += 1

# img = board._repr_svg_()
def render_svg(svg, board_container):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.session_state['board_container'].write(html, unsafe_allow_html=True)



def handle_move(move):
    # st.session_state['board_container'] = st.empty()
    #make move lowercase
    move = move.lower()
    moves.append(move)

    # st.write('in handle move:' + str(moves) + value + str(st.session_state['refresh_counter']))
    # st.write('in handle move:' + str(moves) + value + str(st.session_state['refresh_counter']))

    
    if st.session_state['board'].is_legal(chess.Move.from_uci(move)):
        # st.write(st.session_state['move'] + " is LEGAL")
        st.session_state['board'].push(chess.Move.from_uci(move))
        suggested_move = pl.pick_random_move(st.session_state['board']).uci()
        st.session_state['suggested_move'] = suggested_move
        # st.session_state['board'].empty()
        # render_svg(st.session_state['board']._repr_svg_(), st.session_state['board_container'])
    else:
        st.write("Illegal Move")
        # st.session_state['board_container'].write("Illegal Move")
    
    render_svg(st.session_state['board']._repr_svg_(), st.session_state['board_container'])


def initial_setup():
    render_svg(st.session_state['board']._repr_svg_(), st.session_state['board_container'])
    
def handle_apply_suggested_move():
    st.write("applying Suggested move")

    handle_move (st.session_state['suggested_move'])
    # st.session_state['board'].push(chess.Move.from_uci(st.session_state['suggested_move']))
    # render_svg(st.session_state['board']._repr_svg_(), st.session_state['board_container'])
    st.write("Suggested move applied")

if "initial_setup" not in st.session_state:
    # st.write("initial setup")
    st.session_state['initial_setup'] = True
    initial_setup()
    move = 'e2e4'
    st.session_state['initial_setup'] = False


# board = st.session_state['board']
# board_container = st.session_state['board_container']
# refresh_counter = st.session_state['refresh_counter']
# moves = st.session_state['moves']
# move = st.session_state['move']

# st.write(str(st.session_state['refresh_counter']) + ', From main' + str(st.session_state['moves']))


# def handle_move_change():
#     handle_move()
#     render_svg(st.session_state['board']._repr_svg_(), st.session_state['board_container'])
#     st.session_state['suggested_move'] = pl.pick_random_move(st.session_state['board']).uci()

# def handle_move_click():
#     st.write('handle_move_click' + st.session_state['move']) 
#     st.write('handle_move_click' ) 
#     st.write('handle_move_click: ' + st.session_state['move']) 
#     # st.write (st.session_state['move_input'].value)

# st.write("Moves" + str(moves))
# st.write("Suggested Move: " +  st.session_state['suggested_move'])
inct = st.empty()
st.write("x")
entered_move = input_container.text_input("Enter move: ", value = '', key = 'move')


if entered_move != st.session_state['move']:
    None

if entered_move:
    st.session_state['refresh_counter'] += 1
    st.write('refresh: ' + str(st.session_state['refresh_counter']) + ', From main' + str(st.session_state['moves']))
    handle_move(entered_move)
    # render_svg(st.session_state['board']._repr_svg_(), st.session_state['board_container'])

    # st.write("Suggested Move: " + suggested_move)
    entered_move = None
    move = ''

if suggested_move:
    st.button("Apply Suggested Move: " + suggested_move, on_click = handle_apply_suggested_move, key = 'apply_suggested_move')


