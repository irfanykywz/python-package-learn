import ffmpeg

# Retrieve information about the video
info = ffmpeg.probe('test.mp4')
video_info = next((stream for stream in info['streams'] if stream['codec_type'] == 'video'), None)
width = int(video_info['width'])
height = int(video_info['height'])

print(video_info)

"""
{
  'index': 0,
  'codec_name': 'h264',
  'codec_long_name': 'H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10',
  'profile': 'High',
  'codec_type': 'video',
  'codec_tag_string': 'avc1',
  'codec_tag': '0x31637661',
  'width': 720,
  'height': 1280,
  'coded_width': 720,
  'coded_height': 1280,
  'closed_captions': 0,
  'film_grain': 0,
  'has_b_frames': 2,
  'sample_aspect_ratio': '1:1',
  'display_aspect_ratio': '9:16',
  'pix_fmt': 'yuv420p',
  'level': 31,
  'color_range': 'tv',
  'color_space': 'bt709',
  'color_transfer': 'bt709',
  'color_primaries': 'bt709',
  'chroma_location': 'left',
  'field_order': 'progressive',
  'refs': 1,
  'is_avc': 'true',
  'nal_length_size': '4',
  'id': '0x1',
  'r_frame_rate': '21/1',
  'avg_frame_rate': '21/1',
  'time_base': '1/10752',
  'start_pts': 0,
  'start_time': '0.000000',
  'duration_ts': 260096,
  'duration': '24.190476',
  'bit_rate': '1028175',
  'bits_per_raw_sample': '8',
  'nb_frames': '508',
  'extradata_size': 45,
  'disposition': {
    'default': 1,
    'dub': 0,
    'original': 0,
    'comment': 0,
    'lyrics': 0,
    'karaoke': 0,
    'forced': 0,
    'hearing_impaired': 0,
    'visual_impaired': 0,
    'clean_effects': 0,
    'attached_pic': 0,
    'timed_thumbnails': 0,
    'captions': 0,
    'descriptions': 0,
    'metadata': 0,
    'dependent': 0,
    'still_image': 0
  },
  'tags': {
    'language': 'und',
    'handler_name': 'VideoHandler',
    'vendor_id': '[0][0][0][0]'
  }
}
"""