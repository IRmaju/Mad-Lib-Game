import streamlit as st

# Function to create the mad libs story
def create_mad_libs(adjective, noun, verb, place):
    story = f"Once upon a time in a {adjective} land, there was a {noun} who loved to {verb} in the {place}. The {noun} was very happy and always had a big smile on its face."
    return story

# Title for the app
st.title("Mad Libs Game!")

# Instructions for the user
st.write("Fill in the blanks to create a fun story!")

# Input fields for the user to fill in
adjective = st.text_input("Adjective (e.g., funny, crazy, colorful)")
noun = st.text_input("Noun (e.g., dog, car, city)")
verb = st.text_input("Verb (e.g., run, jump, dance)")
place = st.text_input("Place (e.g., beach, park, forest)")

# Create the mad libs story when all inputs are provided
if adjective and noun and verb and place:
    story = create_mad_libs(adjective, noun, verb, place)
    st.subheader("Your Mad Libs Story:")
    st.write(story)
else:
    st.warning("Please fill in all the fields above to see your story!")

