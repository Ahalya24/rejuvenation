import datetime
import os

import streamlit as st
from openai import OpenAI


def fetch_apple_health_data(apple_id: str, password: str, date: datetime.date) -> dict:
    """Placeholder for fetching movement and nutrition data from Apple Health.

    This function should be replaced with actual integration code that
    authenticates with the user's Apple ID and retrieves HealthKit data.
    For now it returns static example values.
    """
    # TODO: Integrate with Apple HealthKit or Fitness API using the user's credentials.
    return {
        "steps": 5000,
        "calories": 1800,
        "food_log": "Example food log for the day",
    }


def generate_health_reminder(health_data: dict) -> str:
    """Call an LLM to create a personalized health reminder."""
    client = OpenAI()

    prompt = (
        "You are a friendly health assistant. Based on the user's movement and food \n"
        "data, remind them about their health goals for the day and suggest a goal for \n"
        "tomorrow. Today's data:"
        f"\n- Steps: {health_data['steps']}"
        f"\n- Calories: {health_data['calories']}"
        f"\n- Food log: {health_data['food_log']}"
        "\nProvide a concise, motivating message."
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
    )
    return response.choices[0].message.content.strip()


st.title("Daily Health Goal Reminder")

with st.form("auth_form"):
    apple_id = st.text_input("Apple ID")
    password = st.text_input("Password", type="password")
    date = st.date_input("Date", datetime.date.today())
    submitted = st.form_submit_button("Get Reminder")

if submitted:
    if not os.getenv("OPENAI_API_KEY"):
        st.error("OPENAI_API_KEY environment variable not set.")
    else:
        health_data = fetch_apple_health_data(apple_id, password, date)
        reminder = generate_health_reminder(health_data)
        st.subheader("Today's Reminder")
        st.write(reminder)
