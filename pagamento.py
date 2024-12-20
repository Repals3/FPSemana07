class Pagamento:
    def processar_pagamento(self, valor):
        pass

class CartaoCredito(Pagamento):
    def __init__(self, numero_cartao, titular, validade, cvv):
        self.numero_cartao = numero_cartao
        self.titular = titular
        self.validade = validade
        self.cvv = cvv

    def processar_pagamento(self, valor):
        print(f"€{valor:.2f} com Cartao de Credito ({self.numero_cartao})")

class PayPal(Pagamento):
    def __init__(self, email):
        self.email = email

    def processar_pagamento(self, valor):
        print(f"€{valor:.2f} com PayPal (e-mail: {self.email})")

class TransferenciaBancaria(Pagamento):
    def __init__(self, banco, agencia, conta):
        self.banco = banco
        self.agencia = agencia
        self.conta = conta

    def processar_pagamento(self, valor):
        print(f"€{valor:.2f} com Transferencia Bancaria (banco: {self.banco}, conta: {self.conta})")

def realizar_pagamento(pagamento: Pagamento, valor):
    pagamento.processar_pagamento(valor)

if __name__ == "__main__":
    cartao = CartaoCredito("1234 5678 9012 3456", "João Silva", "12/25", "123")
    realizar_pagamento(cartao, 150.00)

    paypal = PayPal("joao.silva@email.com")
    realizar_pagamento(paypal, 200.00)
    transferencia = TransferenciaBancaria("Banco Central", "1234", "12345678")
    realizar_pagamento(transferencia, 300.00)
