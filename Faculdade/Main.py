from back_end import Mago, Ladino, Guerreiro,Heroi
from abc import ABC, abstractmethod

if __name__ == "__main__":
    

    heroi_1 = Mago("Lion", "masculino", "Elfo", "Bola de Fogo", 142, 4, 3, 7)
    print(f"""\n ===== Herói Generico 1 =====
    
    - Nome: {heroi_1.get_nome()}
    - Idade: {heroi_1.get_idade()}
    - Vida: {heroi_1.get_vida()}
    - Genêro: {heroi_1.get_genero()}
    - Raça: {heroi_1.get_raça()}
    - Mana + Multiplicador: {heroi_1.get_mana()}
    - Carisma: {heroi_1.get_carisma()}
    - Tipo: {heroi_1.Elemento()}

    {heroi_1.apresentar()}

    Seus objetos iniciais serão: {heroi_1.Obj_iniciais()}

    {heroi_1.usar_habilidade()}

    {heroi_1.set_nome("Irineu")}
    {heroi_1.set_idade(1)}
    {heroi_1.set_vida(999)}
    {heroi_1.set_genero("Não identificado")}
    {heroi_1.set_raça("Não reconhecida")}
    {heroi_1.set_mana(9999)}
    {heroi_1.set_carisma(0)}

    Heroi mudou todos os seus atributos.

    - Nome: {heroi_1.get_nome()}
    - Idade: {heroi_1.get_idade()}
    - Vida: {heroi_1.get_vida()}
    - Genêro: {heroi_1.get_genero()}
    - Raça: {heroi_1.get_raça()}
    - Mana + Multiplicador: {heroi_1.get_mana()}
    - Carisma: {heroi_1.get_carisma()}
    - Tipo: {heroi_1.Elemento()}

    {heroi_1.apresentar()}

""")
    heroi_2 = Ladino("Albriana", "feminino", "Anão", "Espreitar nas Sombras", 162, 6, 8, 5)
    print(f"""\n ===== Herói Generico 2 =====
    
    - Nome: {heroi_2.get_nome()}
    - Idade: {heroi_2.get_idade()}
    - Vida: {heroi_2.get_vida()}
    - Genêro: {heroi_2.get_genero()}
    - Raça: {heroi_2.get_raça()}
    - Furtividade + Multiplicador: {heroi_2.get_furtividade()}
    - Carisma: {heroi_2.get_carisma()}
    - Tipo: {heroi_2.Elemento()}

    {heroi_2.apresentar()}
    
    Seus objetos iniciais serão: {heroi_2.Obj_iniciais()}

    {heroi_2.usar_habilidade()}

    {heroi_2.set_tecnica("Espreitar da morte")}
    {heroi_2.set_furtividade(9)}

    Heroi mudou sua habilidade para {heroi_2.get_tecnica()}
    Heroi mudou (outro multiplicador) sua furtividade para {heroi_2.get_furtividade()}

""")
    heroi_3 = Guerreiro("Scarbert", "masculino", "Goblin", "Martelo Voador", 222, 8, 1, 5)
    print(f"""\n ===== Herói Generico 3 =====
    
    - Nome: {heroi_3.get_nome()}
    - Idade: {heroi_3.get_idade()}
    - Vida: {heroi_3.get_vida()}
    - Genêro: {heroi_3.get_genero()}
    - Raça: {heroi_3.get_raça()}
    - Fúria + Multiplicador: {heroi_3.get_fúria()}
    - Carisma: {heroi_3.get_carisma()}
    - Tipo: {heroi_3.Elemento()}

    {heroi_3.apresentar()}

    Seus objetos iniciais serão: {heroi_3.Obj_iniciais()}

    {heroi_3.usar_habilidade()}

    {heroi_3.set_golpe("Machado ESMAGADOR")}
    {heroi_3.set_fúria(9)}

    Heroi mudou sua habilidade para {heroi_3.get_golpe()}
    Heroi mudou (outro multiplicador) sua fúria para {heroi_3.get_fúria()}
""")