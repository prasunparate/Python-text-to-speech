from gtts import gTTS
import os

def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='en')
    
    tts.save(output_file)
    print(f'Audio content written to file "{output_file}"')

if __name__ == "__main__":
    text = "Hello, world!, This is Prasun"
    output_file = "output.mp3"
    text_to_speech(text, output_file)
    
    # Play the audio file (optional)
    os.system(f"start {output_file}")  # For Windows
    # os.system(f"afplay {output_file}")  # For macOS
    # os.system(f"xdg-open {output_file}")  # For Linux

