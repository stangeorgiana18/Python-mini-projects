# A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.

import beepy 
import time

def get_user_input():
    	
    time_setting = input("Choose minutes or seconds (m/s): ")
    time_value = input(f"How many {time_setting}?: ")

    return time_setting.lower(), time_value


def convert_to_seconds(time_setting, time_value):
    	
    if time_setting not in ['m', 's']:
        raise ValueError("Invalid time setting. Choose 'm' or 's'.")
    
    try:
        return 60 * int(time_value) if time_setting == 'm' else int(time_value)
    
    except ValueError as e:
        raise ValueError("Invalid time or duration. Enter a valid number.") from e

def wait_for_alarm(seconds):
    
	# set the current time
    current_time = time.time()
    while time.time() - current_time < seconds:
        time.sleep(1) # wait until checking the condition again
        

def main():
    try:
        time_setting, time_value = get_user_input()
        seconds = convert_to_seconds(time_setting, time_value)

        # wait for the alarm
        wait_for_alarm(seconds)

        # play the sound
        beepy.beep(sound=1)

        print("Alarm triggered. Exiting program.")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()