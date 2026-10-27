# avaliaçao:o que o usuario escreve sobre uma obra
class avaliacao:
    def __init__(self,autor,nota,comentario = ""):
        self.nota = nota
        self.comentario = comentario

    def __str__(self):
        texto = f"{self.autor}: {self.nota}/10"
        if self.comentario:
            texto += f' - "{self.comentario}"'

        class filme(obra):
            tipo = "filme" # atributo de classe: cada subclasse sobrescreve

            def __init__(self, titulo, ano, genero, duracao_min):
                super().__init(titulo,ano,genero)
                self.duracao_min = duracao_min

            def adicionar_avaliacoes(self, avaliacao):
                self.avaliacoes.append(avaliacao)

            def media(self):
                if not self.avliacoes:
                    return 0.0
                total = sum(a.nota for a in self.avaliacoes)
                return total / len(self.avaliacoes)
            
            def detalhes(self):
                return ""
            def __str__(self):
                base = f"[{self.tipo}] {self.titulo} ({self.ano}) - {self.genero}"
                extra = self.detalhes
                if extra:
                    base += f" | {extra}"
                return f"{base} | media: {self.media():.1f} ({len(self.avaliacoes)} avaliacoes)"
                
def main():
    avaliacao = avaliacao("joel", 9, "otimo filme")
    print(avaliacao)

    obra = obra("interestelar", 20214, "ficçao cientifica")
    print (obra)
    obra.adicionar_avaliacao(avaliacao("ana", 9))    
    obra.adicionar_avaliacao(avaliacao("bruno", 7))  
    print(obra)
    print("media: ", obra.media()) 

    filme = filme("matrix", 199, "ficçao cientifica", 136)
    filme.adicionar_avaliacao(avaliacao("carla", 10))
    print(filme)

if __name__ == "__main__":
    main()