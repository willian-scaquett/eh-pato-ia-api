from pydantic import BaseModel

class ElementoParaAnalise(BaseModel):
    esverdeamento: int
    tamanho_bico: int
    grau_sotaque: int
    recorde_dias_sem_comer: int
    tem_smartphone: str
    gosta_de_lagos: str
    come_o_pao_dado_pelos_velhinhos_no_parque: str
    cursa_ti: str
    time_do_coracao: str
    
    def to_dict(self):
        return {
            'esverdeamento': [self.esverdeamento],
            'tamanho_bico': [self.tamanho_bico],
            'grau_sotaque': [self.grau_sotaque],
            'recorde_dias_sem_comer': [self.recorde_dias_sem_comer],
            'tem_smartphone': [self.tem_smartphone],
            'gosta_de_lagos': [self.gosta_de_lagos],
            'come_o_pao_dado_pelos_velhinhos_no_parque': [self.come_o_pao_dado_pelos_velhinhos_no_parque],
            'cursa_ti': [self.cursa_ti],
            'time_do_coracao': [self.time_do_coracao]
        }