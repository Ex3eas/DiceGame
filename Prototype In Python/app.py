import streamlit as st 
import random 
st.title("2 Player Dice game")

# ---Player Inputs---- 

P1 = st.text_input("Enter Your Name P1") 
P2 = st.text_input("Enter Your Name P2") 

if P1 == P2:
    st.write("Sorry this name is in use")
#---Buttons--- 

Start_button = st.button("Start the game?")

if Start_button:
    dice_button = st.button("Click to Roll")

    if dice_button:
        dice_roll = random.randint(1,6)
        st.write("You rolled : ", dice_roll)    
