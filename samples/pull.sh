
# using https://github.com/ytdl-org/youtube-dl

youtube-dl -x --audio-format wav  `yq ".music[].yt" < music.yaml `
