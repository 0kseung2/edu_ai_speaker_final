import time, os
import speech_recognition as sr
from gtts import gTTS
import requests
import openai
from ctypes import*

# 음성 인식 (듣기, STT)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[사용자] ' + text)
        answer(text)
    except sr.UnknownValueError: #음성 인식 실패한 경우
        print('인식 실패')
        text = input()
        answer(text) 
    except sr.RequestError as e:
        print('요청 실패 :{0}'.format(e)) #API Key 오류, 네트워크 단절 등

# 게임 진행 텍스트
# Rock_Paper_Scissors_txt = open("가위바위보 게임.txt", "r", encoding='UTF8')
# Rock_Paper_Scissors_ment = Rock_Paper_Scissors_txt.read()


# 대답
def answer(input_text):
    answer_text = ''
    if '게임' in input_text:
        if '가위바위보' in input_text:
            # answer_text = Rock_Paper_Scissors_ment
            answer_text = '가위바위보 게임을 진행하겠습니다. 게임은 삼 세판으로 진행하겠습니다. 안 내면 진다 가위바위보! 누가 이기셨나요 ? 이기신 분 축하드립니다. 다시 한번 가위바위보! 같은 분이 두번 이기셨다면 AI 스피커에 종료해달라고 말씀해주세요. 그렇지 않다면 다시 진행하겠습니다. 안 내면 진다. 가위바위보!'
        elif '만두' in input_text:
            answer_text = '만두 게임을 진행하겠습니다. 게임은 삼 세판으로 진행하겠습니다. 숫자를 셀게요. 하나 둘 셋 시작. 만두. 만두. 만두. 만두! 한번더! 만두. 만두. 만두. 만두! 한번더! 만두. 만두. 만두. 만두!'
    
    elif '수학' in input_text:
        if '학습관리' in input_text:
            answer_text = '수학 50분 학습관리 3초 후에 시작합니다 3!2!1! 파이팅!'
        elif '학습 관리' in input_text:
            answer_text = '수학 50분 학습관리 3초 후에 시작합니다 3!2!1  파이팅!'

    elif '10초' in input_text:
        time.sleep(10)
        answer_text = '현재 남은 시간은 49분 20초입니다.'

    elif '15초' in input_text:
        time.sleep(15)
        answer_text = '15초가 지났습니다. 다시 학습을 시작하겠습니다'

    elif '마음이' in input_text:
        answer_text = "마음이 힘들 때는 잠시 하던 것을 내려두고 산책을 가는 건 어떨까요. 자연 속에서 바람을 쐬고, 풍경을 감상한다면 마음이 편안해질 수 있을 거에요. 저는 당신을 응원합니다"

    elif '우울해' in input_text:
        answer_text = "당신에게 너무 많은 짐이 쌓여있는 것 같아요. 잠시 스스로에게 준 부담을 내려놓고, 자신을 편안하게 만들 수 있는 행동을 하는 건 어떨까요?"

    elif '자습 종료' in input_text:
        answer_text = "우리 아들 공부하느라 수고 많았어. 사랑해~"

    elif '자습종료' in input_text:
        answer_text = "우리 아들 공부하느라 수고 많았어. 사랑해~"    

    elif '궁금' in input_text:
        openai.api_key = "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"

        completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role":"user", "content":input_text}]
        )

        answer_text = completion.choices[0].message.content
    
    # elif '종료' in input_text:
    #     answer_text = '다음에 또 만나요'       
    #     stop_listening(wait_for_stop=False) # 더 이상 듣지 않음

    else:
        answer_text = '다시 한번 말씀해주시겠어요?'
    
    speak(answer_text)
    

# 소리내어 읽기 (TTS)
def speak(text):
    print('[AI 스피커] ' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    os.system('mpg123 ' + file_name)
    if os.path.exists(file_name): #voice.mp3 파일 삭제
        os.remove(file_name)

r = sr.Recognizer()
m = sr.Microphone()

speak('무엇을 도와드릴까요?')
stop_listening = r.listen_in_background(m, listen)
#stop_listening(wait_for_stop=False) # 더 이상 듣지 않음

while True:
    time.sleep(0.1)


