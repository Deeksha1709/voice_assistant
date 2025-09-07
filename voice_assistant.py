import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig

# --- Load environment variables ---
load_dotenv()
AGENT_ID = os.getenv("AGENT_ID")
print("DEBUG: AGENT_ID =", os.getenv("AGENT_ID"))
API_KEY = os.getenv("API_KEY")
print("DEBUG: API_KEY starts with =", str(os.getenv("API_KEY"))[:5])


if not AGENT_ID or not API_KEY:
    raise RuntimeError("Missing AGENT_ID or API_KEY. Create a .env file based on .env.example and try again.")

# --- Customize assistant behavior (edit as you like) ---
user_name = os.getenv("USER_NAME", "Alex")
schedule = os.getenv("SCHEDULE", "Sales Meeting with Taipy at 10:00; Gym with Sophie at 17:00")
prompt = f"You are a helpful assistant. Your interlocutor has the following schedule: {schedule}."
first_message = f"Hello {user_name}, how can I help you today?"

# --- Configure conversation overrides ---
conversation_override = {
    "agent": {
        "prompt": {"prompt": prompt},
        "first_message": first_message,
    },
}

config = ConversationConfig(
    conversation_config_override=conversation_override,
    extra_body={},
    dynamic_variables={},
    user_id="deeksha"
)

client = ElevenLabs(api_key=API_KEY)

# --- Callback handlers ---
def print_agent_response(response):
    print(f"Agent: {response}")

def print_interrupted_response(original, corrected):
    print(f"Agent interrupted, truncated response: {corrected}")

def print_user_transcript(transcript):
    print(f"User: {transcript}")

# --- Build conversation ---
conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),  # Uses your default Windows mic/speakers
    callback_agent_response=print_agent_response,
    callback_agent_response_correction=print_interrupted_response,
    callback_user_transcript=print_user_transcript,
)

if __name__ == "__main__":
    print("Starting your voice assistant... Speak into your microphone.")
    conversation.start_session()
