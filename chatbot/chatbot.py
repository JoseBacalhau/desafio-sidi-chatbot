import requests
from pymongo import MongoClient

# Função para fazer uma requisição GET ao back-end
def make_request(url):
    response = requests.get(url)
    return response.json()

# Função para validar as respostas do usuário
def validate_answer(answer):
    return answer.lower() == 'sim'

def get_user_input(prompt, options=None, max_attempts=3):
    for _ in range(max_attempts):
        user_input = input(prompt)
        if options is not None and user_input.upper() not in options:
            print("Digite uma opção válida.")
            print("Você tem mais", max_attempts - (_ + 1), "tentativa(s).")
        else:
            return user_input
    print("Você excedeu o número máximo de tentativas. O chatbot será encerrado.")
    return None

def chatbot_flow():
    print("Início")

    print("Olá. Seja bem-vindo ao chatbot do SiDi. Qual o código da vaga?")
    job_id = input()

    # Requisição ao back-end para verificar a existência da vaga
    url = f"http://localhost:5000/check_job_id/{job_id}"
    response = make_request(url)

    if response == {'job': None}:
        print("A vaga não existe. Você tem mais 2 tentativas.")
        # Mais 2 tentativas para digitar o código da vaga
        for _ in range(2):
            job_id = input()
            url = f"http://localhost:5000/check_job_id/{job_id}"
            response = make_request(url)
            if response == {'job': None}:
                print("A vaga não existe. Você tem mais", 1 - _, "tentativa(s).")
            else:
                job_value = response['job']
                print("A vaga existe", job_value)
                print("Vamos continuar.")
                break
        else:
            print("Você excedeu o número máximo de tentativas. O chatbot será encerrado.")
            return
    else:
        job_value = response['job']
        print("A vaga existe", job_value)
        print("Vamos continuar.")
    
    # Perguntas Eliminatórias
    elimination_questions = []
    elimination_answers = []  # List to store elimination question answers
    for i in range(1, 4):
        url = f"http://localhost:5000/get_job_messages/{i}"
        response = make_request(url)
        elimination_question = response['jobmessages']
        elimination_questions.append(elimination_question)

        prompt = f"{elimination_question}\n"
        answer = get_user_input(prompt, options=["SIM", "NÃO"])
        if answer is None:
            return
        elif answer.upper() == "NÃO":
            print("Esse conhecimento é obrigatório para essa vaga. Tente outras vagas disponíveis.")
            return
        else:
            print("Resposta Registrada!")
            elimination_answers.append(answer.upper())  # Store the answer
    
    # Perguntas Obrigatórias
    mandatory_questions = []
    mandatory_answers = []  # List to store mandatory question answers
    for i in range(4, 8):
        url = f"http://localhost:5000/get_job_messages/{i}"
        response = make_request(url)
        mandatory_question = response['jobmessages']
        mandatory_questions.append(mandatory_question)

        prompt = f"{mandatory_question}\n"
        answer = get_user_input(prompt)
        if answer is None:
            return
        else:
            print("Resposta Registrada!")
            mandatory_answers.append(answer.upper())  # Store the answer

    # Confirmação da Vaga
    prompt = "Confirmar aplicação da vaga? (SIM ou NÃO)\n"
    answer = get_user_input(prompt, options=["SIM", "NÃO"])
    if answer is None:
        return

    if validate_answer(answer):
        print("Preencher formulário GUPY")
        print("Sua candidatura a vaga foi registrada com sucesso. Obrigado por participar. :D")

        # Armazenar a resposta no MongoDB
        client = MongoClient('localhost', 27017)
        db = client['Chatbot']
        collection = db['respostas']

        resposta = {
            'Cargo': job_value ,
            elimination_questions[0]: elimination_answers[0],
            elimination_questions[1]: elimination_answers[1],
            elimination_questions[2]: elimination_answers[2],
            mandatory_questions[0]: mandatory_answers[0],
            mandatory_questions[1]: mandatory_answers[1],
            mandatory_questions[2]: mandatory_answers[2],
            mandatory_questions[3]: mandatory_answers[3],
            'Você quer candidatar-se a vaga ?': answer.upper()
        }

        collection.insert_one(resposta)
    else:
        print("Confirmada sua desistência da vaga.")

chatbot_flow()
