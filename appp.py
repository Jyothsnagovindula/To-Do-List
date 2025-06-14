import streamlit as st

# App title
st.set_page_config(page_title="To-Do List", layout="centered")
st.title("📝 To-Do List Manager")

# Dark Mode toggle
dark_mode = st.toggle("🌗 Dark Mode", value=False)

# Apply dark mode style
if dark_mode:
    st.markdown(
        """
        <style>
        body, .stApp {
            background-color: #1e1e1e;
            color: white;
        }
        .stTextInput>div>div>input {
            color: white;
            background-color: #2b2b2b;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Initialize session state to store tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input box for new task
new_task = st.text_input("Add a new task:")

# Button to add task
if st.button("Add Task"):
    if new_task.strip() != "":
        st.session_state.tasks.append({"task": new_task.strip(), "done": False})
        st.success("Task added successfully!")
    else:
        st.warning("Task cannot be empty.")

st.markdown("---")

# Display tasks
if st.session_state.tasks:
    st.subheader("Your Tasks:")
    for i, task in enumerate(st.session_state.tasks):
        cols = st.columns([6, 1, 1])
        # Task text
        if task["done"]:
            cols[0].markdown(f"✅ ~~{task['task']}~~")
        else:
            cols[0].markdown(f"🔲 {task['task']}")

        # Mark as done
        if cols[1].button("✔️", key=f"done_{i}"):
            st.session_state.tasks[i]["done"] = True

        # Delete task
        if cols[2].button("🗑️", key=f"delete_{i}"):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()

    # 🎉 Celebrate when all tasks are done
    if all(task["done"] for task in st.session_state.tasks) and st.session_state.tasks:
        st.success("All tasks completed! 🎉")
        st.balloons()
else:
    st.info("No tasks yet. Add one above!")
