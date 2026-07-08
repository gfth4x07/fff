Antes de usar os scripts é necessário executar uma vez `sudo pigpiod` para iniciar os pinos do Raspberry.

> [!NOTE]
>  Códigos com a tag `# PY5 IMPORTED MODE CODE` deve-se usar o Thonny com a opção _Imported mode for py5_ ativa

Python é muto chato para lidar com bibliotecas.
A biblioteca `keyboard` precisa ser instalada para isso usar `pip install keyboard` não basta.

É necessário usar `pip install keyboard --break-system-packeges` e além disso, para rodar precisa ser em sudo portanto usar `sudo python` não é suficiente por que esse comando roda uma versão diferente de python da que foi instalada a biblioteca.
Então é necessário usar `sudo -E python3`
