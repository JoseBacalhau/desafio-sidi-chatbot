import pymongo
import requests

from pymongo import MongoClient

# Função para fazer uma requisição GET ao back-end
def make_request(url):
    response = requests.get(url)
    return response.json()

# Função para validar as respostas do usuário
def validate_answer(answer):
    return answer.lower() == 'sim'

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
    
    # Requisição ao back-end para receber a primeira Pergunta Eliminatória
    url = "http://localhost:5000/get_job_messages/1"
    response = make_request(url)
    EliminationQuestion1 = response['jobmessages']
    print(f"{EliminationQuestion1}")
    EliminatoryAnswer1 = input()
    if EliminatoryAnswer1.upper() != "SIM" and EliminatoryAnswer1.upper() !="NÃO":
        print("Você não está escrevendo corretamente! Você tem mais 2 tentativas.")
        for _ in range(2):
            EliminatoryAnswer1 = input()
            if EliminatoryAnswer1.upper() != "SIM" and EliminatoryAnswer1.upper() !="NÃO":
                print("Digite Corretamente. Você tem mais", 1 - _, "tentativa(s).")
            elif EliminatoryAnswer1.upper() == "NÃO":
                print("Esse conhecimento é obrigatório para essa vaga. Tente outras vagas disponíveis.")
                return
            else:
                print("Agora vocÊ digitou corretamente!")
                print("Vamos continuar.")
                break
        else:
            print("Você excedeu o número máximo de tentativas. O chatbot será encerrado.")
            return
    elif EliminatoryAnswer1.upper() == "NÃO":
        return
    else:
        print("Resposta Registrada!")
    
    # Requisição ao back-end para receber a Segunda Pergunta Eliminatória
    url = "http://localhost:5000/get_job_messages/2"
    response = make_request(url)
    EliminationQuestion2 = response['jobmessages']
    print(f"{EliminationQuestion2}")
    EliminatoryAnswer2 = input()
    if EliminatoryAnswer2.upper() != "SIM" and EliminatoryAnswer2.upper() !="NÃO":
        print("Você não está escrevendo corretamente! Você tem mais 2 tentativas.")
        for _ in range(2):
            EliminatoryAnswer2 = input()
            if EliminatoryAnswer2.upper() != "SIM" and EliminatoryAnswer2.upper() !="NÃO":
                print("Digite Corretamente. Você tem mais", 1 - _, "tentativa(s).")
            elif EliminatoryAnswer2.upper() == "NÃO":
                print("Esse conhecimento é obrigatório para essa vaga. Tente outras vagas disponíveis.")
                return
            else:
                print("Agora vocÊ digitou corretamente!")
                print("Vamos continuar.")
                break
        else:
            print("Você excedeu o número máximo de tentativas. O chatbot será encerrado.")
            return
    elif EliminatoryAnswer2.upper() == "NÃO":
        return
    else:
        print("Resposta Registrada!")

    # Requisição ao back-end para receber a Terceira Pergunta Eliminatória
    url = "http://localhost:5000/get_job_messages/3"
    response = make_request(url)
    EliminationQuestion3 = response['jobmessages']
    print(f"{EliminationQuestion3}")
    EliminatoryAnswer3 = input()
    if EliminatoryAnswer3.upper() != "SIM" and EliminatoryAnswer3.upper() !="NÃO":
        print("Você não está escrevendo corretamente! Você tem mais 2 tentativas.")
        for _ in range(2):
            EliminatoryAnswer3 = input()
            if EliminatoryAnswer3.upper() != "SIM" and EliminatoryAnswer3.upper() !="NÃO":
                print("Digite Corretamente. Você tem mais", 1 - _, "tentativa(s).")
            elif EliminatoryAnswer3.upper() == "NÃO":
                print("Esse conhecimento é obrigatório para essa vaga. Tente outras vagas disponíveis.")
                return
            else:
                print("Agora vocÊ digitou corretamente!")
                print("Vamos continuar.")
                break
        else:
            print("Você excedeu o número máximo de tentativas. O chatbot será encerrado.")
            return
    elif EliminatoryAnswer3.upper() == "NÃO":
        return
    else:
        print("Resposta Registrada!")
    
    # Requisição ao back-end para receber a Primeira Pergunta Obrigatória
    url = "http://localhost:5000/get_job_messages/4"
    response = make_request(url)
    mandatoryQuestion1 = response['jobmessages']
    print(f"{mandatoryQuestion1}")
    MandatoryAnswer1 = input()
    print("Resposta Registrada!")

    # Requisição ao back-end para receber a Segunda Pergunta Obrigatória
    url = "http://localhost:5000/get_job_messages/5"
    response = make_request(url)
    mandatoryQuestion2 = response['jobmessages']
    print(f"{mandatoryQuestion2}")
    MandatoryAnswer2 = input()
    print("Resposta Registrada!")

    # Requisição ao back-end para receber a Terceira Pergunta Obrigatória
    url = "http://localhost:5000/get_job_messages/6"
    response = make_request(url)
    mandatoryQuestion3 = response['jobmessages']
    print(f"{mandatoryQuestion3}")
    MandatoryAnswer3 = input()
    print("Resposta Registrada!")

    # Requisição ao back-end para receber a Quarta Pergunta Obrigatória
    url = "http://localhost:5000/get_job_messages/7"
    response = make_request(url)
    mandatoryQuestion4 = response['jobmessages']
    print(f"{mandatoryQuestion4}")
    MandatoryAnswer4 = input()
    print("Resposta Registrada!")

    # Requisição da Confirmação da Vaga
    print("Confirmar aplicação da vaga ? SIM OU NÃO")
    answer = input()

    if validate_answer(answer):
        print("Preencher formulário GUPY")
        print("Sua candidatura a vaga foi registrada com sucesso. Obrigado por participar. :D")

        # Armazenar a resposta no MongoDB
        client = MongoClient('localhost', 27017)
        db = client['Chatbot']
        collection = db['respostas']

        resposta = {
            'Cargo': job_value ,
            EliminationQuestion1: EliminatoryAnswer1.upper(),
            EliminationQuestion2: EliminatoryAnswer2.upper(),
            EliminationQuestion3: EliminatoryAnswer3.upper(),
            mandatoryQuestion1: MandatoryAnswer1.upper(),
            mandatoryQuestion1: MandatoryAnswer2.upper(),
            mandatoryQuestion3: MandatoryAnswer3.upper(),
            mandatoryQuestion4: MandatoryAnswer4.upper(),
            'Você quer candidatar-se a vaga ?': answer.upper()
        }

        collection.insert_one(resposta)
    else:
        print("Confirmada sua desistência da vaga.")

chatbot_flow()
