
import streamlit as st

# Grade calculation
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


# Page title
st.title("Student Grade Manager")

# Store students in session state
if "students" not in st.session_state:
    st.session_state.students = []

# Form to add a student
with st.form("add_student"):
    name = st.text_input("Name")
    mark = st.number_input(
        "Mark",
        min_value=0,
        max_value=100,
        step=1
    )

    submitted = st.form_submit_button("Add")

    if submitted:
        if name.strip():
            student = {
                "Name": name.strip(),
                "Mark": mark,
                "Grade": get_grade(mark)
            }

            st.session_state.students.append(student)
            st.success("Student added successfully!")
        else:
            st.error("Please enter the student name.")

# Display student results
if st.session_state.students:

    st.subheader("Student Results")

    st.table(st.session_state.students)

    # Calculate class figures
    marks = [student["Mark"] for student in st.session_state.students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # Display metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("Average", f"{average:.1f}")
    col2.metric("Highest", highest)
    col3.metric("Lowest", lowest)

else:
    st.info("No students added yet. Use the form above to add students.")
