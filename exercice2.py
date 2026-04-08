class Produit:
    def __init__(self,nom,prix,description):
        self.nom=nom
        self.prix=prix
        self.description=description

    def afficher_infos(self):
        print(f"le nom est: {self.nom},le prix est: {self.prix} et la description est: {self.description}")
    def modifier_prix(self,nouveau_prix):
        self.prix=nouveau_prix
        print(f"le nouveau prix est: {self.prix}")
    def mettre_a_jour(self,nouvelle_description):
        self.description=nouvelle_description
        print(f"la nouvelle description est: {self.description}")

mn_produit=Produit("creme main", "4500f", "Hydratante et douce")
mn_produit.afficher_infos()
mn_produit.modifier_prix("6000f")
mn_produit.mettre_a_jour("Enrichi en huile de coco")


