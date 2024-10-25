import pandas as pd
from typing import Union
from fastapi import FastAPI
from typing import Dict
from models import ElementoParaAnalise

app = FastAPI()

@app.post("/verificarElemento")
def verificarElemento(elementoParaAnalise: ElementoParaAnalise)-> Dict[str, Union[str, float]]:

    modelo_one_hot = pd.read_pickle('modelos/modelo_onehotenc.pkl')
    modelo_arvore = pd.read_pickle('modelos/modelo_arvore.pkl')

    return {"ehPato": "true" if modelo_arvore.predict(modelo_one_hot.transform(pd.DataFrame(elementoParaAnalise.to_dict())))[0] else "false"}