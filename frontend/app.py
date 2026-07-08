import streamlit as st
import requests
from datetime import datetime

st.set_page_config(
    page_title="AI Task Manager",
    page_icon="📝",
    layout="wide"
)

BASE_URL = "http://127.0.0.1:8000"

# ---------------- SESSION STATE ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "edit_task" not in st.session_state:
    st.session_state.edit_task = None

if "ai_title" not in st.session_state:
    st.session_state.ai_title = ""

if "ai_description" not in st.session_state:
    st.session_state.ai_description = ""

if "ai_priority" not in st.session_state:
    st.session_state.ai_priority = "Medium"

# ==========================================================
# LOGIN / SIGNUP PAGE
# ==========================================================

if not st.session_state.logged_in:

    st.title("📝 AI Task Manager")

    page = st.radio(
        "Select",
        ["Login", "Sign Up"],
        horizontal=True
    )

    st.divider()

    # ---------------- LOGIN ----------------

    if page == "Login":

        st.subheader("Login")

        email = st.text_input("Email")
        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            response = requests.post(
                f"{BASE_URL}/login",
                json={
                    "email": email,
                    "password": password
                }
            )

            if response.status_code == 200:

                st.session_state.logged_in = True
                st.rerun()

            else:

                st.error("Invalid email or password")

    # ---------------- SIGNUP ----------------

    else:

        st.subheader("Create Account")

        username = st.text_input("Username")

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Sign Up"):

            response = requests.post(
                f"{BASE_URL}/signup",
                json={
                    "username": username,
                    "email": email,
                    "password": password
                }
            )

            if response.status_code == 200:

                st.success(
                    "Account created successfully!"
                )

                st.info(
                    "Go to the Login tab and sign in."
                )

            else:

                try:
                    st.error(response.json()["detail"])
                except:
                    st.error("Signup failed.")

# ==========================================================
# DASHBOARD
# ==========================================================

else:

    col1, col2 = st.columns([8, 1])

    with col1:
        st.title("📝 AI Task Manager")

    with col2:

        if st.button("Logout"):

            st.session_state.logged_in = False
            st.session_state.edit_task = None

            st.session_state.ai_title = ""
            st.session_state.ai_description = ""
            st.session_state.ai_priority = "Medium"

            st.rerun()

    st.divider()

    # ------------------------------------------------------

    if st.session_state.edit_task is None:

        st.subheader("🤖 Generate Task with AI")

        prompt = st.text_area(
            "Describe your work"
        )

        if st.button("Generate with AI"):

            response = requests.post(
                f"{BASE_URL}/ai/suggest",
                json={
                    "prompt": prompt
                }
            )

            if response.status_code == 200:

                ai = response.json()

                st.session_state.ai_title = ai["title"]
                st.session_state.ai_description = ai["description"]
                st.session_state.ai_priority = ai["priority"]

                st.rerun()

            else:

                st.error("AI generation failed.")

        st.divider()

        st.subheader("➕ Create Task")

        title = st.text_input(
            "Title",
            value=st.session_state.ai_title
        )

        description = st.text_area(
            "Description",
            value=st.session_state.ai_description
        )

        due_date = st.date_input(
            "Due Date"
        )

        priorities = [
            "Low",
            "Medium",
            "High"
        ]

        priority = st.selectbox(
            "Priority",
            priorities,
            index=priorities.index(
                st.session_state.ai_priority
            )
        )

        if st.button("Create Task"):

            response = requests.post(
                f"{BASE_URL}/tasks",
                json={
                    "title": title,
                    "description": description,
                    "due_date": str(due_date),
                    "priority": priority
                }
            )

            if response.status_code == 200:

                st.success("Task created successfully.")

                st.session_state.ai_title = ""
                st.session_state.ai_description = ""
                st.session_state.ai_priority = "Medium"

                st.rerun()

            else:

                st.error("Unable to create task.")

    # =====================================================
    # EDIT MODE
    # =====================================================

    else:

        task = st.session_state.edit_task

        st.subheader("✏ Edit Task")

        title = st.text_input(
            "Title",
            value=task["title"]
        )

        description = st.text_area(
            "Description",
            value=task["description"]
        )

        due_date = st.date_input(
            "Due Date",
            value=datetime.strptime(
                task["due_date"],
                "%Y-%m-%d"
            ).date()
        )

        priorities = [
            "Low",
            "Medium",
            "High"
        ]

        priority = st.selectbox(
            "Priority",
            priorities,
            index=priorities.index(
                task["priority"]
            )
        )

        statuses = [
            "To Do",
            "In Progress",
            "Done"
        ]

        status = st.selectbox(
            "Status",
            statuses,
            index=statuses.index(
                task["status"]
            )
        )

        c1, c2 = st.columns(2)

        with c1:

            if st.button("Update Task"):

                response = requests.put(
                    f"{BASE_URL}/tasks/{task['id']}",
                    json={
                        "title": title,
                        "description": description,
                        "due_date": str(due_date),
                        "priority": priority,
                        "status": status
                    }
                )

                if response.status_code == 200:

                    st.success("Task updated.")

                    st.session_state.edit_task = None

                    st.rerun()

                else:

                    st.error("Update failed.")

        with c2:

            if st.button("Cancel"):

                st.session_state.edit_task = None

                st.rerun()

    st.divider()


    # ---------------- TASK LIST ----------------

    st.subheader("Your Tasks")

    response = requests.get(f"{BASE_URL}/tasks")

    if response.status_code == 200:

        tasks = response.json()

        if len(tasks) == 0:

            st.info("No tasks available.")

        else:

            for task in tasks:

                st.write(f"### {task['title']}")
                st.write(task["description"])
                st.write(f"Priority : {task['priority']}")
                st.write(f"Status : {task['status']}")
                st.write(f"Due Date : {task['due_date']}")

                col1, col2 = st.columns(2)

                with col1:

                    if st.button(
                        "Edit",
                        key=f"edit_{task['id']}"
                    ):

                        st.session_state.edit_task = task

                        st.rerun()

                with col2:

                    if st.button(
                        "Delete",
                        key=f"delete_{task['id']}"
                    ):

                        response = requests.delete(
                            f"{BASE_URL}/tasks/{task['id']}"
                        )

                        if response.status_code == 200:

                            st.success("Task Deleted")

                            st.rerun()

                st.divider()