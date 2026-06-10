from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT = """Eres un tutor socrático. Tu único objetivo es guiar al usuario a descubrir las respuestas por sí mismo, nunca dándolas directamente.

Cuando el usuario presente un problema o pregunta:
- Responde siempre con una pregunta que lo acerque un paso más a la solución
- Si está en la dirección correcta, has preguntas que afirmen y profundicen su razonamiento
- Si está equivocado, has preguntas que lo lleven a detectar el error por sí mismo
- Solo confirma cuando el usuario llegue a la respuesta correcto con sus propias palabras
- Nunca des código, soluciones ni respuestas directas

Tono: paciente, alentador, curioso. Trata al usuario como alguien capaz de llegar solo."""

def main():
    client = Anthropic()
    history = []

    print("Tutor Socrático — escribe 'salir' para terminar\n")

    while True:
        user_input = input("Tú: ").strip()

        if not user_input:
            continue
        if user_input.lower() in ("salir", "exit", "quit"):
            print("¡Hasta luego!")
            break

        history.append({"role": "user", "content": user_input})

        print("Tutor: ", end="", flush=True)
        with client.messages.stream(
            model="claude-opus-4-8",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=history,
        ) as stream:
            response_text = ""
            for text in stream.text_stream:
                print(text, end="", flush=True)
                response_text += text

        print("\n")
        history.append({"role": "assistant", "content": response_text})

if __name__ == "__main__":
    main()
