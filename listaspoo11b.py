class Perfil:
    def __init__(self, id, nome, descricao, beneficios):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.beneficios = beneficios

    def __str__(self):
        return f"Perfil(id={self.id}, nome={self.nome}, descricao={self.descricao}, beneficios={self.beneficios})"


class Cliente:
    def __init__(self, id, nome, email, telefone, senha, id_perfil):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.id_perfil = id_perfil

    def __str__(self):
        return f"Cliente(id={self.id}, nome={self.nome}, email={self.email}, telefone={self.telefone}, id_perfil={self.id_perfil})"


class Profissional:
    def __init__(self, id, nome, especialidade, conselho, email, senha):
        self.id = id
        self.nome = nome
        self.especialidade = especialidade
        self.conselho = conselho
        self.email = email
        self.senha = senha

    def __str__(self):
        return f"Profissional(id={self.id}, nome={self.nome}, especialidade={self.especialidade})"


class Horario:
    def __init__(self, id, data, confirmado, id_cliente, id_servico, id_profissional):
        self.id = id
        self.data = data
        self.confirmado = confirmado
        self.id_cliente = id_cliente
        self.id_servico = id_servico
        self.id_profissional = id_profissional

    def __str__(self):
        return f"Horario(id={self.id}, data={self.data}, confirmado={self.confirmado})"


class Servico:
    def __init__(self, id, descricao, valor, duracao):
        self.id = id
        self.descricao = descricao
        self.valor = valor
        self.duracao = duracao

    def __str__(self):
        return f"Servico(id={self.id}, descricao={self.descricao}, valor={self.valor})"


def cadastrar_profissional(id, nome, especialidade, conselho, email, senha):
    profissional = Profissional(id, nome, especialidade, conselho, email, senha)
    Profissionais.inserir(profissional)
    print(f"Profissional {nome} cadastrado com sucesso!")

def cadastrar_perfil(id, nome, descricao, beneficios):
    perfil = Perfil(id, nome, descricao, beneficios)
    Perfis.inserir(perfil)
    print(f"Perfil {nome} cadastrado com sucesso!")
    
def alterar_dados_usuario(id_cliente, novos_dados):
    Clientes.atualizar(id_cliente, novos_dados)
    print(f"Dados do cliente com ID {id_cliente} atualizados com sucesso!")


def visualizar_agenda_profissional(id_profissional):
    agenda = [h for h in Horarios.listar() if h.id_profissional == id_profissional]
    if not agenda:
        print("Nenhum horário encontrado para este profissional.")
    else:
        for horario in agenda:
            print(horario)

