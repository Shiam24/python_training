import streamlit as st
import json
import os

DATA_FILE = "bank_data.json"

# ---------- Save data to JSON ----------
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
    st.success(f"Data saved to {DATA_FILE} successfully!")

# ---------- Load existing data (if available) ----------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                st.warning("JSON file was empty or corrupted. Starting fresh.")
                return {}
    else:
        return {}

# ---------- Main Streamlit app ----------
def main():
    st.title("Bank Account Manager")

    if "data" not in st.session_state:
        st.session_state.data = load_data()

    menu = ["Create Account", "Display All Accounts", "Update Account", "Delete Account", "Save & Exit"]
    choice = st.sidebar.selectbox("Menu", menu)

    data = st.session_state.data

    if choice == "Create Account":
        st.header("Create Account")
        name = st.text_input("Enter account holder name").strip()
        pin = st.text_input("Enter 4-digit PIN", max_chars=4, type="password").strip()
        balance = st.number_input("Enter initial balance", min_value=0.0, format="%.2f")

        if st.button("Create"):
            if not name:
                st.error("Account holder name cannot be empty.")
            elif name in data:
                st.error(f"Account for '{name}' already exists!")
            elif len(pin) != 4 or not pin.isdigit():
                st.error("PIN must be exactly 4 digits.")
            else:
                data[name] = {"account_holder": name, "pin": pin, "balance": balance}
                st.success(f"Account for {name} added successfully!")

    elif choice == "Display All Accounts":
        st.header("All Bank Accounts")
        if not data:
            st.info("No accounts found.")
        else:
            for account in data.values():
                st.write(f"**Name:** {account['account_holder']}  |  **PIN:** {account['pin']}  |  **Balance:** ${account['balance']:.2f}")

    elif choice == "Update Account":
        st.header("Update Account")
        name = st.text_input("Enter the account holder name to update").strip()

        if name and name in data:
            update_choice = st.radio("What would you like to update?", ("PIN", "Balance"))
            if update_choice == "PIN":
                new_pin = st.text_input("Enter new 4-digit PIN", max_chars=4, type="password").strip()
                if st.button("Update PIN"):
                    if len(new_pin) != 4 or not new_pin.isdigit():
                        st.error("PIN must be exactly 4 digits.")
                    else:
                        data[name]['pin'] = new_pin
                        st.success(f"PIN updated for {name}")
            elif update_choice == "Balance":
                new_balance = st.number_input("Enter new balance", min_value=0.0, format="%.2f")
                if st.button("Update Balance"):
                    data[name]['balance'] = new_balance
                    st.success(f"Balance updated for {name}")
        elif name:
            st.error(f"Account for '{name}' does not exist!")

    elif choice == "Delete Account":
        st.header("Delete Account")
        name = st.text_input("Enter the account holder name to delete").strip()

        if name and name in data:
            if st.button("Delete Account"):
                confirm = st.checkbox(f"Are you sure you want to delete account '{name}'?")
                if confirm:
                    del data[name]
                    st.success(f"Account '{name}' deleted successfully!")
        elif name:
            st.error(f"Account for '{name}' does not exist!")

    elif choice == "Save & Exit":
        save_data(data)
        st.write("Data saved. You can close this tab now.")

if __name__ == "__main__":
    main()
