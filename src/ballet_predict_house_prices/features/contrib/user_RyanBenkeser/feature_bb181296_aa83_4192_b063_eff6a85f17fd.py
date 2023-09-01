from ballet import Feature
from ballet.eng.external.sklearn import SimpleImputer

input = ["Year Built"]
transformer = SimpleImputer(
    strategy="mean"
)  # TODO - function, transformer-like, or list thereof
name = "Imputed Year Built"  # TODO - str
feature = Feature(input=input, transformer=transformer, name=name)
