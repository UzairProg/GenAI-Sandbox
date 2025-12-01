# Multimodal AI - Notes

## What is Multimodal?
AI models that can process and generate **multiple types of data** (text, images, audio, video) in a single system.

## Input Modalities

### Text
- Natural language queries, prompts, documents
- Traditional LLM input

### Images
- Photos, screenshots, diagrams, charts
- Model analyzes visual content and context
- Example: "What's in this image?" with a photo

### Audio
- Speech, music, sound effects
- Can transcribe or understand audio content
- Example: Voice commands, podcast analysis

### Video
- Sequences of frames + audio
- Temporal understanding of events
- Example: "Summarize this video clip"

## Output Modalities

### Text
- Generated responses, explanations, code
- Most common output format

### Images
- Generated artwork, edited photos, diagrams
- Models: DALL-E, Midjourney, Stable Diffusion

### Audio
- Text-to-speech, music generation
- Models: Whisper (speech), MusicLM

### Video
- Generated video clips from text/images
- Models: Sora, Runway, Pika

## Combined (Input → Output)

| Input | Output | Use Case |
|-------|--------|----------|
| Text | Image | "Draw a sunset over mountains" |
| Image | Text | "Describe this medical scan" |
| Audio | Text | Speech-to-text transcription |
| Text | Audio | Text-to-speech, podcast generation |
| Image + Text | Text | "What brand is this logo?" + image |
| Video | Text | Video summarization, captioning |
| Text | Video | "Generate a 5-second clip of waves" |

## Popular Multimodal Models

- **GPT-4 Vision (GPT-4V)**: Text + Image → Text
- **Gemini**: Text, Image, Audio, Video → Text
- **Claude 3**: Text + Image → Text
- **DALL-E 3**: Text → Image
- **Whisper**: Audio → Text
- **Sora**: Text → Video

## Why Multimodal Matters

1. **Richer Context**: Understanding images/audio provides deeper insights
2. **Broader Applications**: Medical imaging, accessibility tools, content creation
3. **Natural Interaction**: Humans communicate with more than just text
4. **Complex Tasks**: "Fix the bug in this screenshot" requires visual understanding

## Key Challenges

- **Alignment**: Ensuring different modalities work together coherently
- **Data Requirements**: Need large paired datasets (image + caption, audio + transcript)
- **Computational Cost**: Processing multiple modalities is resource-intensive
- **Hallucination**: Models may "see" things not actually in images/videos
