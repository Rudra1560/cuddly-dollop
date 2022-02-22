import pathlib
import csv


subjects_list = []
start_hour = 8 
next_hour = 9 
school_days = [
	'monday',
	'tuesday'
]
time_slot_list = [] 
subject_per_slot = {}
MAX_HOUR_PER_SUBJECT = 6 
subject_hour_count = {}

def fill_out_subjects_list():
	

	subjects = input('Type all subjects you want add in subjects list\
and separate them by comma: ')

	the_subjects = subjects.replace(', ', ',')

	the_subjects = the_subjects.split(',')

	for subject in the_subjects:
		subject = subject.capitalize()

		if not subject in subjects_list:
			subjects_list.append(subject)
			subject_hour_count[subject] = MAX_HOUR_PER_SUBJECT

def ask_hour():
    
	print(f'Subjects list: {subjects_list}')

	print(f'Planning time: {start_hour}h-{next_hour}h')
	user_answer = input('What\'s subject do you want put here? ')

	return user_answer

def fill_in_timetable():
	global start_hour
	global next_hour

	for day in school_days:
		the_hour = {}
		time = 0
		start_hour = 8 # we suppose that school start at 8.am
		next_hour = 9

		print('\n---------------------------')
		print(f'{day.capitalize()} timetable')
		print('---------------------------\n')

		while time < 4: 

			hour_format = f'{start_hour}h-{next_hour}h' 
			
			if time == 2: 
				subject_per_slot[hour_format] = ['Break time']

				
				if not hour_format in time_slot_list:
					time_slot_list.append('hour_format')
				
			else:
				chosen_subject = ask_hour().capitalize()
				print(f'start_hour: {start_hour}')
				print(f'next_hour: {next_hour}')

				
				while not chosen_subject in subjects_list:
					print(f'{chosen_subject} is not in subjects list.')
					print('Choose another subject.')
					chosen_subject = ask_hour().capitalize()

				
				if not hour_format in time_slot_list:
					time_slot_list.append(hour_format)
					subject_per_slot[hour_format] = [chosen_subject]
				else:
					subject_per_slot[hour_format] += [chosen_subject]

				
				for subject, max_hour in subject_hour_count.items():
					if chosen_subject == subject:
						
						subject_hour_count[chosen_subject] = max_hour - 1

			
			start_hour += 1
			next_hour += 1
			time += 1



fill_out_subjects_list()
fill_in_timetable()
print(f'Subject per slot: {subject_per_slot}')

timetable_path = pathlib.Path.cwd() / 'timetable.csv'


with open(timetable_path, 'w') as timetable_file:
	timetable_writing = csv.writer(timetable_file)


	csv_headers = ['Hours']
	csv_headers.extend(school_days)
	timetable_writing.writerow(csv_headers)

	for time_slot, concerned_subjects in subject_per_slot.items():
		time_line = [time_slot]
		concerned_subjects_list = []

		if concerned_subjects == ['Break time']:
			for x in range(0, len(school_days)):
				concerned_subjects_list.append('Break time')
		else:
			concerned_subjects_list = concerned_subjects

		final_line = time_line + concerned_subjects_list
		timetable_writing.writerow(final_line)
	print('Your timetable is ready')
