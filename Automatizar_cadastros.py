import pyautogui as pa
import time


pa.PAUSE = 0.8


pa.press('win')
pa.write('chrome')
pa.press('enter')
pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pa.press('enter')

time.sleep(3)

pa.click(x=703, y=412)
pa.write('teste@gmail.com')
pa.press('tab')
pa.write('123123456456')
pa.press('tab')
pa.press('enter')

import pandas as pd
tabela = pd.read_csv('produtos.csv')

for linha in tabela.index:

    informacao = str(tabela.loc[linha, 'codigo'])

    pa.click(x=647, y=293)


    pa.write(str(informacao))
    pa.press('tab')
    pa.write(str(tabela.loc[linha, 'marca']))
    pa.press('tab')
    pa.write(str(tabela.loc[linha, 'tipo']))
    pa.press('tab')
    pa.write(str(tabela.loc[linha, 'categoria']))
    pa.press('tab')
    pa.write(str(tabela.loc[linha, 'preco_unitario']))
    pa.press('tab')
    pa.write(str(tabela.loc[linha, 'custo']))
    pa.press('tab')
    obs = tabela.loc[linha, 'obs']
    
    if not pd.isna(obs):
        pa.write(str(tabela.loc[linha, "obs"]))
    
    pa.press('tab')
    time.sleep(1)
    pa.press('enter')
    pa.press('enter')
    
    time.sleep(0.5)