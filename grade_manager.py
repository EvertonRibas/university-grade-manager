"""
Sistema de Gerenciamento de Notas Universitárias
Autor: Everton Ribas
Data: 2025
"""

import pandas as pd
import os

class GerenciadorNotas:
    def __init__(self):
        self.arquivo_notas = "notas.csv"
        self.carregar_notas()
    
    def carregar_notas(self):
        """Carrega notas do arquivo CSV ou cria novo"""
        if os.path.exists(self.arquivo_notas):
            self.df = pd.read_csv(self.arquivo_notas)
        else:
            self.df = pd.DataFrame(columns=['Materia', 'Nota1', 'Nota2', 'Media', 'Situacao'])
    
    def calcular_media(self, nota1, nota2):
        """Calcula média simples"""
        return (nota1 + nota2) / 2
    
    def verificar_situacao(self, media):
        """Verifica se aluno foi aprovado"""
        return "Aprovado" if media >= 6.0 else "Reprovado"
    
    def adicionar_materia(self, materia, nota1, nota2):
        """Adiciona nova matéria com notas"""
        media = self.calcular_media(nota1, nota2)
        situacao = self.verificar_situacao(media)
        
        nova_linha = {
            'Materia': materia,
            'Nota1': nota1,
            'Nota2': nota2,
            'Media': round(media, 1),
            'Situacao': situacao
        }
        
        self.df = pd.concat([self.df, pd.DataFrame([nova_linha])], ignore_index=True)
        self.salvar_notas()
        print(f"Matéria '{materia}' adicionada com sucesso!")
        print(f"Média: {media:.1f} - Situação: {situacao}")
    
    def salvar_notas(self):
        """Salva notas no arquivo CSV"""
        self.df.to_csv(self.arquivo_notas, index=False)
    
    def mostrar_relatorio(self):
        """Mostra relatório completo das notas"""
        if self.df.empty:
            print("Nenhuma matéria cadastrada.")
            return
        
        print("\n" + "="*50)
        print("📊 RELATÓRIO DE NOTAS - GESTÃO DE TI")
        print("="*50)
        print(self.df.to_string(index=False))
        
        # Estatísticas
        media_geral = self.df['Media'].mean()
        aprovados = len(self.df[self.df['Situacao'] == 'Aprovado'])
        total = len(self.df)
        
        print(f"\n📈 ESTATÍSTICAS:")
        print(f"Média Geral: {media_geral:.1f}")
        print(f"Matérias Aprovadas: {aprovados}/{total}")
        
        if media_geral >= 6.0:
            print("🎉 Situação Geral: APROVADO!")
        else:
            print("⚠️  Situação Geral: REPROVADO")
        print("="*50)

def main():
    sistema = GerenciadorNotas()
    
    while True:
        print("\n🎓 SISTEMA DE GERENCIAMENTO DE NOTAS")
        print("1. Adicionar Matéria")
        print("2. Ver Relatório")
        print("3. Sair")
        
        opcao = input("\nEscolha uma opção (1-3): ")
        
        if opcao == "1":
            print("\n➕ ADICIONAR NOVA MATÉRIA")
            materia = input("Nome da matéria: ")
            try:
                nota1 = float(input("Nota 1: "))
                nota2 = float(input("Nota 2: "))
                sistema.adicionar_materia(materia, nota1, nota2)
            except ValueError:
                print("❌ Erro: Digite notas válidas!")
        
        elif opcao == "2":
            sistema.mostrar_relatorio()
        
        elif opcao == "3":
            print("👋 Saindo do sistema...")
            break
        
        else:
            print("❌ Opção inválida! Digite 1, 2 ou 3.")

if __name__ == "__main__":
    main()
