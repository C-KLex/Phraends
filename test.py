import streamlit as st


def testfun():
    test1 = ['link1', 'link2', 'link3']
    test2 = ['summary1', 'summary2', 'summary3']
    return test1, test2

testlist = testfun()
st.write("test_title")
for i in range(len(testlist[0])):
    # st.write(f"{i+1}. link: {testlist[0][i]} ·   · summary: {testlist[1][i]}")
    st.write(str(i+1) + '. link: ' + testlist[0][i])
    st.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; summary: ' + testlist[1][i])