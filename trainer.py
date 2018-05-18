#this is the code for beat and tempo extraction
#importing important libraries
import glob
import errno
import librosa
#give path for the music folder use wav format
path = r'.\*.wav'
files = glob.glob(path)
for name in files:
    try:
        with open(name) as f:
            y, sr = librosa.load(name)
            tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
            print(name)
            print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
            beat_times = librosa.frames_to_time(beat_frames, sr=sr)
            beat_times=int(sum(beat_times)/len(beat_times))
            print(beat_times)
            
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
