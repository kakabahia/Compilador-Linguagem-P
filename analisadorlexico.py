tokens = [
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
    def __init__ (self, conteudo):
        self.texto = conteudo
        self.posicao = 0
        self.estadoatual = 0
        self.linha = 1
        self.tokens = list()
        self.erros = 0
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
            token = {'tipo': str(), 'lexema': str(), 'linha': int()}
            char = self.char_atual()
            if char == "\n":
                self.linha += 1
                self.avancar()
            elif char == " ":
                self.avancar()
            elif char == "(" and self.estadoatual == 0:
                token["lexema"] = "("
                token["tipo"] = tokens[11]
                token["linha"] = self.linha
            elif char == ")" and self.estadoatual == 0:
                token["lexema"] = ")"
                token["tipo"] = tokens[12]
                token["linha"] = self.linha
            elif char == "{" and self.estadoatual == 0:
                token["lexema"] = "{"
                token["tipo"] = tokens[13]
                token["linha"] = self.linha
            elif char == "}" and  self.estadoatual == 0:
                token["lexema"] = "}"
                token["tipo"] = tokens[14]
                token["linha"] = self.linha
            elif char == ":" and self.estadoatual == 0:
                token["lexema"] = ":"
                token["tipo"] = tokens[16]
                token["linha"] = self.linha
            elif char == ";" and self.estadoatual == 0:
                token["lexema"] = ";"
                token["tipo"] = tokens[17]
                token["linha"] = self.linha
            elif char == "," and self.estadoatual == 0:
                token["lexema"] = ","
                token["tipo"] = tokens[18]
                token["linha"] = self.linha
            elif char == "=" and self.estadoatual == 0:
                if self.posicao+1 < len(self.texto) and self.texto[self.posicao+1] == "=":
                    token["lexema"] = "=="
                    token["tipo"] = tokens[20]
                    token["linha"] = self.linha
                    self.avancar()
                else:
                    token["lexema"] = "="
                    token["tipo"] = tokens[19]
                    token["linha"] = self.linha
            elif char == "!" and self.estadoatual == 0:
                if self.posicao+1 < len(self.texto) and self.texto[self.posicao+1] == "=":
                    token["lexema"] = "!="
                    token["tipo"] = tokens[21]
                    token["linha"] = self.linha
            elif char == ">" and self.estadoatual == 0:
                if self.posicao+1 < len(self.texto) and self.texto[self.posicao+1] == "=":
                    token["lexema"] = ">="
                    token["tipo"] = tokens[23]
                    token["linha"] = self.linha
                    self.avancar()
                else:    
                    token["lexema"] = ">"
                    token["tipo"] = tokens[22]
                    token["linha"] = self.linha
            elif char == "<" and self.estadoatual == 0:
                if self.posicao+1 < len(self.texto) and self.texto[self.posicao+1] == "=":
                    token["lexema"] = "<="
                    token["tipo"] = tokens[25]
                    token["linha"] = self.linha
                    self.avancar()
                else:
                    token["lexema"] = "<"
                    token["tipo"] = tokens[24]
                    token["linha"] = self.linha
            elif char == "+" and self.estadoatual == 0:
                token["lexema"] = "+"
                token["tipo"] = tokens[26]
                token["linha"] = self.linha
            elif char == "-" and self.estadoatual == 0:
                if self.posicao < len(self.texto) and self.texto[self.posicao+1] == ">":
                    token["lexema"] = "->"
                    token["tipo"] = tokens[15]
                    token["linha"] = self.linha
                    self.avancar()
                else:
                    token["lexema"] = "-"
                    token["tipo"] = tokens[27]
                    token["linha"] = self.linha
            elif char == "*" and self.estadoatual == 0:
                token["lexema"] = "*"
                token["tipo"] = tokens[28]
                token["linha"] = self.linha
            elif char == "/" and self.estadoatual == 0:
                token["lexema"] = "/"
                token["tipo"] = tokens[29]
                token["linha"] = self.linha
            elif char == "'" and self.estadoatual == 0:
                temp = list()
                temp.append(char)
                if self.posicao+1 < len(self.texto) and self.texto[self.posicao+1].isascii() == True and self.texto[self.posicao+1] != "\n":
                    self.avancar()
                    temp.append(char)
                    if self.posicao+1 < len(self.texto) and self.texto[self.posicao+1] == "'":
                        temp.append(char)
                        self.avancar()
                        token["lexema"] = temp
                        token["tipo"] = tokens[33]
                    else:
                        self.erros = 1
                        print(f"Erro léxico, linha {self.linha}.")
                else:
                    self.erros = 1
                    print(f"Erro léxico, linha {self.linha}.")
            elif char == '"' and self.estadoatual == 0:
                self.estadoatual = 1
            elif char.isascii() == True and self.estadoatual == 1:
                temp = list()
                temp.append('"')
                if char == '"' and ((self.posicao+1 < len(self.texto) and self.texto[self.posicao+1] == "\n") or self.texto[self.posicao+1] == False):
                    temp.append(char)
                    token["lexema"] = temp
                    token["tipo"] = tokens[34]
                    token["linha"] = self.linha
                    self.posicao = 0
                elif char != "\n":
                    temp.append(char)

                    
                    
                            
            self.avancar()
            self.tokens.append(token)



def identificarPalavrasReservadas(codigo):
    for item in codigo:
        if (item[tokens] == tokens[30]):
            if ("fn" in item[codigo] and len(item[codigo]) == 2):
                item[tokens] = tokens[0]
            elif ("main" in item[codigo] and len(item[codigo]) == 4):
                    item[tokens] = tokens[1]
            elif ("let" in item[codigo] and len(item[codigo]) == 3):
                item[tokens] = tokens[2]
            elif ("int" in item[codigo] and len(item[codigo]) == 3):
                item[tokens] = tokens[3]
            elif ("float" in item[codigo] and len(item[codigo]) == 5):
                item[tokens] = tokens[4]
            elif ("char" in item[codigo] and len(item[codigo]) == 4):
                item[tokens] = tokens[5]
            elif ("if" in item[codigo] and len(item[codigo]) == 2):
                item[tokens] = tokens[6]
            elif ("else" in item[codigo] and len(item[codigo]) == 4):
                item[tokens] = tokens[7]
            elif ("while" in item[codigo] and len(item[codigo]) == 5):
                item[tokens] = tokens[8]
            elif ("println" in item[codigo] and len(item[codigo]) == 7):
                item[tokens] = tokens[9]
            elif ("return" in item[codigo] and len(item[codigo]) == 6):
                item[tokens] = tokens[10]
