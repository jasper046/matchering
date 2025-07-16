import matchering as mg

# Sending all log messages to the default print function
mg.log(print)

# Create a preset from the first reference track
mg.analyze_reference_track(
    reference="/home/jasper/Music/matchering/payback.wav",
    preset_path="preset1.pkl",
)

# Apply the first preset to the target track
mg.process_with_preset(
    target="/home/jasper/Music/matchering/LP13 PSYCHEDELISCH.wav",
    preset_path="preset1.pkl",
    results=[
        mg.pcm24("my_song_master_preset1.wav"),
    ],
)

# Create a preset from the second reference track
mg.analyze_reference_track(
    reference="/home/jasper/Music/matchering/sbmt.wav",
    preset_path="preset2.pkl",
)

# Blend the two presets
mg.blend_presets(
    preset_paths=["preset1.pkl", "preset2.pkl"],
    new_preset_path="blended_preset.pkl",
)

# Apply the blended preset to the target track
mg.process_with_preset(
    target="/home/jasper/Music/matchering/LP13 PSYCHEDELISCH.wav",
    preset_path="blended_preset.pkl",
    results=[
        mg.pcm24("my_song_master_blended.wav"),
    ],
)
