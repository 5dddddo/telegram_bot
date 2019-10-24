from flask import Flask,render_template,request
from decouple import config
import requests,random
app = Flask(__name__)

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id=config('CHAT_ID')

@app.route('/')
def hello_world():
    return 'Helo World!'


# 텔레그램 서버가 우리 서버에게 HTTP POST 요청을 통해,
# 사용자 메시지 정보를 받으라고 전달해 줌
# 설정이 되어 있는 것! -> GET으로 바꿀 수 없음

# 우리가 status 200을 리턴해줘야 텔레그램이 데이터 전송을 중단함
# 200을 안 보내주면 텔레그램측에서 계속해서 POST 요청을 보냄

# https://ngrok.com/ : 로컬 호스트 주소를 Public 주소로 바꿔줌
# 다른 사람이 나의 로컬 호스트 주소로 접근할 수 있게 됨
@app.route(f'/{token}',methods=['POST'])
def telegram():
    # 1. 메아리 기능
    # 1.1 request.get_json() 구조 확인하기
    print(request.get_json())

    # 1.2 사용자 아이디, 텍스트 가져오기

    chat_id = request.get_json().get('message').get('from').get('id')
    text = request.get_json().get('message').get('text')
    # 1.3 텔레그램 API에게 요청을 보내서 답변해주기
    
    # requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    
    if text == '/로또':
        lotto = sorted(random.sample(range(1,46),6))
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={lotto}')
    if text[0:8] == '/vonvon ':
        name = text[9:]
        first_list = ['매우못생김', '못생김', '서혁진얼굴', '머존잘', '우주꼴등얼굴', '꼼장어', '오징어외모', '배추김치얼굴']
        second_list = ['자신감','귀찮음','쑥스러움','열정적임','하찮음']
        third_list = ['허세','물욕','식욕','똘기','폭풍섹시']
        first = random.choice(first_list)
        second = random.choice(second_list)
        third = random.choice(third_list)
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={name}님은 {first}, {second}, {third}')

    return '',200


@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('message')
    requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return '<h1>메시지전송완료</h1>'

if __name__ == '__main__':
    app.run(debug=True)
