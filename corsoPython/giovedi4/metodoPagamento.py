class MetodoPagamento:
    def effettua_pagamento(self,importo):


class CartadiCredito(MetodoPagamento):
    def effettua_pagamento(self,importo)
     return f"Pagamento di {importo}€ effettuato con Carta di Credito."

class PayPal(MetodoPagamento):
    def effettua_pagamento(self,importo)
     return f"Pagamento di {importo}€ effettuato con PayPal."

class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self,importo)
     return f"Pagamento di {importo}€ effettuato con Bonifico Bancario."

class GestorePagamenti:
    def __init__(self, metodo_pagamento):
        self.metodo_pagamento = metodo_pagamento

    def paga(self, importo):
        return self.metodo_pagamento.effettua_pagamento(importo)

# Esempio di utilizzo
pagamento_carta = CartaDiCredito()
pagamento_paypal = PayPal()
pagamento_bonifico = BonificoBancario()

gestore_carta = GestorePagamenti(pagamento_carta)
gestore_paypal = GestorePagamenti(pagamento_paypal)
gestore_bonifico = GestorePagamenti(pagamento_bonifico)