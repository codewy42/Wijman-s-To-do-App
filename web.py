import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Wijmans To-Do App")
st.subheader("Welkom bij mijn eerste app!")
st.write("Een geheugensteuntje, wat doe jij vandaag?")


for todo in todos:
    st.checkbox(todo)

st.text_input(label= "", placeholder="Vul hier je nieuwe to-do in:",
              on_change=add_todo, key='new_todo')

