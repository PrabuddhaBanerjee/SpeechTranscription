import streamlit as st
import websockets
import asyncio
import base64
import json
from configure import auth_key
from googletrans import Translator
from gtts import gTTS
import os
os.system("pipwin install pyaudio")
import pyaudio
import assemblyai as aai
import speech_recognition as sr


if 'text' not in st.session_state:
	st.session_state['text'] = 'Listening...'
	st.session_state['run'] = False

 
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
p = pyaudio.PyAudio()
 
# starts recording
stream = p.open(
   format=FORMAT,
   channels=CHANNELS,
   rate=RATE,
   input=True,
   frames_per_buffer=FRAMES_PER_BUFFER
)


def start_listening():
	"""
	start_listening(): Start Listening method is utilsed to activate the listening functionality of app
	and setting Playback button to reset
	"""
	st.session_state['run'] = True
	st.session_state.play_back = False

def stop_listening():
	"""
	stop_listening(): Stop Listening method is utilsed to deactivate the listening functionality of app
	momentarily and setting Playback button to active and playing the last transcribed text
	"""
	st.session_state['run'] = False
	st.session_state.play_back = True
	playback('current_transcript.mp3')

def start_playback():
	"""
	start_playback(): Start Playback method is utilsed to deactivate the listening functionality of app
	momentarily and setting Playback button to active and playing the all transcribed text.
	"""
	st.session_state['run'] = False
	st.session_state.play_back = True
	playback('transcript.mp3')
		
st.title('Healthcare Translation Web App with Generative AI')
st.markdown('_Currently this application is available to translate speech English, French, Spanish, Italian and Hindi only._')

# Creating Columns
start, stop = st.columns(2)

# Dropdown for Input from Speaker to specify their language of conversation
st.markdown('Speakers Language')
input_options = ["English", "Spanish", "French","Italian", "Hindi"]
selected_input_option = st.selectbox("Select an option:",input_options)

# Dropdown for Input from Speaker to specify their output of conversation
st.markdown('Translated Language')
output_options = ["Translate to English", "Translate to Spanish", "Translate to French","Translate to Italian", "Translate to Hindi"]
selected_output_option = st.selectbox("Select an option:",output_options)

# Initializing Start Listening Button
start.button('Start listening', on_click=start_listening)

# Initializing Stop Listening Button
stop.button('Stop listening', on_click=stop_listening)

if 'play_back' not in st.session_state:
    st.session_state.play_back = False

# Assembly AI endpoint
URL = "wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000"

# Initializing source input language and destination language.
src_lang, dest_lang = ''

# Transcription of real time audio
recon = sr.Recognizer()

async def send_receive():
	"""
	send_receive(): This function is called when the connection has been established.
	"""
	global dest_lang
	global src_lang
	print(f'Connecting websocket to url ${URL}')

	async with websockets.connect(
		URL,
		extra_headers=(("Authorization", auth_key),),
		ping_interval=5,
		ping_timeout=20
	) as _ws:

		r = await asyncio.sleep(0.1)
		print("Receiving SessionBegins ...")

		session_begins = await _ws.recv()
		print(session_begins)
		print("Sending messages ...")

		async def send():
			"""
			send(): This function is called when the connection has been established and is ready to send data.
			"""
			while st.session_state['run']:
				if selected_input_option != 'English':
					with sr.Microphone() as source:
						print(dest_lang)
						if selected_input_option == 'Spanish':
								input_lang = 'es'
						elif selected_input_option == 'French':
							input_lang = 'fr'
						elif selected_input_option == 'Hindi':
							input_lang = 'hi'
						elif selected_input_option == 'Italian':
							input_lang = 'it'

						if selected_output_option == 'Translate to Spanish':
								out_lang = 'es'	
						elif selected_output_option == 'Translate to French':
							out_lang = 'fr'
						elif selected_output_option == 'Translate to Hindi':
							out_lang = 'hi'
						elif selected_output_option == 'Translate to Italian':
							out_lang = 'it'
						else: out_lang = 'en'	
						st.session_state['run'] = True
						audio = recon.listen(source)
						translator = Translator()
				try:
					if selected_input_option != 'English':
						text = recon.recognize_google(audio, language=input_lang)
						translations = await translator.translate(text, src=input_lang, dest=out_lang )
						st.write("Speakers Transcription: " + text)
						st.write("Translated Transcription: ",translations.text)
						# Check if file path exists
						file_path = "transcript.txt"
							
						# File Path existst then append
						if os.path.exists(file_path):
							print("File exists")
							create_file = open("transcript.txt", "a")
							create_file.write(translations.text)
							create_file.close()
						else:
							create_file = open("transcript.txt", "w")
							create_file.write(translations.text)
							create_file.close()
							
						myobj = gTTS(text=translations.text, lang=out_lang, slow=False)
						# print("Translated")
						create_file.close()
						file = "current_transcript.mp3"
						myobj.save(file)

					else: 
						data = stream.read(FRAMES_PER_BUFFER)
						data = base64.b64encode(data).decode("utf-8")
						json_data = json.dumps({"audio_data":str(data)})
						r = await _ws.send(json_data)

				except websockets.exceptions.ConnectionClosedError as e:
					print(e)
					assert e.code == 4008
					break

				except Exception as e:
					print(e)
					assert False, "Not a websocket 4008 error"

				r = await asyncio.sleep(0.01)

		async def receive():
			"""
			recieve(): This function is called when the connection has been established and is ready to recieve data.
			"""
			while st.session_state['run']:
					try:
						result_str = await _ws.recv()
						result = json.loads(result_str)['text']

						if json.loads(result_str)['message_type']=='FinalTranscript':
							print(result)
							st.session_state.play_back = False
							
							if selected_input_option == 'Spanish':
								src_lang = 'es'
							elif selected_input_option == 'French':
								src_lang = 'fr'
							elif selected_input_option == 'English':
								src_lang = 'en'
							elif selected_input_option == 'Hindi':
								src_lang = 'hi'
							elif selected_input_option == 'Italian':
								src_lang = 'it'
							
							
							if selected_output_option == 'Translate to Spanish':
								dest_lang = 'es'
							elif selected_output_option == 'Translate to English':
								dest_lang = 'en'
							elif selected_output_option == 'Translate to French':
								dest_lang = 'fr'
							elif selected_output_option == 'Translate to Hindi':
								dest_lang = 'hi'
							elif selected_output_option == 'Translate to Italian':
								dest_lang = 'it'
								
							st.session_state['text'] = result
							
							#Translate
							translator = Translator()
							translations_from = await translator.translate(st.session_state['text'], src=dest_lang, dest=dest_lang)
							st.write("Speakers Transcription:", translations_from.text)
							translations = await translator.translate(translations_from.text, src=src_lang, dest=dest_lang )
							st.write("Translated Transcription:", translations.text)
							
							# Check if file path exists
							file_path = "transcript.txt"
							
							# File Path existst then append
							if os.path.exists(file_path):
								print("File exists")
								create_file = open("transcript.txt", "a")
								create_file.write(translations.text)
								create_file.close()
							else:
								create_file = open("transcript.txt", "w")
								create_file.write(translations.text)
								create_file.close()
								
							myobj = gTTS(text=translations.text, lang=dest_lang, slow=False)
							print("Translated")
							create_file.close()
							file = "current_transcript.mp3"
							myobj.save(file)
							
					except websockets.exceptions.ConnectionClosedError as e:
						print(e)
						assert e.code == 4008
						break

					except Exception as e:
						print(e)
						assert False, "Not a websocket 4008 error2"

		send_result, receive_result = await asyncio.gather(send(), receive())


st.markdown('---')

# Initializing Playback Button
st.button('Playback', on_click=start_playback)

def playback(file):
	"""
	playback(): This function is called when the playback option is called to play the transcripts.
	"""
	if selected_output_option == 'Translate to Spanish':
		dest_lang = 'es'
	elif selected_output_option == 'Translate to English':
		dest_lang = 'en'
	elif selected_output_option == 'Translate to French':
		dest_lang = 'fr'
	elif selected_output_option == 'Translate to Hindi':
		dest_lang = 'hi'
	elif selected_output_option == 'Translate to Italian':
		dest_lang = 'it'
	elif selected_output_option == 'Translate to Chinese(simplified)':
		dest_lang = 'zh-cn'
		
	# print('dest_lang',file)
	os.system("afplay " + file)
	st.session_state.play_back = False
	f = open("transcript.txt", "r")
	translat_lang = gTTS(text=f.read(), lang=dest_lang, slow=False)
	translat_lang.save("transcript.mp3")

if st.session_state.play_back:
	playback('transcript.mp3')
	st.session_state.play_back = False
	
asyncio.run(send_receive())
