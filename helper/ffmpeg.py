import time
import os
import asyncio
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

async def fix_thumb(thumb):
    width = 0
    height = 0
    try:
        if thumb != None:
            metadata = extractMetadata(createParser(thumb))
            if metadata.has("width"):
                width = metadata.get("width")
            if metadata.has("height"):
                height = metadata.get("height")
                Image.open(thumb).convert("RGB").save(thumb)
                img = Image.open(thumb)
                img.resize((320, height))
                img.save(thumb, "JPEG")
    except Exception as e:
        print(e)
        thumb = None 
       
    return width, height, thumb
    
async def take_screen_shot(video_file, output_directory, ttl):
    # https://stackoverflow.com/a/13891070/4723940
    out_put_file_name = output_directory + \
        "/" + str(time.time()) + ".jpg"
    file_genertor_command = [
        "ffmpeg",
        "-ss",
        str(ttl),
        "-i",
        video_file,
        "-vframes",
        "1",
        out_put_file_name
    ]
    # width = "90"
    process = await asyncio.create_subprocess_exec(
        *file_genertor_command,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    if os.path.lexists(out_put_file_name):
        return out_put_file_name
    else:
        return None

async def generate_screen_shots(
    video_file,
    output_directory,
    is_watermarkable,
    wf,
    min_duration,
    no_of_photos
):
    metadata = extractMetadata(createParser(video_file))
    duration = 0
    if metadata is not None:
        if metadata.has("duration"):
            duration = metadata.get('duration').seconds
    if duration > min_duration:
        images = []
        ttl_step = duration // no_of_photos
        current_ttl = ttl_step
        for looper in range(0, no_of_photos):
            ss_img = await take_screen_shot(video_file, output_directory, current_ttl)
            current_ttl = current_ttl + ttl_step
            if is_watermarkable:
                ss_img = await place_water_mark(ss_img, output_directory + "/" + str(time.time()) + ".jpg", wf)
            images.append(ss_img)
        return images
    else:
        return None
