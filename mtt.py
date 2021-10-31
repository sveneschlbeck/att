"""Microphone-to-Text

This module contains a terminal-based microphone-to-text converter.
"""

import speech_recognition as sr
import os
import time
from pydub import AudioSegment
from pydub.silence import split_on_silence


# Banner
banner = r'''

	 _    _    ______   ______
	| \__/ |  |__  __| |__  __|
	| |  | |    |  |     |  |
	|_|  |_|    |__|     |__|

	by Sven Eschlbeck


	Enter 'q' to quit.
'''

# Printing the banner
print(banner)

# Listing the languages that can be detected
prompt = r"""
Please specify the spoken language.
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
while True:

	print("-----------------------------------------------------------------------------------------------------------------------------")
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

	print("-----------------------------------------------------------------------------------------------------------------------------\n")

	# Asking for the duration of the planned recording
	length = input("How long do you plan to speak?\n\nDefine a time span.\nPress '1' for 30 seconds.\nPress '2' for 60 seconds.\nPress '3' for 90 seconds.\nPress '4' for 120 seconds.\nPress '5' for 300 seconds.\n\nLeave blank for default (10 seconds).\n")
	if length == '1':
		duration = 30
	if length == '2':
		duration = 60
	if length == '3':
		duration = 90
	if length == '4':
		duration = 120
	if length == '5':
		duration = 300
	if length == '':
		duration = 10
	if length == 'q':
		break

	# Initializing the recognizer
	r = sr.Recognizer()

	# Defining microphone as input source
	with sr.Microphone() as source:
		# Users starts speaking
		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
		print("Speak now!")
		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")

		# Read the audio data from the default microphone
		audio_data = r.record(source, duration = duration)

		# Printing wait statement
		print("Recognizing voice...\n")
		animation = "|/-\\|/-\\"
		idx = 0
		while idx < 11:
		    print(animation[idx % len(animation)], end="\r")
		    idx += 1
		    time.sleep(0.3)

		# Convert speech to text
		text = r.recognize_google(audio_data, language = language)

		# Print text
		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
		print(f"Record:\n{text}")
		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")

	question_save = input("Do you want to save the transcription to a text file? [y/n]\n")
	if question_save == 'y':
		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")

		# Ask for the destination folder where the text should be stored
		destination_folder = input("Please specify the full path to the destination folder.\nYour entry should look like this: 'C:/User/.../folder'.\n")

		# Aborting if a 'q' is given
		if destination_folder == 'q':
			break

		# Ask for the file name
		file_name = input("\nPlease specify the file name.\n")

		# Aborting if a 'q' is given
		if file_name == 'q':
			break

		# Creating individual user path from destination folder and file name
		user_path = f"{destination_folder}/{file_name}"
		with open(user_path, 'w') as f:
			# Write the text into the file
			f.write(f"{text}")

		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
		print("Your text file was created.\nGo to the specified folder to access it.")
		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")

	if question_save == 'n':
		pass
	if question_save == 'q':
		break

	question_more = input("Do you wish to record another speech? [y/n]\n")
	if question_more == 'y':
		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
		continue
	if question_more == 'n':
		break
	if question_more == 'q':
		break