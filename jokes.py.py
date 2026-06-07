import asyncio
import pyjokes
import edge_tts

# Get a joke
joke = pyjokes.get_joke()

# Print the joke
print(joke)

async def main():
    voice = "en-GB-SoniaNeural"  # en-US-JennyNeural  en-US-AriaNeural en-GB-SoniaNeural
    communicate = edge_tts.Communicate(joke, voice)
    await communicate.save("joke.mp3")

asyncio.run(main())

print("Voice saved as joke.mp3")