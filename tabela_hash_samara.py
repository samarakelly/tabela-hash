class tabela_hash: #OK
    def __init__(self,tamanho):
        self.tamanho= tamanho
        self.qnt_elemento= 0
        self.tabela= []
        self.inicializar_tabela()

    class elemento:
        def __init__(self, key, value):
            self.key= key
            self.value=value

    def items(self):
        items=[]
        for lista in self.tabela:
            for elemento in lista:
                tupla= elemento.key, elemento.value
                items.append(tupla)
        return items

    def keys(self):
        keys= []
        for lista in self.tabela:
            for elemento in lista:
                keys.append(elemento.key)
        return keys

    def values(self):
        values= []
        for lista in self.tabela:
            for elemento in lista:
                values.append(elemento.values)

    def __len__(self):
        return self.qnt_elemento

    def __iter__(self):
        return iter(self.keys())

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        retorno = "["
        i=0
        for chave, valor in self.items():
            retorno+= chave.__repr__()
            retorno+= ':'
            retorno+= valor.__repr__()

            if 1< len(self)-1:
                retorno+= ','
            i+=1
        retorno+=']'
        return retorno

    def __delitem__(self, key):
        indicie= self.fun_hash(key)
        for i, elemento in enumerate(self.tabela):
            if elemento.key == key:
                del self.tabela[indicie][i]
                self.qnt_elemento-=1
                return
        raise KeyError(key)

    def __setitem__(self, key, value):
        self.atualizar_elemento(key, value)

    def __getitem__(self,key):
        elemento= self.buscar_elemento(key)
        return elemento

    def __contains__(self,key):
        try:
            self.buscar_elemento(key)
            return True
        except KeyError:
            return False

    def buscar_elemento(self, key):
        for lista in self.tabela:
            for elemento in lista:
                if elemento.key== key:
                    return elemento
        raise KeyError(key)

    def atualizar_elemento(self, key, value):
        try:
            elemento= self.buscar_elemento(key)
            elemento.value= value

        except KeyError:
            indicie= self.fun_hash(key)
            novo= self.elemento(key, value)
            self.tabela[indicie].append(novo)
            self.qnt_elemento+=1

    def fun_hash(self, key):
        return hash(key) % self.tamanho

    def inicializar_tabela(self):
        for i in range(self.tamanho):
            self.tabela.append([])


notas = tabela_hash(11)
pessoa = tabela_hash(11)

notas['1va'] = 7.9
notas['2va'] = 7.2
notas['3va'] = 8.6

pessoa['nome'] = 'Ygor'
pessoa['nome'] = 'João'
pessoa['idade'] = 31
pessoa['profissão'] = 'Professor'
pessoa['notas'] = notas

print(pessoa['profissão'])
print(len(pessoa))
print('nom' in pessoa)
print(pessoa)
print()
for e in pessoa.items():
    print(e)

aluno = {'nome': 'Fulano da Silva', 'idade': 30}

for e in aluno.values():
     print(e)
