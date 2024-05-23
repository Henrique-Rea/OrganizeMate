import PyPDF2
import os

mixer = PyPDF2.PdfMerger()

arquivos = os.listdir("Mixerpdf/arquivos")#os pdfs usados deverão ser inseridos na pasta arquivos
arquivos.sort() #aqui o código irá organizar os arquivos, então recomendo que enumere eles no seu nome como: 01.Dom Casmurro, que será o primeiro arquivo do pdf final

for arquivo in arquivos:
  if ".pdf" in arquivo: #checa se o arquivo é um pdf por meio de sua extensão
    mixer.append(f"Mixerpdf/arquivos/{arquivo}")


mixer.write("PDF Mesclado.pdf") #ao fim ele cria o novo arquivo nomeado como "PDF Mesclado"