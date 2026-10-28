# Puntos de control de la práctica guiada de Bazilio

Estos archivos acompañan al documento `Practica_Guiada_Interprete_Bazilio.docx`.
Cada `bazilio_etapaN.py` es el estado del intérprete al terminar la etapa N y se probó con los
programas de `programas/`.

| Archivo | Etapa | Qué agrega |
|---|---|---|
| `Bazilio.g4`, `analizar.py` | 1 | Lexer, parser y analizador |
| `bazilio_etapa2.py` | 2 | Variables, operadores, `<w>` y `<?>` |
| `bazilio_etapa3.py` | 3 | `if` / `else` y `while` |
| `bazilio_etapa4.py` | 4 | Procedimientos y recursividad |
| `bazilio_etapa5.py` | 5 | Notas, listas y errores |
| `bazilio_etapa6.py` | 6 | Música: LilyPond, MIDI, WAV y MP3 |

## Uso

    pip install antlr4-python3-runtime==4.13.2
    antlr4 -Dlanguage=Python3 -visitor Bazilio.g4       # genera el lexer y el parser

    python3 analizar.py programas/hello.bzl
    python3 bazilio_etapa2.py programas/e2_aritmetica.bzl
    python3 bazilio_etapa4.py programas/hanoi.bzl        # pide un entero por la entrada
    python3 bazilio_etapa6.py programas/hello.bzl        # genera .ly, PDF, MIDI, WAV y MP3

La etapa 6 necesita LilyPond, TiMidity++ (con un soundfont configurado) y ffmpeg.
