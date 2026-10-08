listatokens = [
    "FUNCTION",     # fn  (0)
    "MAIN",         # main  (1)
    "LET",          # let  (2)
    "INT",          # int  (3)
    "FLOAT",        # float  (4)
    "CHAR",         # char  (5)
    "IF",           # if  (6)
    "ELSE",         # else  (7)
    "WHILE",        # while  (8)
    "PRINTLN",      # println  (9)
    "RETURN",       # return  (10)
    "LBRACKET",     # (  (11)
    "RBRACKET",     # )  (12)
    "LBRACE",       # {  (13)
    "RBRACE",       # }  (14)
    "ARROW",        # ->  (15)
    "COLON",        # :  (16)
    "SEMICOLON",    # ;  (17)
    "COMMA",        # ,  (18)
    "ASSIGN",       # =  (19)
    "EQ",           # ==  (20)
    "NE",           # !=  (21)
    "GT",           # >  (22)
    "GE",           # >=  (23)
    "LT",           # <  (24)
    "LE",           # <=  (25)
    "PLUS",         # +  (26)
    "MINUS",        # -  (27)
    "MULT",         # *  (28)
    "DIV",          # /  (29)
    "ID",           # [a-zA-Z]([a-zA-Z0-9])*  (30)
    "INT_CONST",    # [0-9]([0-9])*  (31)
    "FLOAT_CONST",  # [0-9]([0-9])*.[0-9]([0-9])*  (32)
    "CHAR_LITERAL", # ∑  literal de caractere  (33)
    "FMT_STRING"    # ∑+ string de formatação  (34)
]

def readFile(name):
    with open(name, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        return conteudo

class reconheceLexema():
    def __init__ (self, conteudo:str):
        self.texto = conteudo
        self.posicao = 0
        self.estadoatual = 0
        self.linha = 1
        self.tokens = list()
        self.erro = 0
        self.temp = list()

    def char_atual (self):
        """Define o caractere atual do ponteiro"""
        if self.posicao < len(self.texto):
            return self.texto[self.posicao]
        return None

    def avancar (self, passos = 1):
        """Move o ponteiro para frente"""
        self.posicao += passos

    def executarLeitura(self):
        while self.posicao < len(self.texto):
            token = {"tipo": str(), "lexema": str(), "linha": int()}
            char = self.char_atual()
            print(f"Lendo char: {char}")
            if char == "\n" and self.estadoatual == 0:
                self.linha += 1
                token["linha"] = self.linha
                self.avancar()
                continue
            elif char == " " and self.estadoatual == 0:
                self.avancar()
                continue
            elif char == "(" and self.estadoatual == 0:
                token["lexema"] = "("
                token["tipo"] = listatokens[11]
                self.tokens.append(token)
            elif char == ")" and self.estadoatual == 0:
                token["lexema"] = ")"
                token["tipo"] = listatokens[12]
                self.tokens.append(token)
            elif char == "{" and self.estadoatual == 0:
                token["lexema"] = "{"
                token["tipo"] = listatokens[13]
                self.tokens.append(token)
            elif char == "}" and  self.estadoatual == 0:
                token["lexema"] = "}"
                token["tipo"] = listatokens[14]
                self.tokens.append(token)
            elif char == ":" and self.estadoatual == 0:
                token["lexema"] = ":"
                token["tipo"] = listatokens[16]
                self.tokens.append(token)
            elif char == ";" and self.estadoatual == 0:
                token["lexema"] = ";"
                token["tipo"] = listatokens[17]
                self.tokens.append(token)
            elif char == "," and self.estadoatual == 0:
                token["lexema"] = ","
                token["tipo"] = listatokens[18]
                self.tokens.append(token)
            elif char == "=" and self.estadoatual == 0:
                if self.posicao+1 < len(self.texto) and self.texto[self.posicao+1] == "=":
                    token["lexema"] = "=="
                    token["tipo"] = listatokens[20]
                    self.tokens.append(token)
                    self.avancar()
                else:
                    token["lexema"] = "="
                    token["tipo"] = listatokens[19]
                    self.tokens.append(token)
            elif char == "!" and self.estadoatual == 0:
                if self.posicao+1 < len(self.texto) and self.texto[self.posicao+1] == "=":
                    token["lexema"] = "!="
                    token["tipo"] = listatokens[21]
                    self.tokens.append(token)
            elif char == ">" and self.estadoatual == 0:
                if self.posicao+1 < len(self.texto) and self.texto[self.posicao+1] == "=":
                    token["lexema"] = ">="
                    token["tipo"] = listatokens[23]
                    self.tokens.append(token)
                    self.avancar()
                else:    
                    token["lexema"] = ">"
                    token["tipo"] = listatokens[22]
                    self.tokens.append(token)
            elif char == "<" and self.estadoatual == 0:
                if self.posicao+1 < len(self.texto) and self.texto[self.posicao+1] == "=":
                    token["lexema"] = "<="
                    token["tipo"] = listatokens[25]
                    self.tokens.append(token)
                    self.avancar()
                else:
                    token["lexema"] = "<"
                    token["tipo"] = listatokens[24]
                    self.tokens.append(token)
            elif char == "+" and self.estadoatual == 0:
                token["lexema"] = "+"
                token["tipo"] = listatokens[26]
                self.tokens.append(token)
            elif char == "-" and self.estadoatual == 0:
                if self.posicao < len(self.texto) and self.texto[self.posicao+1] == ">":
                    token["lexema"] = "->"
                    token["tipo"] = listatokens[15]
                    self.tokens.append(token)
                    self.avancar()
                else:
                    token["lexema"] = "-"
                    token["tipo"] = listatokens[27]
                    self.tokens.append(token)
            elif char == "*" and self.estadoatual == 0:
                token["lexema"] = "*"
                token["tipo"] = listatokens[28]
                self.tokens.append(token)
            elif char == "/" and self.estadoatual == 0:
                token["lexema"] = "/"
                token["tipo"] = listatokens[29]
                self.tokens.append(token)
            elif char == "'" and self.estadoatual == 0:
                self.temp.clear()
                self.temp.append(char)
                self.tokens.append(token)
                if self.posicao+1 < len(self.texto) and self.texto[self.posicao+1].isascii() == True and self.texto[self.posicao+1] != "\n":
                    self.avancar()
                    self.temp.append(char)
                    if self.posicao+1 < len(self.texto) and self.texto[self.posicao+1] == "'":
                        self.temp.append(char)
                        self.avancar()
                        token["lexema"] = "".join(self.temp)
                        token["tipo"] = listatokens[33]
                        self.tokens.append(token)
                    else:
                        self.erro = 1
                        print(f"Erro léxico, linha {self.linha}.")
                else:
                    self.erro = 1
                    print(f"Erro léxico, linha {self.linha}.")
            elif char == '"' and self.estadoatual == 0:
                self.estadoatual = 1
                self.temp.clear()
                self.temp.append('"')
            elif char.isascii() == True and self.estadoatual == 1:
                self.temp.append(char)
                if char == '"' and ((self.posicao+1 < len(self.texto) and self.texto[self.posicao+1] == "\n") or self.texto[self.posicao+1] == False):
                    self.temp.clear()
                    self.temp.append(char)
                    token["lexema"] = "".join(self.temp)
                    token["tipo"] = listatokens[34]
                    self.tokens.append(token)
                    self.estadoatual = 0
                elif char != "\n":
                    self.temp.clear()
                    self.temp.append(char)
                else:
                    print(f"Erro léxico, linha {self.linha}.")
                    self.erro = 1
            elif char.islower()== True and self.estadoatual == 0:
                self.estadoatual = 2
                self.temp.clear()
                self.temp.append(char)
                if not (self.posicao+1 < len(self.texto) and (self.texto[self.posicao+1].isalnum() == True or self.texto[self.posicao+1] == "_")):
                    token["lexema"] = "".join(self.temp)
                    token["tipo"] = listatokens[30]
                    self.tokens.append(token)
                    self.estadoatual = 0
            elif (char.isalnum() == True or char == "_") and self.estadoatual == 2:
                self.temp.append(char)
                if not (self.posicao+1 < len(self.texto) and (self.texto[self.posicao+1].isalnum() == True or self.texto[self.posicao+1] == "_")):
                    token["lexema"] = "".join(self.temp)
                    token["tipo"] = listatokens[30]
                    self.tokens.append(token)
                    self.estadoatual = 0
            elif char.isnumeric() == True and self.estadoatual == 0:
                self.temp.clear()
                self.temp.append(char)
                self.estadoatual = 3
                if not (self.posicao+1 < len(self.texto) and (self.texto[self.posicao+1].isnumeric() or self.texto[self.posicao+1] == ".")):
                    token["lexema"] = "".join(self.temp)
                    token["tipo"] = listatokens[31]
                    self.tokens.append(token)
                    self.estadoatual = 0
            elif char.isnumeric() == True and self.estadoatual == 3:
                self.temp.append(char)
                if not (self.posicao+1 < len(self.texto) and (self.texto[self.posicao+1].isnumeric() or self.texto[self.posicao+1] == ".")):
                    token["lexema"] = "".join(self.temp)
                    token["tipo"] = listatokens[31]
                    self.tokens.append(token)
                    self.estadoatual = 0
            elif char == "." and self.estadoatual == 3:
                self.temp.append(char)
                self.estadoatual = 4
                if not (self.posicao+1 < len(self.texto) and self.texto[self.posicao+1].isnumeric()):
                    token["lexema"] = "".join(self.temp)
                    token["tipo"] = listatokens[32]
                    self.tokens.append(token)
                    self.estadoatual = 0
            elif char.isnumeric() and self.estadoatual == 4:
                self.temp.append(char)
                if not (self.posicao+1 < len(self.texto) and self.texto[self.posicao+1].isnumeric()):
                    token["lexema"] = "".join(self.temp)
                    token["tipo"] = listatokens[32]
                    self.tokens.append(token)
                    self.estadoatual = 0
            else: 
                print(f"Erro léxico linha {token['linha']}")
                self.erro = 1
            if self.erro == 1:
                self.estadoatual = 0
                self.erro = 0
            self.avancar()
        return self.tokens


def identificarPalavrasReservadas(tokens):
    for item in tokens:
        if (item["lexema"] == listatokens[30]):
            if ("fn" in item["lexema"] and len(item["lexema"]) == 2):
                item["lexema"] = listatokens[0]
            elif ("main" in item["lexema"] and len(item["lexema"]) == 4):
                item["lexema"] = listatokens[1]
            elif ("let" in item["lexema"] and len(item["lexema"]) == 3):
                item["lexema"] = listatokens[2]
            elif ("int" in item["lexema"] and len(item["lexema"]) == 3):
                item["lexema"] = listatokens[3]
            elif ("float" in item["lexema"] and len(item["lexema"]) == 5):
                item["lexema"] = listatokens[4]
            elif ("char" in item["lexema"] and len(item["lexema"]) == 4):
                item["lexema"] = listatokens[5]
            elif ("if" in item["lexema"] and len(item["lexema"]) == 2):
                item["lexema"] = listatokens[6]
            elif ("else" in item["lexema"] and len(item["lexema"]) == 4):
                item["lexema"] = listatokens[7]
            elif ("while" in item["lexema"] and len(item["lexema"]) == 5):
                item["lexema"] = listatokens[8]
            elif ("println" in item["lexema"] and len(item["lexema"]) == 7):
                item["lexema"] = listatokens[9]
            elif ("return" in item["lexema"] and len(item["lexema"]) == 6):
                item["lexema"] = listatokens[10]
    return tokens