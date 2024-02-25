import streamlit as st
import streamlit.components.v1 as components

st.write("Test")
components.html("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="manifest" href="/manifest.json">
    <script>
        if('serviceWorker' in navigator) {
          navigator.serviceWorker.register('/sw.js', { scope: '/' });
        }
    </script>
    <title>Document</title>
</head>
<body>
    
</body>
</html>
""")