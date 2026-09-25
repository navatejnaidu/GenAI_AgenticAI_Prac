import streamlit as st

st.title("Hello Guys This is Navatej")
st.markdown( 
    """
    Welcome to your **Streamlit Playground!** 🚀

    This is a place where you can **experiment, create, and have fun** 
    while discovering what Streamlit can do.

    **There's :rainbow[so much] you can build!**

    Explore the examples below, try out different features, and 
    **turn your ideas into interactive apps.** ✨

    Just click the buttons above to get started and see Streamlit 
    in action!
    """
)

if st.button("Send balloons!"):
    st.balloons()
    st.success("🎉")