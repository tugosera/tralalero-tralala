# tasks = []


#def add_task(task):
#    return tasks.append(task)

#def main():
#    global task
    
#    print("1 - lisa ülesanne \n 2 - kustutta ülesanne \n 3 - ülevaadata ülesanded")
#    userInput = input("Mida sa tahad? \n")
#    if userInput == "1":
#        task = add_task(input("sisesta ülesande: "))
#    elif userInput == "2":
#        pass
#    elif userInput == "3":
#        pass
#    else:
#        print("Sa sisestasid midafi vale")

import streamlit as st

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("Todo List")

def add_task():
    task = st.text_input("Sisesta uus ülesanne", key="new_task_input")
    if st.button("Lisa"):
        if task.strip():
            st.session_state.tasks.append({"text": task, "done": False})
            st.rerun()
        else:
            st.warning("Sisesta mitte tühi ülesanne")

add_task()

st.subheader("Ülesannete nimekiri")

def show_tasks():
    if not st.session_state.tasks:
        st.info("Ei ole ülesandeid")
        return

    for index, task in enumerate(st.session_state.tasks):
        cols = st.columns([0.05, 0.90, 0.05])
        with cols[0]:
            task["done"] = st.checkbox("", value=task["done"], key=f"done_{index}")
        with cols[1]:
            if task["done"] == True:
                text = "----------------",task["text"],"----------------"
            else:
                text = task = task["text"]
            st.markdown(text)
        with cols[2]:
            if st.button("Kustuta", key=f"delete_{index}"):
                st.session_state.tasks.pop(index)
                st.rerun()

show_tasks()