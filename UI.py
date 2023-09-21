import streamlit as st

def clear_background():
    st.markdown(
    """
<style>
[data-testid^="stAppViewContainer"]{
    background-color=black;

}
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
[data-testid^="stFormSubmitButton"] > button:first-child {
    background-color: transparent;
    text-align: center;
    margin: 10;
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
[data-testid^="stFormSubmitButton"]:hover > button:first-child {
    border-color: green;
}

[class^="st-b"]  {
    color: white;
}
[data-testid^="stMarkdownContainer"]{
    background-color: transparent;
    size: 20px;
    color: white;
    weight: bold;
}

#MainMenu {visibility: hidden;}

[class^="main css-k1vhr4 egzxvld3"]{
    background-color:#0e1117;
}

</style>
""",
    unsafe_allow_html=True,
)
    
def make_footer():
    st.markdown(
    """
<style>
footer {visibility: hidden;}
footer:after {
    content:'Made with ❤️ by Pande Dani';
    visibility: visible;
    display: block;
    position: relative;
    #background-color: red;
    padding: 5px;
    top: 2px;
    font-size: 16px;
    color: white;
    text-align: center;
}
</style>
""",
    unsafe_allow_html=True,
)

def make_header():
    st.markdown(
    """
<style>
header {visibility: hidden;}
header:after {
    content:'SICKATHON';
    visibility: visible;
    display: block;
    position: relative;
    background-color: #7a1214;
    padding-left: 20px;
    padding-bottom: 5px;
    font-size: 40px;
    color: white;
    text-align: left;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}
</style>
""",
    unsafe_allow_html=True,
)