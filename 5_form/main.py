import streamlit as st
from datetime import date

def select_course(course_name):
    return st.selectbox(course_name, options=['choice1', 'choice2', 'choice3'], index=0)

with st.form("my_form"):
   st.write("What would you like to order")
   appetizer = select_course("Appetizer")
   main_course = select_course("Main Course")
   desert = select_course("Dessert")
   wine = st.checkbox("Are you bringing your own wine?")
   visit_date = st.date_input("When are you coming?", date.today(), format="DD/MM/YYYY")
   visit_time = st.time_input("At What time are you coming?")
   allergies = st.text_area("Any allergies?", height=200, placeholder="Leave us a note for allergies")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("Form Successfully Submitted")

st.write(f"""Your order summary:

Appetizer: {appetizer}

Main course: {main_course}

Dessert: {desert}

Are you bringing your own wine: {"yes" if wine else "no"}

Date of visit: {visit_date.strftime("%d/%m/%Y")}

Time of visit: {visit_time}

Allergies: {allergies}
""")
