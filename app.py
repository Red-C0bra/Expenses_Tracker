import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Page Title & App Header
st.title("💰 Smart Expense Tracker")
st.subheader("Track your daily spending and see where your money goes.")

# 2. Initialize an empty list in Streamlit's temporary memory (Session State)
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# 3. Sidebar Input Form
st.sidebar.header("Add New Expense")
with st.sidebar.form("expense_form", clear_on_submit=True):
    category = st.selectbox(
        "Category",
        ["Food & Dining", "Rent & Bills", "Entertainment", "Transport", "Shopping"],
    )
    amount = st.number_input("Amount ($)", min_value=0.01, step=1.0)
    note = st.text_input("Note (Optional)")
    submitted = st.form_submit_button("Add Expense")

    if submitted:
        # Add the data to our session state list
        st.session_state.expenses.append(
            {"Category": category, "Amount": amount, "Note": note}
        )
        st.success("Expense added successfully!")
# 4. Main Panel Logic
if st.session_state.expenses:
    # Convert list to a Pandas DataFrame
    df = pd.DataFrame(st.session_state.expenses)

    # Display Metrics
    total_spent = df["Amount"].sum()
    st.metric(label="Total Expenses", value=f"${total_spent:,.2f}")

    # Display Data Table
    st.write("### 📝 Expense History")
    st.dataframe(df)

    # Visualizations (Group data by category)
    st.write("### 📊 Spending Breakdown")
    category_totals = df.groupby("Category")["Amount"].sum()

    # Streamlit Native Bar Chart
    st.bar_chart(category_totals)

else:
    # Message displayed if no data is added yet
    st.info("The tracker is empty. Use the sidebar to add your first expense!")
