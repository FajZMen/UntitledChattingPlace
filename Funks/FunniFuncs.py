import streamlit as st
import PIL as Image
import pandas as pd
import openpyxl as xl
import datetime
from streamlit_extras.colored_header import colored_header
from random import randint as rng
from time import sleep as wait
from Datas.Datathis import useraccounts, vipaccounts, modaccounts, adminaccounts, devaccount, bannedaccounts, globalchat1, globalchat2, globalchat3, adminchats, adminchats2, staffchats, vipchats, devlog, shopideas, testingchattab

def getstates():
    if "loggedin" not in st.session_state:
        st.session_state.loggedin = False
    if "viploggedin" not in st.session_state:
        st.session_state.viploggedin = False
    if "modloggedin"  not in st.session_state:
        st.session_state.modloggedin = False
    if "adminloggedin" not in st.session_state:
        st.session_state.adminloggedin = False
    if "developerlogin" not in st.session_state:
        st.session_state.developerlogin = False
    if "banned" not in st.session_state:
        st.session_state.banned = False
    if "databankaccess" not in st.session_state:
        st.session_state.databankaccess = False

def login(username, password):
    for banacc in bannedaccounts:
        if banacc["username"] == username:
            st.session_state["banned"] = True
            st.session_state["displayname"] = username
            st.session_state["bannedreason"] = banacc["reason"]
            st.rerun()
            return
    for acc in useraccounts:
        if acc["username"] == username and acc["password"] == password:
            st.session_state["loggedin"] = True
            st.session_state["displayname"] = username
            st.session_state["role"] = "User"
            st.session_state["coins"] = acc["balance"]
            st.rerun()
            return
    for vip in vipaccounts:
        if vip["vipusername"] == username and vip["vippassword"] == password:
            st.session_state["viploggedin"] = True
            st.session_state["displayname"] = username
            st.session_state["role"] = "VIP"
            st.session_state["coins"] = vip["balance"]
            st.rerun()
            return
    for modacc in modaccounts:
        if modacc["modusername"] == username and modacc["modpassword"] == password:
            st.session_state["modloggedin"] = True
            st.session_state["displayname"] = username
            st.session_state["role"] = "Moderator"
            st.session_state["coins"] = modacc["balance"]
            st.rerun()
            return
    for adminacc in adminaccounts:
        if adminacc["adminusername"] == username and adminacc["adminpassword"] == password:
            st.session_state["adminloggedin"] = True
            st.session_state["displayname"] = username
            st.session_state["role"] = "Admin"
            st.session_state["coins"] = adminacc["balance"]
            st.rerun()
            return
    for devacc in devaccount:
        if devacc["developerusername"] == username and devacc["developerpassword"] == password:
            st.session_state["developerlogin"] = True
            st.session_state["displayname"] = username
            st.session_state["role"] = "Developer"
            st.session_state["coins"] = devacc["balance"]
            st.rerun()
            return
    else:
        st.error("Username atau password salah!")

def register():
    st.title("Register")
    regname = st.text_input("Username")
    regpass = st.text_input("Password", type="password")
    if st.button("Register"):
        if not regname or not regpass:
            st.error("Username dan password harus diisi!")
        else:
            for regacc in useraccounts:
                if regacc["username"] == regname:
                    st.error("Username sudah ada, mohon gunakan Username yang lain!")
                    break

                else:
                    useraccounts.append({"username": regname, "password": regpass, "balance": 0})
                    st.success("Akun berhasil dibuat!")
                    wait(1)
                    st.rerun()

def chatcolor(role):
    colors = {
        "User": "#000000",
        "VIP": "#FFD700",  # Gold
        "Moderator": "#00FF00",  # Green
        "Admin": "#FF0000",  # Red
        "Developer": "#0000FF"  # Magenta
    }
    return colors.get(role, "#000000")

def chat1():
    colored_header(label="Chatbox 1", description="Chat with other users here!", color_name="red-70")
    if globalchat1:
        chat1df = pd.DataFrame(globalchat1)

        def stylemessage(row):
            role = str(row["Role"]).strip("{}''") 
            color = chatcolor(role)
            return f'color: {color}'
        
        chat1dfstyle = chat1df.style.apply(lambda x: [stylemessage(x)]*len(x), axis=1)
        st.dataframe(chat1dfstyle, column_config={"Message": st.column_config.TextColumn(width="large")})
    else:
        st.write("No one has chatted here yet!, be the first one to do so!")
    message1 = st.chat_input("Chat here (150 characters max, 250 if you're VIP)")
    if st.button("Refresh"):
        st.rerun()
    if message1:
        if len(message1) > 150 and st.session_state.loggedin or len(message1) > 150 and st.session_state.modloggedin:
            st.warning("Message must be less than 150 characters!")
        elif len(message1) > 250 and st.session_state.viploggedin:
            st.warning("Message must be less than 250 characters!")
        else:
            globalchat1.append({f"Waktu": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "User": {st.session_state.displayname}, "Role": {st.session_state["role"]}, "Message": message1})
            randomcoindropper()
            st.rerun()

def chat2():
    colored_header(label="Chatbox 2", description="Chat with other users here!", color_name="red-70")
    if globalchat2:
        chat2df = pd.DataFrame(globalchat2)

        def stylemessage(row):
            role = str(row["Role"]).strip("{}''") 
            color = chatcolor(role)
            return f'color: {color}'
        
        chat2dfstyle = chat2df.style.apply(lambda x: [stylemessage(x)]*len(x), axis=1)
        st.dataframe(chat2dfstyle, column_config={"Message": st.column_config.TextColumn(width="large")})
    else:
        st.write("No one has chatted here yet!, be the first one to do so!")
    message2 = st.chat_input("Chat here (150 characters max, 250 if you're VIP)")
    if st.button("Refresh"):
        st.rerun()
    if message2:
        if len(message2) > 150 and st.session_state.loggedin or len(message2) > 150 and st.session_state.modloggedin:
            st.warning("Message must be less than 150 characters!")
        elif len(message2) > 250 and st.session_state.viploggedin:
            st.warning("Message must be less than 250 characters!")
        else:
            globalchat2.append({f"Waktu": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "User": {st.session_state.displayname}, "Role": {st.session_state["role"]}, "Message": message2})
            randomcoindropper()
            st.rerun()

def chat3():
    colored_header(label="Chatbox 3", description="Chat with other users here!", color_name="red-70")
    if globalchat3:
        chat3df = pd.DataFrame(globalchat3)

        def stylemessage(row):
            role = str(row["Role"]).strip("{}''") 
            color = chatcolor(role)
            return f'color: {color}'
        
        chat3dfstyle = chat3df.style.apply(lambda x: [stylemessage(x)]*len(x), axis=1)
        st.dataframe(chat3dfstyle, column_config={"Message": st.column_config.TextColumn(width="large")})
    else:
        st.write("No one has chatted here yet!, be the first one to do so!")
    message3 = st.chat_input("Chat here (150 characters max, 250 if you're VIP)")
    if st.button("Refresh"):
        st.rerun()
    if message3:
        if len(message3) > 150 and st.session_state.loggedin or len(message3) > 150 and st.session_state.modloggedin:
            st.warning("Message must be less than 150 characters!")
        elif len(message3) > 250 and st.session_state.viploggedin:
            st.warning("Message must be less than 250 characters!")
        else:
            globalchat3.append({f"Waktu": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "User": {st.session_state.displayname}, "Role": {st.session_state["role"]}, "Message": message3})
            randomcoindropper()
            st.rerun()

def chatvip():
    colored_header(label="VIP Chat", description="Chat with other VIP users here!", color_name="yellow-80")
    if vipchats:
        st.dataframe(vipchats, column_config={"Message": st.column_config.TextColumn(width="large")})
    else:
        st.write("No VIP member has chatted here yet!, be the first one to do so!")
    vipmessage = st.chat_input("Chat here (500 characters max)")
    if st.button("Refresh"):
        st.rerun()
    if vipmessage:
        if len(vipmessage) > 500:
            st.warning("Message must be less than 500 characters!")
        else: 
            vipchats.append({f"Waktu": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "User": {st.session_state.displayname}, "Role": {st.session_state["role"]}, "Message": vipmessage})
            randomcoindropper()
            st.rerun()

def staffchat():
    colored_header(label="Staff Chat", description="Staffs-Exclusive Chatbox", color_name="light-blue-70")
    if staffchats:
        st.dataframe(staffchats, column_config={"Message": st.column_config.TextColumn(width="large")})
    else:
        st.write("No staff member has chatted here yet!, be the first one to do so!")
    staffmessage = st.chat_input("Chat here")
    if st.button("Refresh"):
        st.rerun()
    if staffmessage:
        staffchats.append({f"Waktu": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "User": {st.session_state.displayname}, "Role": {st.session_state["role"]}, "Message": staffmessage})
        st.rerun()

def adminchat1():
    colored_header(label="Admin Chat", description="Admins-Exclusive Chatbox", color_name="blue-70")
    if adminchats:
        st.dataframe(adminchats, column_config={"Message": st.column_config.TextColumn(width="large")})
    else:
        st.write("No admin member has chatted here yet!, be the first one to do so!")
    adminmessage = st.chat_input("Chat here")
    if st.button("Refresh"):
        st.rerun()
    if adminmessage:
        adminchats.append({f"Waktu": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "User": {st.session_state.displayname}, "Role": {st.session_state["role"]}, "Message": adminmessage})
        randomcoindropper()
        st.rerun()

def testingchat():
    colored_header(label="Testing Chat", description="Just a Text Chatbox used to test a test", color_name="blue-70")
    if testingchattab:
        testdf = pd.DataFrame(testingchattab)

        def stylemessage(row):
            role = str(row["Role"]).strip("{}''")  # Clean the role string
            color = chatcolor(role)
            return f'color: {color}'
        
        testdfstyle = testdf.style.apply(lambda x: [stylemessage(x)]*len(x), axis=1)
        st.dataframe(testdfstyle, column_config={"Message": st.column_config.TextColumn(width="large")})
    else:
        st.write("Teehee funni")
    testingmessage = st.chat_input("Chat here")
    if st.button("Refresh"):
        st.rerun()
    if testingmessage:
        testingchattab.append({f"Waktu": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "User": {st.session_state.displayname}, "Role": {st.session_state["role"]}, "Message": testingmessage})
        randomcoindropper()
        st.rerun()

def devclearchat(halamandev):
    if halamandev == "Chat 1":
        globalchat1.clear()
    if halamandev == "Chat 2":
        globalchat2.clear()
    if halamandev == "Chat 3":
        globalchat3.clear()
    if halamandev == "VIP Chat":
        vipchats.clear()
    if halamandev == "Staff Chat":
        staffchats.clear()
    if halamandev == "Admin Chat":
        adminchats.clear()
    else:
        st.write("Error")
    st.rerun()

def accountcreatortool(userinput, passinput, walletstart, selectedtype):
    if selectedtype == "User Account":
        useraccounts.append({"username": userinput, "password": passinput, "balance": walletstart})
        st.success("Account created!")
    elif selectedtype == "VIP Account":
        vipaccounts.append({"vipusername": userinput, "vippassword": passinput, "balance": walletstart})
        st.success("VIP Account created!")
    elif selectedtype == "Mod Account":
        modaccounts.append({"modusername": userinput, "modpassword": passinput, "balance": walletstart})
        st.success("Mod Account created!")
    elif selectedtype == "Admin Account":
        adminaccounts.append({"adminusername": userinput, "adminpassword": passinput, "balance": walletstart})
        st.success("Admin Account created!")
    else:
        st.write("You didnt select the account type bruh")

def accountdeletortool(deluserinput, delselectedtype):
    if delselectedtype == "User Account":
        for user in useraccounts:
            if deluserinput == user["username"]:
                useraccounts.remove(user)
                st.success("User Account deleted!")
                break
        else:
            st.error("User Account not found!")
    elif delselectedtype == "VIP Account":
        for vipd in vipaccounts:
            if deluserinput == vipd["vipusername"]:
                vipaccounts.remove(vipd)
                st.success("VIP Account deleted!")
                break
        else:
            st.error("VIP Account not found!")
    elif delselectedtype == "Mod Account":
        for dmodacc in modaccounts:
            if deluserinput == dmodacc["modusername"]:
                modaccounts.remove(dmodacc)
                st.success("Mod Account deleted!")
                break
        else:
            st.error("Mod Account not found!")
    elif delselectedtype == "Admin Account":
        for dauser in adminaccounts:
            if deluserinput == "Radit" or deluserinput == "Tubagus":
                st.error("This Account cannot be Deleted!")
                break

            elif deluserinput == dauser["adminusername"]:
                adminaccounts.remove(dauser)
                st.success("Admin Account deleted!")
                break
        else:
            st.error("Admin Account not found!")
    else:
        st.write("You didnt select the account type bruh")

def banaccounts(banuserinput, reason):
    for alrban in bannedaccounts:
        if banuserinput == alrban["username"]:
            st.error("Account already banned!")
            return

    accountisnotbanned = True

    for acctoban in useraccounts:
        if banuserinput == acctoban["username"]:
            bannedaccounts.append({"username": banuserinput, "reason": reason})
            st.success("Account Banned!")
            accountisnotbanned = False
            devlog.append({"Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Log": f"{st.session_state.role} {st.session_state.displayname} has Banned {banuserinput} for {reason}"})
            break

    for vipaccban in vipaccounts:
        if banuserinput == vipaccban["vipusername"]:
            bannedaccounts.append({"username": banuserinput, "reason": reason})
            st.success("Account Banned!")
            accountisnotbanned = False
            devlog.append({"Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Log": f"{st.session_state.role} {st.session_state.displayname} has Banned {banuserinput} for {reason}"})
            break 
    
    if accountisnotbanned:
        st.error("Account not found.")

def unbanaccount(unbanuserinput):
    for unban in bannedaccounts:
        if unbanuserinput == unban["username"]:
            bannedaccounts.remove(unban)
            st.success("Account Unbanned!")
            devlog.append({"Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Log": f"{st.session_state.role} {st.session_state.displayname} Unbanned {unbanuserinput}"})
            break
    else:
        st.error("Account not found.")

def accountbank():
    selectedlist = st.selectbox("Account List", ["User Accounts", "VIP Accounts", "Mod Accounts", "Admin Accounts", "Developer Accounts"])
    if selectedlist == "User Accounts":
        st.dataframe(useraccounts)
    elif selectedlist == "VIP Accounts":
        st.dataframe(vipaccounts)
    elif selectedlist == "Mod Accounts":
        st.dataframe(modaccounts)
    elif selectedlist == "Admin Accounts":
        st.dataframe(adminaccounts)
    elif selectedlist == "Developer Accounts":
        st.dataframe(devaccount)
    else:
        st.write("Nothing to show")

def randomcoindropper():
    dropcoinorno = rng(1, 4)
    if dropcoinorno == 2:
        drops = rng(10, 100)
        
        if st.session_state.role == "VIP":
            finalamount = drops * 2
        elif st.session_state.role == "Developer": 
            finalamount = drops * 22
        else:
            finalamount = drops

        st.session_state.coins += finalamount
        targetusername = st.session_state.displayname
        
        for tacc in useraccounts:
            if tacc["username"] == targetusername:
                tacc["balance"] += finalamount
                return
                
        for tvip in vipaccounts:
            if tvip["vipusername"] == targetusername:
                tvip["balance"] += finalamount
                return
                
        for tmod in modaccounts:
            if tmod["modusername"] == targetusername:
                tmod["balance"] += finalamount
                return
                
        for tadmin in adminaccounts:
            if tadmin["adminusername"] == targetusername:
                tadmin["balance"] += finalamount
                return
                
        for tdev in devaccount:
            if tdev["developerusername"] == targetusername:
                tdev["balance"] += finalamount
                return

def devcoineditor():
    usertogive = st.text_input("Target (Username)")
    addordeduct = st.selectbox("Add or Deduct?", ["Add", "Deduct"])
    howmany = st.number_input(f"How much coins?", min_value=0)
    if st.button("Give"):
        moneygivenordeducted = False
        for cuser in useraccounts:
            if usertogive == cuser["username"]:
                if addordeduct == "Add":
                    cuser["balance"] += howmany
                    moneygivenordeducted = True
                    st.success("Coins given!")
                    break
                elif addordeduct == "Deduct":
                    cuser["balance"] -= howmany
                    moneygivenordeducted = True
                    st.success("Coins deducted!")
                    break

        for vuser in vipaccounts:
            if usertogive == vuser["vipusername"]:
                if addordeduct == "Add":
                    vuser["balance"] += howmany
                    moneygivenordeducted = True
                    st.success("Coins given!")
                    break
                elif addordeduct == "Deduct":
                    vuser["balance"] -= howmany
                    moneygivenordeducted = True
                    st.success("Coins deducted!")
                    break
        
        for moduser in modaccounts:
            if usertogive == moduser["modusername"]:
                if addordeduct == "Add":
                    moduser["balance"] += howmany
                    moneygivenordeducted = True
                    st.success("Coins given!")
                    break
                elif addordeduct == "Deduct":
                    moduser["balance"] -= howmany
                    moneygivenordeducted = True
                    st.success("Coins deducted!")
                    break

        for adminuser in adminaccounts:
            if usertogive == adminuser["adminusername"]:
                if addordeduct == "Add":
                    adminuser["balance"] += howmany
                    moneygivenordeducted = True
                    st.success("Coins given!")
                    break
                elif addordeduct == "Deduct":
                    adminuser["balance"] -= howmany
                    moneygivenordeducted = True
                    st.success("Coins deducted!")
                    break

        for devuser in devaccount:
            if usertogive == devuser["devusername"]:
                if addordeduct == "Add":
                    devuser["balance"] += howmany
                    moneygivenordeducted = True
                    st.success("Coins given!")
                    break
                elif addordeduct == "Deduct":
                    devuser["balance"] -= howmany
                    moneygivenordeducted = True
                    st.success("Coins deducted!")
                    break
        
        if not moneygivenordeducted:
            st.error("User not found!")

def untitledshop(): #In Development
    st.title("Untitled Shop")
    st.warning("Coming soon!")
    st.write("While this feature is still in development, you can submit me ideas by submiting them below!")
    shopidea = st.chat_input("Submit your Idea here")
    if shopidea:
        shopideas.append({f"User": {st.session_state.displayname}, "Idea": shopidea})
        st.success("Submitted, Thanks!")

def trading(): #In Development
    st.title("Trading")

def gift(): #In Development
    st.title("Gift")

# //////////////////// Micelaniouses
def rules():
    st.title("Rules")
    st.write("1. No Spamming, results in Immideate Ban without hesitation.")
    st.write("2. No Racism, Homophobia, or any other form of Hate Speech. results in Immideate Ban or Account Termination without hesitation.")

def aboutme():
    st.image("Funni/Ok.jpg")
    st.title("About Me")
    st.write("Hiya there!, im Fajar or FajZ whatever you wanna call me with, an Indonesian Developer who made this dumb silly web project cuz im bored. anyway have fun xd.")
