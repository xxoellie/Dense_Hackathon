import streamlit as st
from PIL import Image
from playsound import playsound

st.set_option('deprecation.showfileUploaderEncoding', False) # deprecation 표시 안함
st.markdown("<h1 style='text-align: center; '>자네! 분리수거 어디까지 해봤나?</h1>", unsafe_allow_html=True)
# st.title("자네 분리수거 어디까지 해봤나")
st.markdown("<h5 style='text-align: center; color: red; '>쓰레기 분리수거만 잘해도 연간 100억원을 절감할 수 있습니다.</h5>", unsafe_allow_html=True)


image2 = Image.open('image.png')
st.image(image2, caption='분리수거 판독 서비스',use_column_width=True)


st.write("")
st.write("")
st.markdown("<h5 style='text-align: center;'>***이미지 분류를 위해 분리수거할 사진을 업로드 해 주세요***</h5>", unsafe_allow_html=True)

# st.text("***이미지 분류를 위해 분리수거할 사진을 업로드 해 주세요***")
#Streamlit 파일 처리 및 결과

st.write("")
st.write("")

from PIL import Image, ImageOps
from img_classification import machine_classification
uploaded_file = st.file_uploader("분리수거 할 사진을 업로드 해 주세요.", type=['jpeg', 'png', 'jpg', 'webp'])
if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Trash Image.', use_column_width=True)
        st.write("")
        st.write("처리중입니다...")
        label = machine_classification(image, 'keras_model.h5')
        if label == 0 :
            st.write("***결과 : 폐건전지는 중금속이 함유되어 있습니다. 함부로 버리면 그 중금속이 당신의 몸으로 들어갑니다.***")
            playsound('battery.mp3')
        elif label == 1 :
            st.write("***결과 : 계란껍질은 일반쓰레기입니다. 음식물쓰레기가 아닙니다.***")
            playsound('egg.mp3')
        elif label == 2 :
            st.write("***결과 : 과일포장재는 일반쓰레기입니다. 재활용이 불가능해요. ***")
            playsound('fruit.mp3')
        elif label == 3 :
            st.write("***결과 : 밤껌질은 일반쓰레기입니다. 귀찮더라도 음식물에 버리지 말아주세요.***")
            playsound('bam.mp3')
        elif label == 4 :
            st.write("***결과 : 부탄가스는 구멍을 뚫어 가스가 빠져나오게 해줍니다. 가스가 거의 다 빠져나오면 송곳이나 와인 따개, "
                     "부탄가스 전용 펀치를 이용해서 용기 옆쪽에 구멍을 2~3개 뚫어줍니다. 구멍 낸 가스통을 뒤집어서 10분간 세워두면 가스가 "
                     "모두 제거되는데요. 빈 통은 캔 류로 분리 배출하면 됩니다. ***")
            playsound('butangas.mp3')
        elif label == 5 :
            st.write("***결과 : 빨대는 일반쓰레기입니다. 자그마한 플라스틱 제품은 일반쓰레기로 버려주세요. ***")
            playsound('straw.mp3')
        elif label == 6 :
            st.write("***결과 : 스티로폼은 스티로폼에 버려주세요***")
            playsound('stiroprom.mp3')
        elif label == 7 :
            st.write("***결과 : 스프링노트는 스프링을 분리하여 금속에 분리수거하고 종이는 종이에 버려주세요***")
            playsound('note.mp3')
        elif label == 8 :
            st.write("***결과 : 식용유 용기는 플라스틱에 기름은 기름수거함에 버려주세요. 음식물이 아닙니다!!!!!!***")
            playsound('oil.mp3')
        elif label == 9 :
            st.write("***결과 : 아이스팩 내용물은 일반쓰레기에 버려주세요. 비닐은 비닐에 분리수거해주세요.ㅠㅠ***")
            playsound('icepack.mp3')
        elif label == 10 :
            st.write("***결과 : 견과류 껍질은 일반쓰레기입니다.***")
            playsound('nut.mp3')
        elif label == 11 :
            st.write("***결과 : 양파/마늘 껍질은 일반쓰레기에 버려주세요.***")
            playsound('onion.mp3')
        elif label == 12 :
            st.write("***결과 : 살충제 용기는 구멍을 뚫어 캔에 넣어주세요. 폭파의 위험이 있습니다. ***")
            playsound('fkila.mp3')
        elif label == 13 :
            st.write("***결과 : 우유팩은 내용물을 버린 후 깨끗이 씻어 말려서 압축해서 우유팩 수거함에 버려주세요***")
            playsound('milk.mp3')
        elif label == 14 :
            st.write("***결과 : 유리는 유리에 분리수거 해주세요. 깨진 유리는 종량제 봉투에 담아서 버려주세요. ***")
            playsound('glass.mp3')
        elif label == 15 :
            st.write("***결과 : 조개껍질은 일반쓰레기에요. 음식물이 아닙니다 동물의 사료로 만들수 없어요ㅠㅠ***")
            playsound('shell.mp3')
        elif label == 16 :
            st.write("***결과 : 종이는 종이에 분류해주세요.***")
            playsound('paper.mp3')
        elif label == 17 :
            st.write("***결과 : 종이상자는 펴서 종이끼리 모아주세요***")
            playsound('papebox.mp3')
        elif label == 18 :
            st.write("***결과 : 동물의 뼈는 일반쓰레기에요 음식물에 버리면 안됩니다***")
            playsound('bone.mp3')
        elif label == 19 :
            st.write("***결과 : 깨끗이 씻어서 캔에 넣어주세요***")
            playsound('can.mp3')
        elif label == 20 :
            st.write("***결과 : 컵라면용기는 일반쓰레기~ 플라스틱으로 재활용이 안됩니다!! ***")
            playsound('cupramen.mp3')
        elif label == 21 :
            st.write("***결과 : 플라스틱은 플라스틱에~ 단! 비닐은 포장재와 분리해서 버려주세요***")
            playsound('plastic.mp3')
        elif label == 22 :
            st.write("***결과 : 플라스틱 숟가락은 재활용이 안되니 일반쓰레기로 버려주세요***")
            playsound('spoon.mp3')
        elif label == 23 :
            st.write("***결과 : 햇반용기는 일반쓰레기입니다! 밥풀은 깨끗이 닦아주실꺼죠?***")
            playsound('rice.mp3')
        elif label == 24 :
            st.write("***결과 : 형광등 수거함에 쏘옥 넣어주세요***")
            playsound('light.mp3')
        elif label == 25 :
            st.write("***결과 : 테이크 아웃 용기는 플라스틱 빨대는 일반쓰레기 슬리브는 종이에 넣어주세요 뿌잉뿌잉***")
            playsound('takeoutcup.mp3')
        elif label == 26 :
            st.write("***결과 : 비닐은 비닐에 넣어주시면 감사하겠습니다***")
            playsound('vinly.mp3')
        elif label == 27 :
            st.write("***결과 : 과자봉지는 비닐에 넣어주세요 딱지로 접어서 딱지치기 하면 안돼요***")
            playsound('snack.mp3')
        elif label == 28 :
            st.write("***결과 : 플라스틱은 깨끗이 씻어서 플라스틱에 슝하고 넣어주세요. 비닐은 따로 분류하기로 약속!!***")
            playsound('pet.mp3')
        elif label == 30 :
            st.write("***결과 : 종이컵은 종이가 아니라 종이컵 수거함에 넣어주셔야 되요 근데 일회용품은 안쓰면 좋겠어요***")
            playsound('papercup.mp3')
        else:
            st.write("***결과 : 다시 촬영해주세요.***")