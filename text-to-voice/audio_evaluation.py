import google.generativeai as genai
import os
import mimetypes
from dotenv import load_dotenv
load_dotenv()
# Configure the Gemini API client
# Replace with your actual API key, or set it as an environment variable
# os.environ["GEMINI_API_KEY"] = "YOUR_API_KEY"
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
 
        # genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        # self.model = genai.GenerativeModel('gemini-2.5-flash')

def evaluate_grammar_from_audio(audio_file_path):
    """
    Evaluates the grammar of a voice recording using the Gemini API.

    Args:
        audio_file_path (str): The path to the audio file.
    
    Returns:
        str: The AI's response with grammar corrections and explanation.
    """
    try:
        # Determine the MIME type of the audio file
        mime_type, _ = mimetypes.guess_type(audio_file_path)
        if not mime_type or not mime_type.startswith('audio/'):
            raise ValueError("File is not a valid audio format.")

        # Upload the audio file to the Gemini API
        print(f"Uploading file: {audio_file_path}...")
        uploaded_file = genai.upload_file(path=audio_file_path, display_name=os.path.basename(audio_file_path))
        print("File uploaded. Waiting for processing...")
        
        # Poll for file processing completion (optional, but good practice)
        # This step is for demonstration; the API call handles timing automatically.
        # file_info = genai.get_file(uploaded_file.name)
        # while file_info.state == 'PROCESSING':
        #     print("File processing...")
        #     time.sleep(5)
        #     file_info = genai.get_file(uploaded_file.name)

        # Define the prompt for grammar evaluation
        prompt = (
            "You are a grammar expert. Analyze the grammar of the following "
            "audio transcription. First, provide the corrected text. "
            "Then, in a new paragraph, list and explain the specific grammar "
            "mistakes and changes made."
        )
        
        # Send the prompt and the uploaded file to the Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([prompt, uploaded_file])
        
        # Clean up the uploaded file
        genai.delete_file(uploaded_file.name)
        print("Uploaded file deleted.")
        
        return response.text

    except Exception as e:
        return f"An error occurred: {e}"

# --- Example Usage ---
if __name__ == "__main__":
    # Create a dummy audio file for demonstration. 
    # In a real scenario, you would use a pre-existing audio file.
    # For a real voice recording, make sure the audio is clear.
    try:
        import wave
        import struct
        
        print("Creating a dummy audio file...")

        filename = "recorded_audio.wav"
        duration = 2  # seconds
        sample_rate = 44100
        num_channels = 1
        sampwidth = 2 # 16-bit
        num_frames = duration * sample_rate
        
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(num_channels)
            wf.setsampwidth(sampwidth)
            wf.setframerate(sample_rate)
            for _ in range(num_frames):
                wf.writeframes(struct.pack('<h', 0)) # write silent frame

        print(f"Dummy audio file '{filename}' created.")
        
        # You will need to replace this with your actual audio file path.
        audio_path = filename
        if not os.path.exists(audio_path):
            print(f"Error: The audio file '{audio_path}' was not found.")
        else:
            print("\nEvaluating grammar...")
            result = evaluate_grammar_from_audio(audio_path)
            print("\n--- Gemini API Response ---")
            print(result)

            # Clean up the dummy file
            os.remove(filename)

    except ImportError:
        print("A required library was not found. Skipping dummy file creation.")
        print("To run this example, create your own audio file and replace 'test_audio.wav'.")
    except Exception as e:
        print(f"An error occurred during execution: {e}")
