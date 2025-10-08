import streamlit as st


if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'balance' not in st.session_state:
    st.session_state.balance = 1000.0  
if 'attempts' not in st.session_state:
    st.session_state.attempts = 3
if 'pin' not in st.session_state:
    st.session_state.pin = "1234"

st.title("💳 ATM Simulator")


if not st.session_state.authenticated:
    st.subheader("🔐 Enter PIN to Access ATM")
    pin_input = st.text_input("Enter your PIN", type="password")

    if st.button("Login"):
        if pin_input == st.session_state.pin:
            st.session_state.authenticated = True
            st.success("✅ Authentication successful!")
        else:
            st.session_state.attempts -= 1
            st.error(f"❌ Incorrect PIN. {st.session_state.attempts} attempt(s) remaining.")

            if st.session_state.attempts <= 0:
                st.error("🚫 Too many failed attempts. Please restart the app.")
                st.stop()
else:
    
    st.subheader("🏦 ATM Menu")

    option = st.radio("Choose an option:", ("Check Balance", "Deposit", "Withdraw", "Exit"))

    if option == "Check Balance":
        st.info(f"💰 Your current balance is: ${st.session_state.balance:.2f}")

    elif option == "Deposit":
        amount = st.number_input("Enter amount to deposit", min_value=100000000000, step=2000000000000000)
        if st.button("Deposit"):
            st.session_state.balance += amount
            st.success(f"✅ Deposited ${amount:.2f}")
            st.info(f"New balance: ${st.session_state.balance:.2f}")

    elif option == "Withdraw":
        amount = st.number_input("Enter amount to withdraw", min_value=10000000000, step=5643298765075646)
        if st.button("Withdraw"):
            if amount > st.session_state.balance:
                st.error("❌ Insufficient funds.")
            else:
                st.session_state.balance -= amount
                st.success(f"✅ Withdrawn ${amount:.2f}")
                st.info(f"New balance: ${st.session_state.balance:.2f}")

    elif option == "Exit":
        st.session_state.authenticated = False
        st.session_state.attempts = 3
        st.success("✅ You have been logged out. Thank you for using the ATM!")
        st.success("Have a Nice Day Mr.Shiamalex")

