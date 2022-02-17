# BLINDA
Es un proyecto que utiliza la inteligencia artificial para ayudar a las personas ciegas o con baja visión. El proyecto consiste en, con una cámara detectar el objeto que tienes delante y a través de un auricular o altavoz escuchar qué objeto se está detectando. Todo este proceso se realiza a través de inteligencia artificial.

Cabe destacar que BLINDA de momento sólo está disponible en idioma inglés, pero se espera que en un futuro integre más idiomas.

En esta guía describiremos paso a paso todo lo que debes de hacer para poder recrear BLINDA.
### Tabla de contenido
- Materiales
- Detección de objetos
- Speak
- Fuente de alimentación
- Puesta en marcha

### MATERIALES
Los materiales utilizados son los siguientes:

- Jetson Nano 2GB o 4GB (En nuestro caso se ha usado la de 2GB)
- Cámara ArduCam 12MP IMX477
- TECNOIOT LTC1871 DC DC Step Up Booster Converter
- MOSFET IRFP9240
- Transistor BD139
- Resitencia 10 Ohmios
- Resistencia 2k2 Ohmios
- Potenciometro 5k Ohmios
- Resistencia 100k Ohmios
- TL431
- Condensador 1nF
- Bateria de Li-Po 3.7V 3000mAh
- Switch
- Conectores DC Jack
- Diodo tipo Schottky 1N5818
- Pines para PCB

### DETECCIÓN DE OBJETOS

Usaremos un repositorio que utiliza NVIDIA TensorRT para implementar eficientemente las redes neuronales en la plataforma de la Jetson Nano, mejorando el rendimiento y la eficiencia energética mediante optimizaciones de gráficos, fusión de kernel y precisión FP16/INT8.
Este repositorio viene con una serie de redes pre-entrenadas, que se pueden cargar en la jetson nano, que se descargan cuando descargas el repositorio

Para ello hacemos uso de los siguientes comando:

```
$ sudo apt-get update
$ sudo apt-get install git cmake libpython3-dev python3-numpy
$ git clone --recursive https://github.com/dusty-nv/jetson-inference
$ cd jetson-inference
$ mkdir build
$ cd build
$ cmake ../
$ make -j$(nproc)
$ sudo make install
$ sudo ldconfig
```

