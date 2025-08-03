import streamlit as st 
import base64


# streamlit_pro = subprocess.Popen(["streamlit", "run", "Server.py"])

# time.sleep(3)

# public_url = ngrok.connect(8501)
# print(f"Streamlit URL : {public_url}")

# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     print("Exiting...")
#     streamlit_pro.terminate()
#     ngrok.kill()


def getbase(filepath):
    with open(filepath,"rb") as fl:
        data = fl.read()
    return base64.b64encode(data).decode()

imgpath = r"D:\Something Gretting\4.jpeg"
base = getbase(imgpath)


st.markdown(

    f"""
    <style>
    .stApp{{
        background-image:  url("data:image/jpeg;base64,{base}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
   
    }}
    <style>""",
    unsafe_allow_html=True
)

st.title("Happy Friendship day ")

st.write("Happy Friendship day to all My Friends  ")
st.write(''' Bro Thanks to be Kind Even when i Behave "rude" , I thanks to God that i got Such Friends''')
st.write("Thank you For Everything Bro")
st.write(" Your's RudeFriend")

button = st.button("Gift for You ")

if button:
    st.title("Moments with you ")
    st.image(r"D:\Something Gretting\1.jpeg")
    st.image(r"D:\Something Gretting\2.jpeg")
    st.image(r"D:\Something Gretting\3.jpeg")
    st.image(r"D:\Something Gretting\5.jpeg")
    st.write("Wesite by - rude friend")
    #---------------------------------------------------------------------------------- 
    # audiopath = r"D:\Something Gretting\Relaxing Music to Sleep Instantly – Stress Relief & Mental Calm relax relaxing.mp3"
    # components.html(f"""
                    
    #             <audio id = "myAudio" autoplay>
    #                 <source src = "{audiopath}" type ="audio/mpeg">
    #             </audio>
    #             <script>
    #                 setTimeout(function(){{
    #                     document.getElementById("myAudio").play();
    #                 }}, 500);  // delay to trigger autoplay
    #             </script>
    #             """,
    #            height = 0 )

    

