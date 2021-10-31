"""Audio-to-Text

This module contains a terminal-based audio-to-text converter.
"""

import speech_recognition as sr
import os
import time
from pydub import AudioSegment
from pydub.silence import split_on_silence


# Banner
banner = r'''

	          ______   ______
	  /  \   |__  __| |__  __|
	 / /\ \    |  |     |  |
	/_/  \_\   |__|     |__|

	by Sven Eschlbeck


	Enter 'q' to quit.
'''

# Printing the banner
print(banner)

# Listing the languages that can be detected
prompt = r"""
Please specify the language of the submitted YouTube video.
Press '1' for French.			Press '2' for German.			Press '3' for Italian.
Press '4' for Russian.			Press '5' for Dutch.			Press '6' for Mandarin (Han Yu).
Press '7' for Spanish.  		Press '8' for Turkish.  		Press '9' for Swedish.
Press '10' for Portuguese.		Press '11' for Japanese.  		Press '12' for Korean.
Press '13' for Polish. 			Press '14' for Czech.  			Press '15' for Finnish.
Press '16' for Hebrew. 			Press '17' for Hungarian.		Press '18' for Indonesian.
Press '19' for Malaysian.		Press '20' for Norwegian.		Press '21' for Romanian.
Press '22' for Serbian.   		Press '23' for Slovak.   		Press '24' for Afrikaans.
Leave blank for default (English).
"""

# Starting main while loop
print("-----------------------------------------------------------------------------------------------------------------------------\n")
while True:
	# Asking user to specify the path to the audio file
	path = input("Please specify the full path to the audio file.\nYour entry should look like this: 'C:/User/.../file.wav'.\n")
	if path == 'q':
		break

	print("\n-----------------------------------------------------------------------------------------------------------------------------")
	lang = input(prompt)

	if lang == '1':
		language = 'fr-FR'
	if lang == '2':
		language = 'de-DE'
	if lang == '3':
		language = 'it-IT'
	if lang == '4':
		language == 'ru-RU'
	if lang == '5':
		language = 'nl-NL'
	if lang == '6':
		language = 'zh-CN'
	if lang == '7':
		language = 'es-ES'
	if lang == '8':
		language = 'tr'
	if lang == '9':
		language = 'sv-SE'
	if lang == '10':
		language = 'pt-PT'
	if lang == '11':
		language = 'ja'
	if lang == '12':
		language = 'ko'
	if lang == '13':
		language = 'pl'
	if lang == '14':
		language = 'cz'
	if lang == '15':
		language = 'fi'
	if lang == '16':
		language = 'he'
	if lang == '17':
		language = 'hu'
	if lang == '18':
		language = 'id'
	if lang == '19':
		language = 'ms-MY'
	if lang == '20':
		language = 'no-NO'
	if lang == '21':
		language = 'ro-RO'
	if lang == '22':
		language = 'sr-SP'
	if lang == '23':
		language = 'sk'
	if lang == '24':
		language = 'af'
	if lang == '':
		language = 'en-US'
	if lang == 'q':
		break

	# Creating a speech recognition object/ Initializing the recognizer
	r = sr.Recognizer()

	# Splitting the audio file into batches and applying speech recognition to the batches
	def get_large_audio_transcription(path):
		"""Splitting audio file into batches and applying speech recognition to each batch"""

		global whole_text # Necessary to access the variable later

		# Opening audio file using pydub
		sound = AudioSegment.from_wav(path)
		batches = split_on_silence(sound, min_silence_len = 500, silence_thresh = sound.dBFS-14, keep_silence = 500)

		# Creating directory to store the audio batches
		if not os.path.isdir('audio_batches'):
			os.mkdir('audio_batches')
		whole_text = ""

		# Process each batch
		for i, audio_batch in enumerate(batches, start=1):
			# Export audio batch and save it in 'audio_files/audio_batches'
			batch_filename = os.path.join('audio_batches', f"batch{i}.wav")
			audio_batch.export(batch_filename, format = 'wav')

			# Recognize the batch
			with sr.AudioFile(batch_filename) as source:
				audio_listened = r.record(source)

				# Trying to convert to text
				try:
					text = r.recognize_google(audio_listened, language = language)
				except sr.UnknownValueError as e:
					print("Error: ", str(e))
				else:
					text = f"{text.capitalize()}. "
					print(batch_filename, ": ", text)
					whole_text += text

		# Return the text for all batches in one piece
		return whole_text

	# Print text
	print("-----------------------------------------------------------------------------------------------------------------------------\n")
	print("Transcribing audio batchwise.\nThis may take a moment. ")
	animation = "|/-\\|/-\\"
	idx = 0
	while idx < 11:
	    print(animation[idx % len(animation)], end = "\r")
	    idx += 1
	    time.sleep(0.3)

	print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
	print("Creating directory 'audio_batches' to store audio chunks.")
	print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
	print("Full text:\n\n")
	print(get_large_audio_transcription(path))
	print("\n-----------------------------------------------------------------------------------------------------------------------------\n")

	question_save = input("Do you want to save the transcription to a text file? [y/n]\n")
	if question_save == 'y':
		# Ask for the destination folder where the text should be stored
		destination_folder = input("\nPlease specify the full path to the desired destination folder.\nYour entry should look like this: 'C:/User/.../folder'.\n")

		# Aborting if a 'q' is given
		if destination_folder == 'q':
			break

		# Ask for the file name
		file_name = input("\nPlease specify the desired file name.\nYour entry should look like this: 'example_file.txt'.\n")

		# Aborting if a 'q' is given
		if file_name == 'q':
			break

		# Creating individual user path from destination folder and file name
		user_path = f"{destination_folder}/{file_name}"
		with open(user_path, 'w') as f:
			# Write the text into the file
			f.write(f"{whole_text}")

		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
		print("Your text file is created.\nGo to the specified folder to access it.")
		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")

	if question_save == 'n':
		pass
	if question_save == 'q':
		break

	# Asking user if he/she wishes to continue
	question_more = input("\nDo you wish to convert another file? [y/n]\n")
	if question_more == 'y':
		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
		continue
	if question_more == 'n':
		break
	if question_more == 'q':
		break