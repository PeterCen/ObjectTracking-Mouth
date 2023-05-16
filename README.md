# Detecção de Boca Aberta ou Fechada com OpenCV e Dlib
Programa para indicar se a boca na webcam está aberta ou fechada.

Este script Python utiliza as bibliotecas OpenCV e Dlib para detectar se a boca de uma pessoa está aberta ou fechada em tempo real, utilizando a webcam do computador.

<h2>Como funciona</h2>
  
Primeiro, o script carrega um modelo pré-treinado para detecção de pontos faciais (shape_predictor_68_face_landmarks.dat) usando a biblioteca Dlib. Este modelo é capaz de detectar 68 pontos de referência em uma face humana, incluindo pontos ao redor da boca.

Em seguida, o script inicializa o detector de faces frontal da Dlib e a captura de vídeo da webcam.

O script entra em um loop infinito, onde lê cada frame da captura de vídeo, converte o frame para escala de cinza e detecta faces no frame.

Para cada face detectada, o script utiliza o modelo pré-treinado para detectar os pontos de referência faciais. Ele extrai as coordenadas dos pontos ao redor da boca (pontos 48 a 68).

O script calcula a distância vertical entre os pontos 2 e 10 da boca (parte superior e inferior da boca, respectivamente). Se essa distância for maior que um valor de limiar (neste caso, 23), a boca é considerada aberta. Caso contrário, é considerada fechada.

O script desenha o contorno da boca e escreve o status da boca (aberta ou fechada) no frame.

O frame resultante é exibido em uma janela. O loop continua até que a tecla 'q' seja pressionada.

Por fim, o script libera os recursos utilizados.

<h2>Requisitos</h2>

Python 3

OpenCV

Dlib

shape_predictor_68_face_landmarks.dat (modelo pré-treinado para detecção de pontos faciais)

<h2>Como executar</h2>
Instale as dependências necessárias.
Baixe o modelo pré-treinado e coloque-o no mesmo diretório do script.
Execute o script Python.
Nota: Você pode precisar ajustar o valor do limiar dependendo da distância da câmera à face (threshold), da qualidade da webcam, entre outros fatores.
