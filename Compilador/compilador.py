from abc import abstractmethod
import sys
import time


class IngredienteTable():
    
    ingrediente_table = {}

    def getter(self, identifier):
        # Devolvendo o valor enviado
        if identifier in self.ingrediente_table:
            # Retornando o tipo e o valor
            return identifier
        elif identifier == "todos":
            return "todos"
        else:
            raise TypeError("Error, variavel não declarada")
        
    def setter(self, identifier, value):
        if identifier not in self.ingrediente_table:
            # Adicionando o valor enviado
            self.ingrediente_table[identifier] = value
        else:
            raise TypeError("Error, variavel já declarada")


class PrePro():
    def filter(code):
        # Removendo comentários em //
        code = code.split("\n")
        for i in range(len(code)):
            if "//" in code[i]:
                code[i] = code[i].split("//")[0]
        code = "\n".join(code)
        return code


class Node():
    def __init__(self, value, children):
        self.value = value
        self.children = children

    @abstractmethod
    def Evaluate(self, st):
        pass

class Cook(Node):
    def Evaluate(self, st):
        for child in self.children:
            child.Evaluate(st)

class Title(Node):
    def Evaluate(self, st):
        print(f"Preparando a receita {self.value}")

class Ingredient(Node):
    def Evaluate(self, st):
        ingrediente = self.value
        quantidade = self.children[0].Evaluate(st)
        unidade = self.children[1].Evaluate(st)
        print(f"Adicionando {quantidade} {unidade} de {ingrediente}")
        return st.setter(ingrediente, quantidade)

class Number(Node):
    def Evaluate(self, st):
        return self.value
    
class Measure(Node):
    def Evaluate(self, st):
        return self.value
    
class TakeIngredient(Node):
    def Evaluate(self, st):
        print(f"Pegando {self.value}")
        return st.getter(self.value)

class PreHeatOven(Node):
    def Evaluate(self, st):
        global oven_temperature
        oven_temperature = self.children[0].Evaluate(st)
        print(f"Pre-aquecendo o forno para {oven_temperature} graus")
        time_to_wait = int(self.children[1].Evaluate(st))
        print(f"Esperando {time_to_wait} minutos")
        time.sleep(time_to_wait)
        print("Forno pre-aquecido!")

class Mix(Node):
    def Evaluate(self, st):
        print("Vamos misturar os ingredientes")
        for child in self.children:
            ingrediente = child.Evaluate(st)  

class Add(Node):
    def Evaluate(self, st):
        print("Vamos adicionar os ingredientes")
        for child in self.children:
            child.Evaluate(st)

class Bake(Node):
    def Evaluate(self, st):
        print("Vamos assar a receita")
        for child in self.children:
            tempo = int(child.Evaluate(st))
            print(f"Assando por {tempo} minutos")
            time.sleep(tempo)
            print("Receita assada!")

class MixFor(Node):
    def Evaluate(self, st):
        print("Vamos misturar os ingredientes")
        for child in self.children:
            if child == self.children[-1]:
                print("Vamos misturar por")
                tempo = int(child.Evaluate(st))
                print(f"{tempo} minutos")
                time.sleep(tempo)
                print("Ingredientes misturados!")
            else:
                ingrediente = child.Evaluate(st)
                print(f"{ingrediente}")
    
class NoOp(Node):
    def Evaluate(self, st):
        pass

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Tokenizer:

    # Palavras reservadas
    RESERVED = ["xicara", "colher_cha", "colher_sopa", "inteiro"]
    FUNCOES = ["PRE-AQUECER-FORNO", "MISTURAR", "ADICIONAR", "MISTURAR-POR", "ASSAR"]
    
    def __init__(self, source : str):
        self.source = source
        self.position = 0
        self.next = None
    
    def select_next(self):

            # Verfica se é EOF
            if self.position == len(self.source):
                self.next = Token("EOF", "")

            # Verifica se é numero
            elif self.source[self.position].isdigit():
                numero = ""
                # Verifica se o número tem mais de uma unidade (ex:22) e se o numero é do tipo 3/4
                while  self.position < len(self.source) and self.source[self.position].isdigit() or self.source[self.position] == "/":
                    numero += self.source[self.position]
                    self.position += 1

                self.next = Token("INT", numero)

            # Verifica se é (
            elif self.source[self.position] == "(":
                self.next = Token("OPEN", self.source[self.position])
                # Atualiza a ponteiro
                self.position += 1
            
            # Verifica se é )
            elif self.source[self.position] == ")":
                self.next = Token("CLOSE", self.source[self.position])
                # Atualiza a ponteiro
                self.position += 1
            
            # Verifica se é #
            elif self.source[self.position] == "#":
                self.next = Token("TITULO", self.source[self.position])
                # Atualiza a ponteiro
                self.position += 1

            # Verifica se é @
            elif self.source[self.position] == "@":
                self.next = Token("INGREDIENTE", self.source[self.position])
                # Atualiza a ponteiro
                self.position += 1
            
            # Verifica se é %
            elif self.source[self.position] == "%":
                self.next = Token("PASSO", self.source[self.position])
                # Atualiza a ponteiro
                self.position += 1
            
            # Verifica se é \n
            elif self.source[self.position] == "\n":
                self.next = Token("BREAK", self.source[self.position])
                # Atualiza a ponteiro
                self.position += 1
            
            # Verifica se é um ponto (,)
            elif self.source[self.position] == ",":
                self.next = Token("COMMA", self.source[self.position])
                # Atualiza a ponteiro
                self.position += 1

            # Verifica se é identificador
            elif self.source[self.position].isalpha():
                identificador = ""
                # Permite identificadores com alfanuméricos, underscores e hífens
                while self.position < len(self.source) and (self.source[self.position].isalnum() or self.source[self.position] in ["_", "-"]):
                    identificador += self.source[self.position]
                    self.position += 1
                
                # Verifica se é palavra reservada
                if identificador in Tokenizer.RESERVED:
                    if(identificador == "xicara" ):
                        self.next = Token("UNIDADE", identificador)
                    elif(identificador == "colher_cha"):
                        self.next = Token("UNIDADE", identificador)
                    elif(identificador == "colher_sopa"):
                        self.next = Token("UNIDADE", identificador)
                    elif(identificador == "inteiro"):
                        self.next = Token("UNIDADE", identificador)
                elif identificador in Tokenizer.FUNCOES:
                    if(identificador == "PRE-AQUECER-FORNO"):
                        self.next = Token("FUNCAO", identificador)
                    elif(identificador == "MISTURAR"):
                        self.next = Token("FUNCAO", identificador)
                    elif(identificador == "ADICIONAR"):
                        self.next = Token("FUNCAO", identificador)
                    elif(identificador == "MISTURAR-POR"):
                        self.next = Token("FUNCAO", identificador)
                    elif(identificador == "ASSAR"):
                        self.next = Token("FUNCAO", identificador)
                # Caso seja uma variavel normal
                else:
                    self.next = Token("PALAVRA", identificador)

            # Verificar se é espaço
            elif self.source[self.position].isspace():
                self.position += 1
                self.select_next()
            
            # Erro
            else:
                raise ValueError(f"Error, caractere {self.source[self.position]} não reconhecido na posição {self.position}")

    
class Parser:
    
    #tokenizer = None

    def parse_recipe():
        resultado = Cook("Cook", [])
        while Parser.tokenizer.next.type != "EOF":
            resultado.children.append(Parser.parse_header())
        return resultado
    
    def parse_header():

        resultado = None

        # verifica se é /n
        if Parser.tokenizer.next.type == "BREAK":
            # Consome o \n
            Parser.tokenizer.select_next()
            return NoOp("NoOp", [])
        
        # Verifica se começa com #
        elif Parser.tokenizer.next.type == "TITULO":
            # Consome o #
            Parser.tokenizer.select_next()
            titulo_receita = ""
            
            while Parser.tokenizer.next.type != "BREAK":
                # Adionando o titulo
                titulo_receita += Parser.tokenizer.next.value
                # Conome palavras do titulo
                Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type == "BREAK":
                # Consome o \n
                Parser.tokenizer.select_next()
                # criando nó Title
                resultado = Title(titulo_receita, [])
                return resultado
        # Verifica se começa com @
        elif Parser.tokenizer.next.type == "INGREDIENTE":
            # Consome o @
            Parser.tokenizer.select_next()
            # Verifica se tem ingrediente
            if Parser.tokenizer.next.type == "PALAVRA":
                # Criando objeto nó do ingrediente
                ingrediente = Ingredient(Parser.tokenizer.next.value, [])
                # Consome o ingrediente
                Parser.tokenizer.select_next()
                # Verifica se tem quantidade
                if Parser.tokenizer.next.type == "INT":
                    # Criando objeto nó da quantidade
                    ingrediente.children.append(Number(Parser.tokenizer.next.value, []))
                    # Consome a quantidade
                    Parser.tokenizer.select_next()
                    # Verifica se tem unidade
                    if Parser.tokenizer.next.type == "UNIDADE":
                        # Criando objeto nó da unidade
                        ingrediente.children.append(Measure(Parser.tokenizer.next.value, []))
                        # Consome a unidade
                        Parser.tokenizer.select_next()
                        if Parser.tokenizer.next.type == "BREAK":
                            # Consome o \n
                            Parser.tokenizer.select_next()
                            return ingrediente
                        else:
                            raise TypeError("Error, não tem quebra de linha")
                    else:
                        raise TypeError("Error, não tem unidade")
                else:
                    raise TypeError("Error, não tem quantidade")
            else:
                raise TypeError("Error, não tem ingrediente")

        # Verifica se começa com %
        elif Parser.tokenizer.next.type == "PASSO":
            # Consome o %
            Parser.tokenizer.select_next()
            # verifica se tem função
            if Parser.tokenizer.next.type == "FUNCAO":
                # Salvando função
                nome_funcao = Parser.tokenizer.next.value
                # Consome a função
                Parser.tokenizer.select_next()
                # Verifica se tem (
                if Parser.tokenizer.next.type == "OPEN":
                    # Consome o (
                    Parser.tokenizer.select_next()
                    # Consumindo o miolo das funções e salvando em uma lista o resultado
                    miolo_funcao = []
                    while Parser.tokenizer.next.type != "CLOSE":
                        miolo_funcao.append(Parser.tokenizer.next.value)
                        # Consome o miolo
                        Parser.tokenizer.select_next()
                        if Parser.tokenizer.next.type == "COMMA":
                            # Consome a virgula
                            Parser.tokenizer.select_next()

                    if Parser.tokenizer.next.type == "CLOSE":
                        # Consome o )
                        Parser.tokenizer.select_next()
                        if Parser.tokenizer.next.type == "BREAK":
                            # Consome o \n
                            Parser.tokenizer.select_next()
                            #Craindo objeto nó da função
                            if nome_funcao == "PRE-AQUECER-FORNO":
                                resultado = PreHeatOven(nome_funcao, [])
                                resultado.children.append(Number(miolo_funcao[0], []))
                                resultado.children.append(Number(miolo_funcao[1], []))
                                return resultado
                            elif nome_funcao == "MISTURAR":
                                resultado = Mix(nome_funcao, [])
                                for ingrediente in miolo_funcao:
                                    resultado.children.append(TakeIngredient(ingrediente, []))
                                return resultado
                            elif nome_funcao == "ADICIONAR":
                                resultado = Add(nome_funcao, [])
                                for ingrediente in miolo_funcao:
                                    resultado.children.append(TakeIngredient(ingrediente, []))
                                return resultado
                            elif nome_funcao == "MISTURAR-POR":
                                resultado = MixFor(nome_funcao, [])
                                for ingrediente in miolo_funcao and miolo_funcao[:-1]:
                                    resultado.children.append(TakeIngredient(ingrediente, []))
                                resultado.children.append(Number(miolo_funcao[-1], []))
                                return resultado
                            elif nome_funcao == "ASSAR":
                                resultado = Bake(nome_funcao, [])
                                resultado.children.append(Number(miolo_funcao[0], []))
                                return resultado
                            
                        else:
                            raise TypeError("Error, não tem quebra de linha")
                else:
                    raise TypeError("Error, não tem (")
            else:
                raise TypeError("Error, não tem função")

        else:
            raise TypeError("Error")
        
            
    def run(code):

        # Inicializa objeto Tokenizador
        Parser.tokenizer = Tokenizer(code)
        # Posicionando no primeiro token
        Parser.tokenizer.select_next()

        # Pegando resultado calculado
        resultado = Parser.parse_recipe()

        # Verificar se chegou ao fim
        if Parser.tokenizer.next.type == "EOF":
            return resultado
        # Senão ERRO
        else:
            raise TypeError("Error")

          

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        code = file.read() + '\n'
        code = PrePro.filter(code)

    # Criando objeto tabela de simbolos
    st = IngredienteTable()
    root = Parser.run(code)
    root.Evaluate(st)
    print("RECEITA PRONTA!")