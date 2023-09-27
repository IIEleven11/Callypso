import torch
from TTS.utils.io import load_checkpoint
from TTS.utils.audio import AudioProcessor
from TTS.utils.generic_utils import setup_model
import json


def get_voice_model():
    model_path = "H:\\PROGRAMS\\SmolDev\\CallypsoTraining.pth"
    config_path = "H:\\PROGRAMS\\SmolDev\\Callypso\\config.json"  # Assuming the config file is in the same directory

    # load model
    num_chars, model, _ = load_checkpoint(model_path)
    model.eval()

    # load config
    with open(config_path, "r") as cf:
        config = json.load(cf)

    # setup audio processor
    ap = AudioProcessor(**config.audio)

    return model, config, ap


def generate_voice_response(text, model, config, ap):
    # synthesize voice
    (
        waveform,
        alignment,
        mel_spec,
        mel_postnet_spec,
        stop_tokens,
        inputs,
    ) = model.inference(text)

    # convert the waveform into an audio file
    voice_response = ap.save_wav(waveform, "response.wav")

    return voice_response
