wget -r "https://imslp.org/wiki/Das_wohltemperierte_Klavier_I%2C_BWV_846-869_(Bach%2C_Johann_Sebastian)"
find  -name \*.ogg  -exec ffmpeg  -i "{}" "{}.wav"   \;
find  -name \*.mp3  -exec ffmpeg  -i "{}" "{}.wav"   \;

