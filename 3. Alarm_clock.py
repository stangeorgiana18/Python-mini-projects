# A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.

import beepy 
import time

def get_user_input():
    	
    while True:
        try:
            time_setting = input("Choose minutes or seconds (m/s): ")
            
            if time_setting.lower() not in ['m', 's']:
                raise ValueError("Invalid time setting. Choose 'm' or 's'.")

            time_value = input(f"How many {time_setting}?: ")
            
            if not time_value.isdigit():
                raise ValueError("Invalid input. Enter a valid number.")
            
            seconds = 60 * int(time_value) if time_setting.lower() == 'm' else int(time_value)
            
            return time_setting.lower(), seconds
        
        except ValueError as e:
            print(f"Error: {e}")



def wait_for_alarm(seconds):
    
	# set the current time
    current_time = time.time()
    while time.time() - current_time < seconds:
        time.sleep(1) # wait until checking the condition again
        

def main():
    try:
        time_setting, seconds = get_user_input()
       

        # wait for the alarm
        wait_for_alarm(seconds)

        # play the sound
        beepy.beep(sound=1)

        print("Alarm triggered. Exiting program.")
        
    except Exception as e:
        print(f"Error: {e}")

# check if the script is run as the main program or imported
if __name__ == "__main__":
    main()