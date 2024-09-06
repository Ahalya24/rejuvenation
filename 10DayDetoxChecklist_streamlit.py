

import streamlit as st

# Initialize session state for day index if not already done
if 'day_index' not in st.session_state:
    st.session_state.day_index = 1

# Function to handle day navigation
def navigate_day(direction):
    if direction == "next" and st.session_state.day_index < 10:
        st.session_state.day_index += 1
    elif direction == "prev" and st.session_state.day_index > 1:
        st.session_state.day_index -= 1

# Display navigation buttons
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("Previous Day"):
        navigate_day("prev")
with col3:
    if st.button("Next Day"):
        navigate_day("next")


# Quotes for each day
quotes = [
    "The food you eat can be either the safest and most powerful form of medicine or the slowest form of poison.",
    "The power of community to create health is far greater than any physician, clinic, or hospital.",
    "Eat food. Not too much. Mostly plants.",
    "Your genes load the gun, but your lifestyle pulls the trigger.",
    "You are what you eat — so don’t be fast, cheap, easy, or fake.",
    "The foundation of good health is a healthy, balanced diet.",
    "Health is not just the absence of disease but a state of immense vitality.",
    "Food is information that speaks to our genes and turns them on or off and affects their function moment to moment.",
    "True health care reform starts in your kitchen, not in Washington.",
    "When diet is wrong, medicine is of no use. When diet is correct, medicine is of no need."
]

# Checklist items
checklist_items = [
    "Wake Up: Drink a large glass of water with lemon :lemon: :droplet: ",
    "Take morning supplements - Anastrazole, Vit D , Omega 3, Calcium, Mitopure, Ashwagandha",
    "20-30 min light/moderate exercise :running: ",
    "Postworkout: Drink the stanley water or herbal tea :droplet: ",
    "Detox-approved breakfast",
    "Morning : 5 min meditation/deep breathing :prayer_beads: ",
    "Mid-Morning: Drink a glass of water or herbal tea :droplet:",
    "Snack (if needed): Nuts/seeds or a piece of fruit",
    "Detox-friendly lunch",
    "Afternoon : 5 min meditation/deep breathing :prayer_beads: ",
    "Take midday supplements - Probiotic",
    "Afternoon: Drink a glass of water or herbal tea :droplet: ",
    "30-60 min vigorous exercise :woman-lifting-weights:",
    "Snack (if needed): Veggie sticks with hummus or berries",
    "Detox-friendly dinner",
    "Take evening supplements - Magnesium",
    "Unwind with relaxing activity :blossom: ",
    "Before Bed: Drink a final glass of water or herbal tea :droplet:",
    "Aim for 7-8 hours of sleep",
]

# Initialize session state for checkboxes and journal if not already done
day_key = f"day_{st.session_state.day_index}"
if day_key not in st.session_state:
    st.session_state[day_key] = {
        'checklist': [False] * len(checklist_items),
        'journal': ''
    }

# Display quote for the selected day
st.header(f"10-Day Detox Day {st.session_state.day_index}")
st.write(quotes[st.session_state.day_index - 1])  # Display the quote for the selected day

# Display progress bar
completed_items = sum(st.session_state[day_key]['checklist'])
total_items = len(checklist_items)
progress = completed_items / total_items
st.progress(progress)
st.write(f"Progress: {completed_items} out of {total_items} tasks completed")

# Display checklist
st.subheader("Daily Checklist")
for i, item in enumerate(checklist_items):
    st.session_state[day_key]['checklist'][i] = st.checkbox(item, value=st.session_state[day_key]['checklist'][i])

# Journal entry section
st.subheader("Daily Journal")
st.session_state[day_key]['journal'] = st.text_area("Write your journal entry here...", value=st.session_state[day_key]['journal'])

# Save the state
if st.button("Save Progress"):
    st.success("Progress saved!")


