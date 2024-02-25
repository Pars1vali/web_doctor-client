import streamlit as st
import streamlit.components.v1 as components

st.write("I'm hier")
components.html("""<!DOCTYPE html>
<html lang="en-US" dir="ltr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <link rel="shortcut icon" href="https://c.s-microsoft.com/favicon.ico?v2" />
    <link rel="manifest" href="/manifest.json">
    <title>Temperature converter</title>
  </head>
  <body>
    <h1>Temperature converter</h1>
  </body>
</html>""")