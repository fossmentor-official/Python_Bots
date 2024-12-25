import subprocess
import time
import pyautogui
from pynput.keyboard import Controller, Key

# Method to host a new meeting with video off and audio off
def zoom_automate(meeting_id, meeting_passcode):
    try:
        # Attempt to open Zoom app
        print("Attempting to open Zoom app...")
        subprocess.Popen(["/Applications/zoom.us.app/Contents/MacOS/zoom.us"])
        time.sleep(10)  # Allow time for the app to open
        print("Zoom app started successfully.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Ensure Zoom is installed and the path is correct.")
        return
    except Exception as e:
        print(f"Unexpected error while opening Zoom: {e}")
        return

    try:
        # Locate and click "Join a Meeting"
        print("Locating 'Join a Meeting' button...")
        join_a_meeting = pyautogui.locateOnScreen("trainer\\join1.png")
        if join_a_meeting is None:
            raise FileNotFoundError("Join button image not found.")
        pyautogui.click(join_a_meeting)
        print("'Join a Meeting' button clicked.")
        time.sleep(10)
    except Exception as e:
        print(f"Error locating 'Join a Meeting' button: {e}")
        return

    try:
        # Type the meeting ID
        print("Typing meeting ID...")
        pyautogui.typewrite(meeting_id)
        print("Meeting ID entered.")
    except Exception as e:
        print(f"Error entering meeting ID: {e}")
        return

    try:
        # Turn off video
        print("Locating 'Video Off' button...")
        video_off = pyautogui.locateOnScreen("trainer\\videooff.png")
        if video_off is None:
            raise FileNotFoundError("Video Off button image not found.")
        pyautogui.click(video_off)
        print("'Video Off' button clicked.")
    except Exception as e:
        print(f"Error locating 'Video Off' button: {e}")
        return

    try:
        # Click join button
        print("Locating 'Join' button...")
        join = pyautogui.locateOnScreen("trainer\\join2.png")
        if join is None:
            raise FileNotFoundError("Join button image not found.")
        pyautogui.click(join)
        print("'Join' button clicked.")
        time.sleep(10)
    except Exception as e:
        print(f"Error locating 'Join' button: {e}")
        return

    try:
        # Enter the meeting passcode
        print("Typing meeting passcode...")
        pyautogui.typewrite(meeting_passcode)
        print("Meeting passcode entered.")
    except Exception as e:
        print(f"Error entering meeting passcode: {e}")
        return

    try:
        # Click final join button
        print("Locating 'Final Join' button...")
        final_join = pyautogui.locateOnScreen("trainer\\finaljoin.png")
        if final_join is None:
            raise FileNotFoundError("Final Join button image not found.")
        pyautogui.click(final_join)
        print("'Final Join' button clicked.")
        time.sleep(30)  # Wait for host to admit
    except Exception as e:
        print(f"Error locating 'Final Join' button: {e}")
        return

    try:
        # Join with computer audio
        print("Locating 'Join with Computer Audio' button...")
        join_audio = pyautogui.locateOnScreen("trainer\\computeraudio.png")
        if join_audio is None:
            raise FileNotFoundError("Computer Audio button image not found.")
        pyautogui.click(join_audio)
        print("'Join with Computer Audio' button clicked.")
        time.sleep(1)
    except Exception as e:
        print(f"Error locating 'Join with Computer Audio' button: {e}")
        return

    try:
        # Mute using Alt+A shortcut
        print("Muting audio...")
        mute = Controller()
        mute.press(Key.alt_l)
        mute.press("a")
        mute.release("a")
        mute.release(Key.alt_l)
        print("Audio muted.")
    except Exception as e:
        print(f"Error muting audio: {e}")


# Automating Zoom Meeting
if __name__ == "__main__":
    try:
        meeting_id = input("Meeting Id: ")
        meeting_passcode = input("Meeting Passcode: ")
        print("\nZoom App is starting.......")
        zoom_automate(meeting_id, meeting_passcode)
    except Exception as e:
        print(f"Unexpected error in main program: {e}")
