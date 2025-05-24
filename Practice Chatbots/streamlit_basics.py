import streamlit as st



# To an image
st.image("Chatbots-in-Machine-Learning.webp", caption="RamaSethu", use_container_width=True)

# To write the title of the app
st.title("RamaSethu Chatbot")

# To write the header of the app
st.header("Chat with Karna")

# To write the subheader of the app
st.subheader("Bot details")

#To provide information about the app
st.info("This is a chatbot that can answer your questions about RamaSethu. You can ask me anything and I will try to answer it. If I don't know the answer, I will let you know.")


# To write the warnig mssage
st.warning("This is a demo app. The chatbot is not perfect and may not always give the correct answer. Please use it at your own risk.")

# Write 
st.write("Kartheek Kottapalli")

st.write(range(50))


# To write the error message
st.error("Wrong Password.")

# To write the success message
st.success("Login Successful.")


# Markdown
st.markdown("## This is a markdown text")
st.markdown("### This is a markdown text")


st.markdown(":moon:")

st.text("This is a text")



# Widgets for user input

# Checkbox for voice output
st.checkbox('login')

# button
st.button('submit')
# Radio button
st.radio("Choose an option", ["Male", "Female"])