from gramformer import Gramformer
import torch
from gingerit.gingerit import GingerIt
def correct(text):
    gf=Gramformer(models=1,use_gpu=True)
    #error_text="what be the reason for everyone leave the company"
    print(list(gf.correct(text))[0])
    return list(gf.correct(text))[0]


def correct_ginger(text):
    parse=GingerIt()
    return parse.parse(text)
