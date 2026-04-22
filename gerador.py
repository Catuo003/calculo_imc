import random
import requests
import os


class Biopedancia:
    def __init__(self):
        self.dados = []
    
    def _limparTela(self):
        return os.system('cls' if os.name == 'nt' else 'clear')


    def _montarUrl(self):
        paginas = random.randint(1, 200)
        return f'https://servicodados.ibge.gov.br/api/v3/nomes/2022/localidade/0/ranking/nome?page={paginas}'
    
    def _requisitaNomes(self):
        site = self._montarUrl()    
        try:
            reque = requests.get(site)
            if reque.status_code == 200:
                return reque.json()
            
            else:
                print(f'| Erro na requisição !')
            
        except Exception as erro:
            print(f'| Erro inesperado na requisição: {erro}')
            return None

    def _geracaoDados(self):
        dados = self._requisitaNomes()
        nome = dados['items'][0]['nome'].capitalize()
        idade = random.randint(18, 65)
        peso = round(random.uniform(30.0, 180.0), 2)
        altura = round(random.uniform(150, 200))
        return nome, idade, peso, altura

    def _montaBd(self):
        nome, idade, peso, altura = self._geracaoDados()
        dados = {
            'nome': nome,
            'idade': idade,
            'peso': peso,
            'altura': altura
        }
        self.dados.append(dados)

    
    def _analiseImc(self, peso, altura_cm):
        altura_cm = altura_cm / 100
        imc = peso / (altura_cm ** 2)
        return round(imc)

    def _situacaoImc(self, imc):
            if imc < 18.5:
                return "Abaixo"
            elif imc < 25:
                return "Normal"
            elif imc < 30:
                return "Sobrepeso"
            else:
                return "Obesidade"

    def _analiseCorporal(self):
        for _ in range(10):
            self._montaBd()

    def main(self):
        self._limparTela()
        self._analiseCorporal()
        print('-'*80)
        print(f'| {'NOME':^10} | {'IDADE':^9} | {'ALTURA(cm)':^10} | {'PESO':^10} | {'IMC':^10} | {'SITUAÇÃO':^10}   |')
        print('-'*80)
        
        for items in self.dados:
            nome = items['nome']
            idade = items['idade']
            altura = items['altura']
            peso = items['peso']
            imc = self._analiseImc(peso, altura)
            situacao = self._situacaoImc(imc)

            print(f'| {nome:^10} | {idade:^9} | {altura:^10} | {peso:^10} | {imc:^10} | {situacao:^10}   |')
        print('-'*80)
run = Biopedancia()
run.main()