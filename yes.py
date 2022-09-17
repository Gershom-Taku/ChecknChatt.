import pyrebase
from datetime import datetime
from click import style
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
import pickle
import sklearn


# Configuration Key
#firebaseConfig = {
 #   'apiKey': " ",
  #  'authDomain': " ",
   # 'projectId': " ",
    #'databaseURL': " ",
    #'#storageBucket': " ",
    #'m#essagingSenderId': "",
    #'appId': " ",
    #'measurementId': " "
#}
st.set_page_config(page_title="Welcome To ChecknChatt-APP", page_icon=":tada:", layout='wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
      st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html= True)  
local_css("style.css")

html_temp = """
        <div style = "background-color:royalblue;padding:10px;border-radius:30px;width :auto;">
        <h1 style = "color:white;text-align:center;font-size:40px;">ChecknChat-App </h1>
        </div>
        """
components.html(html_temp)

A,B = st.columns(2)
with A:
    st.write("Test your self and share your experience with others here!")
    st.success("It's fortunate to discover your self that you are health and safe at ChecknChat🆗")
    st.warning("If you discover that you have been affected,please consult a doctor or hear from others here through out their shared experiences and shared moments!🧑‍⚕️")
     
    
    with B:
        lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_6qyxpnwe.json")
        st_lottie(lottie_coding,height= 300,key = "care")

firebaseConfig = {
  'apiKey': "AIzaSyD8HUrdIhoZoBuHjs36oQsqzexAb_N5jMs",
  'authDomain': "all-in-one-detection-app.firebaseapp.com",
  'projectId': "all-in-one-detection-app",
  'databaseURL':"https://all-in-one-detection-app-default-rtdb.europe-west1.firebasedatabase.app/",
  'storageBucket': "all-in-one-detection-app.appspot.com",
  'messagingSenderId': "643426977084",
  'appId': "1:643426977084:web:8349da1abceb4c837f8a39",
  'measurementId': "G-VL0MLCR1YH"
}

# Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database
db = firebase.database()
storage = firebase.storage()
with st.sidebar:
 lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_6qyxpnwe.json")
 st_lottie(lottie_coding,height= 150,key = "caring")


st.sidebar.title("多动能一体检测用程序/All in one Detection")
#st.title("多动能一体检测用程序/All In One  Detection App")
  
# Authentication
choice = st.sidebar.selectbox('登录:login/注册:Signup', ['Login', 'Sign up'])
#choice = st.selectbox('登录:login/注册:Signup', ['Login', 'Sign up'])

   
# Obtain User Input for email and password
email = st.sidebar.text_input('输入邮件Please enter your email address📩')
password = st.sidebar.text_input('输入密码/Please enter your password🔐', type='password')
#email = st.text_input('输入邮件/Please enter your email address')
#password = st.text_input('输入密码/Please enter your password', type='password')



# Sign up Block
if choice == 'Sign up':
    handle = st.sidebar.text_input(
    'Please input your app name', value='Default')
    submit = st.sidebar.button('注册Create my account🧾')
   # handle = st.text_input(
    #'Please input your app handle name', value='Default')
    #submit = st.button('注册/Create my account')


    if submit:
        user = auth.create_user_with_email_and_password(email, password)
        st.success('注册成功/Your account is created suceesfully!📩')
        st.balloons()
        # Sign in
        user = auth.sign_in_with_email_and_password(email, password)
        db.child(user['localId']).child("Handle").set(handle)
        db.child(user['localId']).child("ID").set(user['localId'])
        st.title('Welcome' + handle)
        st.info('通过登录下拉列表和选择登录Login via login drop down selection🔑')

# Login Block
if choice == 'Login':
    login = st.sidebar.checkbox('登录/Login')
    #login = st.checkbox('登录/Login')

if login:
 user = auth.sign_in_with_email_and_password(email, password)
 st.write("---")
 st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
 bio = st.radio('Explore Now:', ['Home Page🏛️','Profile And Moments👨','Find Friends👯','设置和自己定义/Settings And Customization⚙️','Contact Us Page🤝','Self Test Page🩺'])

 if bio=="Home Page🏛️":
    st.write("Before jumping to self test page ,first you can study on how to do it using information given below:")
    df = pd.DataFrame({'Pregnances': [5, 3, 10, 2,8],
                   'Glucose': [116, 78, 115, 197, 125],
                   'Skin Thickness': [0, 32, 0, 45, 0],
                   'Insulin': [0, 88, 0, 543, 0],
                   'DiabetesPedigree': [0.201, 0.248, 0.134, 0.158,0.232],
                   'BMI': [25.6, 31, 35.3, 30.5, 0],
                   'AGE': [30, 26, 29, 67, 50],
                   'Blood Pressure': [74, 50, 0, 70, 96]})
                   
    st.subheader('Diabetes(糖尿病)')
    st.dataframe(df)

    df = pd.DataFrame({'Age': [54, 48, 49, 64,58],
                   'Sex': [1, 0, 1, 1, 0],
                   'CP': [0, 2, 1, 3, 3],
                   'trestbps': [140, 130, 130, 110, 150],
                   'chol': [239, 275, 266, 211,283],
                   'fbs': [0, 0, 0, 0, 1],
                   'exang': [0, 0, 0, 1, 0],
                   'oldpeak': [1.2, 0.2, 0.6, 1.8, 1],
                   'slope': [2, 2, 2, 1, 2],
                   'ca': [0, 0, 0,0, 0],
                   'thal': [2, 2, 2, 2, 2],
                   'targert': [1, 1, 1, 1, 1],
                   'thalach': [160, 139, 171, 144, 162]})
                   
    st.subheader('Heart(心脏)')
    st.dataframe(df)


    df = pd.DataFrame({'MDVP:Fo(Hz)': [88.333, 91.904, 136.926, 139.173,152.845],
                   'MDVP:Fhi(Hz)': [112.24, 115.871,159.866, 179.139, 163.305],
                   'MDVP:Flo(Hz)': [84.072, 86.292, 131.276, 76.556, 75.836],
                   'MDVP:Jitter(%)': [0.00505, 0.0054, 0.00293, 0.0039, 0.00294],
                   'MDVP:Jitter(Abs)': [0.00006, 0.00006, 0.00002, 0.00003,0.00002],
                   'MDVP:RAP': [0.00254, 0.00281, 0.00118,0.00165, 0.00121],
                   'MDVP:PPQ': [0.0033, 0.00336, 0.00153, 0.00208, 0.00149],
                   'Jitter:DDP': [0.00763, 0.00844, 0.00355, 0.00496, 0.00364],
                   'MDVP:Shimmer': [0.02143, 0.02752, 0.01259, 0.01642, 0.01828],
                   'MDVP:Shimmer(dB)': [0.197, 0.249, 0.112, 0.154, 0.158],
                   'Shimmer:APQ3': [0.01079, 0.01424, 0.00656, 0.00728, 0.01064],
                   'Shimmer:APQ5': [0.01342, 0.01641, 0.00717, 0.00932, 0.00972],
                   'Shimmer:DDA': [0.03237, 0.04272, 0.01968, 0.02184, 0.03191],
                   'NHR': [0.01166, 0.01141, 0.00581, 0.01041, 0.00609],
                   'NHR': [21.118, 21.414, 25.703, 24.889, 24.922],
                   'status': [1, 1, 1, 1, 1],
                   'RPDE': [0.611137, 0.58339, 0.4606, 0.430166, 0.474791],
                   'DFA': [0.776156, 0.79252, 0.646846, 0.665833, 0.654027],
                   'spread1': [-5.24977, -4.960234, -6.547148, -5.660217, -6.105098],
                   'spread2': [0.391002, 0.363566, 0.152813, 0.254989, 0.203653],
                   'D2': [2.407313, 2.642476,2.041277,2.519422, 2.125618],
                   'PPE': [0.24974, 0.275931, 0.138512, 0.199889, 0.1701],
                   'MDVP:APQ': [0.01892, 0.02214, 0.0114, 0.01797, 0.01246]})
                   
    st.subheader('Parkinsons(帕金森病)')
    st.dataframe(df)
		
        # SETTINGS PAGE
 if bio == '设置和自己定义/Settings And Customization⚙️':
            # CHECK FOR IMAGE
            nImage = db.child(user['localId']).child("Image").get().val()
            # IMAGE FOUND
            if nImage is not None:
                # We plan to store all our image under the child image
             Image = db.child(user['localId']).child("Image").get()
             for img in Image.each():
                    img_choice = img.val()
                    # st.write(img_choice)
                    st.image(img_choice)
                    exp = st.beta_expander('改变图像/Change Bio and Image')
                # User plan to change profile picture
                    with exp:
                      newImgPath = st.text_input('输入图像的完整路径/Enter full path of your profile image')
                      upload_new = st.button('上装/Upload')
                    if upload_new:
                        uid = user['localId']
                        fireb_upload = storage.child(uid).put(newImgPath, user['idToken'])
                        a_imgdata_url = storage.child(uid).get_url(fireb_upload['downloadTokens'])
                        db.child(user['localId']).child("Image").push(a_imgdata_url)
                        st.success('成功/Success!')
                        # IF THERE IS NO IMAGE
                        # 
            else:
                st.info("No profile picture yet")
                newImgPath = st.text_input('输入图像的完整路径/Enter full path of your profile image')
                upload_new = st.button('上装/Upload')
            if upload_new:
               uid = user['localId']
                    # Stored Initated Bucket in Firebase
               fireb_upload = storage.child(uid).put(newImgPath, user['idToken'])
                    # Get the url for easy access
               a_imgdata_url = storage.child(uid).get_url(fireb_upload['downloadTokens'])
                    # Put it in our real time database
               db.child(user['localId']).child("Image").push(a_imgdata_url)
        # HOME PAGE
 elif bio == 'Profile And Moments👨':
            st.write("---")
            col1, col2 = st.columns(2)

        # col for Profile picture
            with col1:
                nImage = db.child(user['localId']).child("Image").get().val()
            if nImage is not None:
               val = db.child(user['localId']).child("Image").get()
               for img in val.each():
                img_choice = img.val()
                st.image(img_choice, use_column_width=True)
            else:
                st.info("还没有个人资料图片/No profile picture yet. Go to settings and choose one!")

                post = st.text_input("分享或发布你当前的心情/Share and Post Your Current Mood!", max_chars=100)
                add_post = st.button('Share Posts')
            if add_post:
                      now = datetime.now()
                      dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                      post = {'Post:': post,
                      'Timestamp': dt_string}
                      results = db.child(user['localId']).child("Posts").push(post)
                      st.balloons()

        # This coloumn for the post Display

 
            with col2:
             all_posts = db.child(user['localId']).child("Posts").get()

            if all_posts.val() is not None:
             for Posts in reversed(all_posts.each()):
                st.write(Posts.key()) # Morty
                st.code(Posts.val(), language='')
        # WORKPLACE FEED PAGE
 
                all_users = db.get()
                res = []
            # Store all the users handle name
             for users_handle in all_users.each():
                    k = users_handle.val()["Handle"]
                    res.append(k)
            # Total   users
                    nl = len(res)
                    st.write('Number Of Users In Use Of The App: ' + str(nl))

            # Allow the user to choose which other user he/she wants to see
                    choice = st.selectbox('Friends In Circle', res)
                    push = st.button('Show Profile/显示配置文件')


            # Show the chosen Profile
                    if push:
                     for users_handle in all_users.each():
                        k = users_handle.val()["Handle"]
                    if k == choice:
                       lid = users_handle.val()["ID"]

                       handlename = db.child(lid).child("Handle").get().val()

                       st.markdown(handlename, unsafe_allow_html=True)

                       nImage = db.child(lid).child("Image").get().val()
                    if nImage is not None:
                       val = db.child(lid).child("Image").get()
                       for img in val.each():
                         img_choice = img.val()
                         st.image(img_choice)
                    else:
                     st.info("还没有个人资料图片/No profile picture yet. Go to Edit Profile and choose one!")

                        # All posts
                     all_posts = db.child(lid).child("Posts").get()
                    if all_posts.val() is not None:
                      for Posts in reversed(all_posts.each()):
                       st.code(Posts.val(), language='')


 if bio == "Contact Us Page🤝":
            st.write("----")
            #st.title(f"you have selected{selected}")
            st.markdown(""" <style> .font {
                        font-size:35px ; font-family: 'Cooper Black'; color: blue;} 
                        </style> """, unsafe_allow_html=True)
            st.markdown('<p class="font">Get In Touch with ChecknChat-App Team:</p>', unsafe_allow_html=True)
            contact_form = """
                     <input type = "hidden" name = " _capture" value = "false">
                     <form action="https://formsubmit.co/chototakudzwa8@gmail.com" method="POST">
                     <input type="text" name="name" placeholder = "Your name" required>
                     <input type="email" name="email" placeholder = "Your email" required>
                     <input type = "text" name = "company" placeholder = "Your company" required >
                     <textarea  name = "message" placeholder = "Enter message" required></textarea>
                     <button type="submit">Send</button>
                </form>

                     """

            st.markdown(contact_form, unsafe_allow_html=True)
          
#-----------------------------------------------------------------------------------------------------
 if bio == 'Self Test Page🩺':
    st.write("---")
    # loading the saved models
    diabetes_model = pickle.load(open(r'diabetes_model.sav','rb'))

    heart_disease_model = pickle.load(open(r'heart_disease_model.sav','rb'))

    parkinsons_model = pickle.load(open(r'parkinsons_model.sav','rb'))

        # sidebar for navigation

    bio = option_menu(menu_title=None ,options=
      ['Diabetes Prediction',
      'Heart Disease Prediction',
      'Parkinsons Prediction'],
       icons=['activity', 'heart', 'person'],
       default_index=0,orientation="horizontal")


                                
    styles={
        "container ": {"padding": "0!important", "background-color": "white"},
                           "icon": {"color": "blue", "font-size": "25px"},
                           "nav-link": {
                            "font-size": "25px",
                            "text-align": "left",
                            "margin": "0px",
                             "--hover-color": "blue",

                             },
                             "nav-link-selected": {"background-color": "blue"},
                               }


                            
    # loading the saved models
    diabetes_model = pickle.load(open(r'diabetes_model.sav','rb'))

    heart_disease_model = pickle.load(open(r'heart_disease_model.sav','rb'))

    parkinsons_model = pickle.load(open(r'parkinsons_model.sav','rb'))
                    
# Diabetes Prediction Page
    if (bio == 'Diabetes Prediction'):

    # page title
                              st.title('糖尿病的机器学习检测/Machine Learning Based Detection For Diabetes')

    # getting the input data from the user
                              col1, col2, col3 = st.columns(3)

                              with col1:
                                  Pregnancies = st.text_input('Number of Pregnancies')

                              with col2:
                                  Glucose = st.text_input('Glucose Level')

                              with col3:
                                  BloodPressure = st.text_input('Blood Pressure value')

                              with col1:
                                 SkinThickness = st.text_input('Skin Thickness value')

                              with col2:
                                Insulin = st.text_input('Insulin Level')

                              with col3:
                                 BMI = st.text_input('BMI value')

                              with col1:
                                   DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

                              with col2:
                                    Age = st.text_input('Age of the Person')

    # code for Prediction
                                    diab_diagnosis = ''

    # creating a button for Prediction

                              if st.button('Diabetes Test Result/查结果'):
                                 diab_prediction = diabetes_model.predict(
                                 [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
                                  
                                  

                                 if (diab_prediction[0] == 1):
                                   diab_diagnosis = '这个人受到影响/The person is diabetic'
                                   st.warning(diab_diagnosis)
                                 else:
                                   diab_diagnosis = '这个人没受到影响/The person is not diabetic'
                                   st.success(diab_diagnosis)

# Heart Disease Prediction Page
    if (bio == 'Heart Disease Prediction'):

    # page title
                                st.title('基于机器学习的心脏病预测/Heart Disease Prediction based on Machine Learning')

                                col1, col2, col3 = st.columns(3)

                                with col1:
                                     age = st.text_input('Age')

                                with col2:
                                     sex = st.text_input('Sex')

                                with col3:
                                     cp = st.text_input('Chest Pain types')

                                with col1:
                                    trestbps = st.text_input('Resting Blood Pressure')

                                with col2:
                                    chol = st.text_input('Serum Cholestoral in mg/dl')

                                with col3:
                                    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

                                with col1:
                                    restecg = st.text_input('Resting Electrocardiographic results')

                                with col2:
                                    thalach = st.text_input('Maximum Heart Rate achieved')

                                with col3:
                                    exang = st.text_input('Exercise Induced Angina')

                                with col1:
                                    oldpeak = st.text_input('ST depression induced by exercise')

                                with col2:
                                    slope = st.text_input('Slope of the peak exercise ST segment')

                                with col3:
                                    ca = st.text_input('Major vessels colored by flourosopy')

                                with col1:
                                    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
                                    heart_diagnosis = ''

    # creating a button for Prediction

                                if st.button('Heart Disease Test Result'):
                                    heart_prediction = heart_disease_model.predict(
                                    [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

                                    if (heart_prediction[0] == 1):
                                       heart_diagnosis = '这个人受到影响/The person is having heart disease'
                                       st.warning(heart_diagnosis)
                                    else:
                                       heart_diagnosis = '这个人没受到影响/The person does not have any heart disease'
                                       st.success(heart_diagnosis)

# Parkinson's Prediction Page
    if (bio == "Parkinsons Prediction"):

    # page title
                                st.title("基于机器学习的帕金森病预测/Parkinson's Disease Prediction Based On Machine Learning")

                                col1, col2, col3, col4, col5 = st.columns(5)

                                with col1:
                                      fo = st.text_input('MDVP:Fo(Hz)')

                                with col2:
                                    fhi = st.text_input('MDVP:Fhi(Hz)')

                                with col3:
                                        flo = st.text_input('MDVP:Flo(Hz)')

                                with col4:
                                   Jitter_percent = st.text_input('MDVP:Jitter(%)')

                                with col5:
                                           Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

                                with col1:
                                   RAP = st.text_input('MDVP:RAP')

                                with col2:
                                    PPQ = st.text_input('MDVP:PPQ')

                                with col3:
                                   DDP = st.text_input('Jitter:DDP')

                                with col4:
                                    Shimmer = st.text_input('MDVP:Shimmer')

                                with col5:
                                           Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

                                with col1:
                                         APQ3 = st.text_input('Shimmer:APQ3')

                                with col2:
                                       APQ5 = st.text_input('Shimmer:APQ5')

                                with col3:
                                       APQ = st.text_input('MDVP:APQ')

                                with col4:
                                             DDA = st.text_input('Shimmer:DDA')

                                with col5:
                                        NHR = st.text_input('NHR')

                                with col1:
                                   HNR = st.text_input('HNR')

                                with col2:
                                       RPDE = st.text_input('RPDE')

                                with col3:
                                           DFA = st.text_input('DFA')

                                with col4:
                                  spread1 = st.text_input('spread1')

                                with col5:
                                         spread2 = st.text_input('spread2')

                                with col1:
                                    D2 = st.text_input('D2')

                                with col2:
                                    PPE = st.text_input('PPE')

    # code for Prediction
                                    parkinsons_diagnosis = ''

    # creating a button for Prediction
                                if st.button("Parkinson's/Brain Test Result"):
                                      parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
                                                           Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE,
                                                           DFA, spread1, spread2, D2, PPE]])

                                      if (parkinsons_prediction[0] == 1):

                                       parkinsons_diagnosis = "这个人受到影响/The person has Parkinson's/Brain disease"
                                       st.warning(parkinsons_diagnosis)
                                      else:
                                       parkinsons_diagnosis = "这个人没受到影响/The person does not have Parkinson's/Brain disease"
                                       st.success(parkinsons_diagnosis)


#-----------------------------------------------------------------------------------------------------------
lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_bsPjV4.json")
lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/private_files/lf30_P2uXE5.json")

st.write("------")
footer="""<style>
a:link , a:visited{
color: white;
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: none;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color:#5486ea ;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed and Built By 赵多多Takudzwa Gershom Choto <a style='display: block; text-align: center;'href="https://github.com/TakudzwaChoto" target="_blank">人工智能创新实验@遵义师范学院(Zunyi Normal University)</a></p>
</div>

"""
st.markdown(footer,unsafe_allow_html=True)
          
                   