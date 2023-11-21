# Updated-Impossible-Game-Bot
The is an updated version of the impossible game bot. My previous version is incomplete and inconsistent. This is because I made the mistake of taking on too much at once. I plan on breaking down this project into much smaller chunks know that I have a better idea of the step-by-step process. Here's an outline:

1. Create a program that will have the capability to precisely click any icon/image that is fed to it. Precision is key! It should account for items such as screen resolution and resizing. (Template Matching)\
   I. The program should have the capability to view a window in near real-time capabilities\
   II. The program should take in an image and perform the necessary adjustments for matching\
   III. The program should detect the image on-screen and appropriately navigate the mouse to the correct location and click
   
3. Create a program that will have the capability to listen for a specific .wav sound file. If heard, a ping should be sent by the code indicating the sound is played\
  I. Utilize librosa library for audio processing and perform MFCC on initial .wav file\
  II. (Optional) Manually code a MFCC audio processing procedure\
  III. Detect incoming audio and listen for initial .wav file sounds\
  IV. Send a ping when .wav file sound is detected

4. Create a reinforcement bot that relies on death sounds to learn and make adjustments (through q-learning)\
   I. (to be determined)
