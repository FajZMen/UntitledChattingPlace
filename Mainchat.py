from time import sleep as wait
import streamlit as st
import pandas as pd
import datetime
from Datas.Datathis import useraccounts, modaccounts, adminaccounts, devaccount, bannedaccounts, globalchat1, globalchat2, globalchat3, staffchats, adminchats, adminchats2, devlog, shopideas, untitledcoiniventory
from Funks.FunniFuncs import getstates, login, register, chat1, chat2, chat3, chatvip, staffchat, adminchat1, testingchat, devclearchat, accountcreatortool, accountdeletortool, banaccounts, unbanaccount, accountbank, untitledshop, devcoineditor, aboutme
getstates()
loggedin = st.session_state.get("loggedin", False)
viplogin = st.session_state.get("viploggedin", False)
modlogin = st.session_state.get("modloggedin", False)
adminloggedin = st.session_state.get("adminloggedin", False)
devlogin = st.session_state.get("developerlogin", False)
banned = st.session_state.get("banned", False)
dataaccess = st.session_state.get("databankaccess", False)

if not loggedin and not viplogin and not modlogin and not adminloggedin and not devlogin and not banned:
    loging = st.sidebar.radio("Halaman", ["Welcome", "About Dev", "Login", "Register"])
    if loging == "Welcome":
        st.title("Welcome to Untitled Chatting Place!")
        st.write("A Place where you talk with random people on the world! (REAL!!!! VERY COOL!!!!!!)")

    if loging == "Login":
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            login(username, password)
        
    if loging == "Register":
        register()
    
    if loging == "About Dev":
        aboutme()

elif st.session_state.loggedin:
    st.sidebar.title(f"Hello {st.session_state.displayname}!")
    st.sidebar.write(f"Your wallet: {st.session_state.coins}")
    halamanuser = st.sidebar.radio("Halaman", ["Chat 1", "Chat 2", "Chat 3", "Untitled Shop"])

    if halamanuser == "Chat 1":
        chat1()
    if halamanuser == "Chat 2":
        chat2()
    if halamanuser == "Chat 3":
        chat3()
    if halamanuser == "Untitled Shop":
        untitledshop()

    if st.sidebar.button("Logout"):
        st.session_state["loggedin"] = False
        st.rerun()

elif st.session_state.viploggedin:
    st.sidebar.title(f"Hello VIP {st.session_state.displayname}!")
    st.sidebar.write(f"Your wallet: {st.session_state.coins}")
    halamanvip = st.sidebar.radio("Halaman VIP", ["Chat 1", "Chat 2", "Chat 3", "VIP Chat", "Untitled Shop"])
    if halamanvip == "Chat 1":
        chat1()
    if halamanvip == "Chat 2":
        chat2()
    if halamanvip == "Chat 3":
        chat3()
    if halamanvip == "VIP Chat":
        chatvip()
    if halamanvip == "Untitled Shop":
        untitledshop()
    
    if st.sidebar.button("Logout"):
        st.session_state["viploggedin"] = False
        st.rerun()

elif st.session_state.modloggedin:
    st.sidebar.title(f"Hello Moderator {st.session_state.displayname}!")
    st.sidebar.write(f"Your wallet: {st.session_state.coins}")
    halamanmod = st.sidebar.radio("Halaman Moderator", ["Chat 1", "Chat 2", "Chat 3", "Staff Chat", "Mod Panel", "Untitled Shop"])
    if halamanmod == "Chat 1":
        chat1()
    if halamanmod == "Chat 2":    
        chat2()
    if halamanmod == "Chat 3":
        chat3()
    if halamanmod == "Staff Chat":
        staffchat()
    if halamanmod == "Mod Panel":
        modtab = st.tabs(["Ban", "Unban"])
        if modtab[0]:
            st.title("Ban Accounts")
            banuserinput = st.text_input("Enter Username account to be banned")
            reason = st.text_input("Reason")
            if st.button("Ban Account"):
                banaccounts(banuserinput, reason)
        if modtab[1]:
            st.title("Unban Accounts")
            unbanuserinput = st.text_input("Enter Username account to be unban")
            if st.button("Unban Account"):
                unbanaccount(unbanuserinput)
    if halamanmod == "Untitled Shop":
        untitledshop()

    if st.sidebar.button("Logout"):
        st.session_state["modloggedin"] = False
        st.rerun()

elif st.session_state.adminloggedin:
    st.sidebar.title(f"Hello Admin {st.session_state.displayname}!")
    st.sidebar.write(f"Your wallet: {st.session_state.coins}")
    halamanadmin = st.sidebar.radio("Halaman Admin", ["Chat 1", "Chat 2", "Chat 3", "Staff Chat", "Admin Chat", "Admin Panel", "Untitled Shop"])
    if halamanadmin == "Chat 1":
        chat1()
    if halamanadmin == "Chat 2":    
        chat2()
    if halamanadmin == "Chat 3":
        chat3()
    if halamanadmin == "Staff Chat":
        staffchat()
    if halamanadmin == "Admin Chat":
        adminchat1()
    if halamanadmin == "Admin Panel":
        st.title("Admin Panel")
        admintabs = st.tabs(["Ban Accounts", "Unban Accounts"])
        with admintabs[0]:
            st.title("Ban Accounts")
            banuserinput = st.text_input("Enter Username account to be banned")
            reason = st.text_input("Reason")
            if st.button("Ban Account"):
                banaccounts(banuserinput, reason)

        with admintabs[1]:
            st.title("Unban Accounts")
            unbanuserinput = st.text_input("Enter Username account to be unbanned") 
            if st.button("Unban Account"):
                unbanaccount(unbanuserinput)
            
            if bannedaccounts:
                st.dataframe(bannedaccounts)
            else:
                st.write("No accounts are banned")
    if halamanadmin == "Untitled Shop":
        untitledshop()

    if st.sidebar.button("Logout"):
        st.session_state["adminloggedin"] = False
        st.rerun()

elif st.session_state.developerlogin:
    st.sidebar.title(f"Hello Developer {st.session_state.displayname}!")
    st.sidebar.write(f"Your wallet: {st.session_state.coins}")
    halamandev = st.sidebar.radio("Halaman Dev", ["Chat 1", "Chat 2", "Chat 3", "VIP Chat", "Staff Chat", "Admin Chat", "Testing Chat", "Untitled Shop", "Dev Tools", "Account Bank"])
    if halamandev == "Chat 1":
        chat1()
    if halamandev == "Chat 2":
        chat2()
    if halamandev == "Chat 3":
        chat3()
    if halamandev == "VIP Chat":
        chatvip()
    if halamandev == "Staff Chat":
        staffchat()
    if halamandev == "Admin Chat":
        adminchat1()
    if halamandev == "Testing Chat":
        testingchat()
    if halamandev == "Untitled Shop":
        untitledshop()
        if shopideas:
            st.dataframe(shopideas)
        else:
            st.write("No ideas submitted yet")
    if halamandev == "Dev Tools":
        st.title("Dev Tools")
        devtab = st.tabs(["Account Creation Tool", "Account Deletion Tool", "Ban Accounts", "Unban Accounts", "Dev Log", "Coin Editor"])
        with devtab[0]:
            st.title("Account Creation Tool")
            userinput = st.text_input("Username")
            passwordinput = st.text_input("Password")
            walletstart = st.number_input("Coins", min_value=0)
            selectedtype = st.selectbox("Account Type", ["User Account", "VIP Account", "Mod Account", "Admin Account"])
            if st.button("Create Account"):
                accountcreatortool(userinput, passwordinput, walletstart, selectedtype)

        with devtab[1]:
            st.title("Account Deletion Tool")
            deluserinput = st.text_input("Enter Username account to be deleted")
            delselectedtype = st.selectbox("Account Type to Delete", ["User Account", "VIP Account", "Mod Account", "Admin Account"])
            if st.button("Delete Account"):
                accountdeletortool(deluserinput, delselectedtype)

        with devtab[2]:
            st.title("Ban Accounts")
            banuserinput = st.text_input("Enter Username account to be banned")
            reason = st.text_input("Reason")
            if st.button("Ban Account"):
                banaccounts(banuserinput, reason)
            
        with devtab[3]:
            st.title("Unban Accounts")
            unbanuserinput = st.text_input("Enter Username account to be unbanned") 
            if st.button("Unban Account"):
                unbanaccount(unbanuserinput)
            
            if bannedaccounts:
                st.dataframe(bannedaccounts)
            else:
                st.write("No accounts are banned")
        
        with devtab[4]:
            st.title("Dev Log")
            if devlog:
                st.dataframe(devlog)
            else:
                st.write("No logs")

        with devtab[5]:
            st.title("Coin Editor")
            devcoineditor()

    if halamandev == "Account Bank":
        if st.session_state.databankaccess:
            accountbank()
        else:
            getaccess = st.text_input("Enter meme password to access", type="password")
            if st.button("Get Access"):
                if getaccess == "4202024":
                    st.session_state.databankaccess = True
                    st.rerun()
                else:
                    st.error("Wrong")

    if st.sidebar.button("Logout"):
        st.session_state["developerlogin"] = False
        st.session_state["databankaccess"] = False
        st.rerun()
    
    if st.sidebar.button("Clear current chat history"):
        devclearchat(halamandev=halamandev)

elif st.session_state.banned:
    st.sidebar.title(f"You are banned!")
    st.title("This account has been banned!")
    st.write(f"Reason: {st.session_state.bannedreason}")

    if st.sidebar.button("Logout"):
        st.session_state["banned"] = False
        st.rerun()