# from email.mime import audio
# import subprocess

# # cd /root
# # sudo apt-get update
# # sudo apt-get install git -y
# # sudo apt-get install wget
# # sudo apt install ffmpeg -y
# # sudo apt-get install libsndfile1 -y
# # sudo apt install -y libsm6 libxext6
# # sudo apt-get install pip -y

# # python3.7 -m pip install youtube_dl
# # hash youtube-dl

# # python3.7 -m pip install --upgrade pip setuptools wheel

# # python3.7 -m pip install requests 

# # python3.7 -m pip install numpy==1.17.1
# # python3.7 -m pip install Cython==0.29.32
# # python3.7 -m pip install numba==0.48
# # python3.7 -m pip install librosa==0.7.0

# # python3.7 -m pip install opencv-contrib-python==4.6.0.66
# # python3.7 -m pip install opencv-python==4.1.0.25

# # python3.7 -m pip install tqdm==4.45.0

# # python3.7 -m pip install torch==1.1.0
# # python3.7 -m pip install torchvision==0.3.0


# # wget "https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth" -O "face_detection/detection/sfd/s3fd.pth"
# # wget "https://mcgggn.s3.ap-south-1.amazonaws.com/docs/wav2lip_gan.pth" -O "checkpoints/wav2lip_gan.pth"
# # wget "https://mcgggn.s3.ap-south-1.amazonaws.com/docs/wav2lip.pth" -O "checkpoints/wav2lip.pth"
# # wget "https://storage.googleapis.com/justbaat-dev.appspot.com/audio/lipsync_expert.pth" -O "checkpoints/lipsync_expert.pth"

# # The following commands need to be run from inside the root directory, optimus

# # print(f"\nMaking the data directory structure")
# # make_custom_data_directory = 'mkdir -p data_root/custom/ankur_warikoo'
# # subprocess.run(make_custom_data_directory, shell=True)

# # print(f"\nDownloading Ankur Warikoo video from YouTube")
# # # youtube-dl -F https://www.youtube.com/watch?v=HNPbY6fSeo8 # to find out all the qualities available to be downloaded
# # download_warikoo_video = "cd data_root/custom/ankur_warikoo && youtube-dl -f 22 -w https://www.youtube.com/watch?v=HNPbY6fSeo8" # -w skips the already downloaded video
# # subprocess.run(download_warikoo_video, shell=True)

# # video_trimming_commands = [
# #     "ffmpeg -i 'data_root/custom/ankur_warikoo/STOCK MARKET INVESTING for BEGINNERS! _ Investment Tips 2022 _ Warikoo Hindi-HNPbY6fSeo8.mp4' -ss 00:01:44 -to 00:01:54 'data_root/custom/ankur_warikoo/clip1.mp4'",
# #     "ffmpeg -i 'data_root/custom/ankur_warikoo/STOCK MARKET INVESTING for BEGINNERS! _ Investment Tips 2022 _ Warikoo Hindi-HNPbY6fSeo8.mp4' -ss 00:01:54 -to 00:02:04 'data_root/custom/ankur_warikoo/clip2.mp4'",
# #     "ffmpeg -i 'data_root/custom/ankur_warikoo/STOCK MARKET INVESTING for BEGINNERS! _ Investment Tips 2022 _ Warikoo Hindi-HNPbY6fSeo8.mp4' -ss 00:02:04 -to 00:02:14 'data_root/custom/ankur_warikoo/clip3.mp4'",
# #     "ffmpeg -i 'data_root/custom/ankur_warikoo/STOCK MARKET INVESTING for BEGINNERS! _ Investment Tips 2022 _ Warikoo Hindi-HNPbY6fSeo8.mp4' -ss 00:02:14 -to 00:02:24 'data_root/custom/ankur_warikoo/clip4.mp4'",

# #     "ffmpeg -i 'data_root/custom/ankur_warikoo/STOCK MARKET INVESTING for BEGINNERS! _ Investment Tips 2022 _ Warikoo Hindi-HNPbY6fSeo8.mp4' -ss 00:02:44 -to 00:02:54 'data_root/custom/ankur_warikoo/clip5.mp4'",
# #     "ffmpeg -i 'data_root/custom/ankur_warikoo/STOCK MARKET INVESTING for BEGINNERS! _ Investment Tips 2022 _ Warikoo Hindi-HNPbY6fSeo8.mp4' -ss 00:02:54 -to 00:03:01 'data_root/custom/ankur_warikoo/clip6.mp4'",

# #     "ffmpeg -i 'data_root/custom/ankur_warikoo/STOCK MARKET INVESTING for BEGINNERS! _ Investment Tips 2022 _ Warikoo Hindi-HNPbY6fSeo8.mp4' -ss 00:03:06 -to 00:03:16 'data_root/custom/ankur_warikoo/clip7.mp4'",
# #     "ffmpeg -i 'data_root/custom/ankur_warikoo/STOCK MARKET INVESTING for BEGINNERS! _ Investment Tips 2022 _ Warikoo Hindi-HNPbY6fSeo8.mp4' -ss 00:03:16 -to 00:03:26 'data_root/custom/ankur_warikoo/clip8.mp4'",
# #     "ffmpeg -i 'data_root/custom/ankur_warikoo/STOCK MARKET INVESTING for BEGINNERS! _ Investment Tips 2022 _ Warikoo Hindi-HNPbY6fSeo8.mp4' -ss 00:03:26 -to 00:03:30 'data_root/custom/ankur_warikoo/clip9.mp4'",
# #     "ffmpeg -i 'data_root/custom/ankur_warikoo/STOCK MARKET INVESTING for BEGINNERS! _ Investment Tips 2022 _ Warikoo Hindi-HNPbY6fSeo8.mp4' -ss 00:03:39 -to 00:03:49 'data_root/custom/ankur_warikoo/clip10.mp4'",
# #     "ffmpeg -i 'data_root/custom/ankur_warikoo/STOCK MARKET INVESTING for BEGINNERS! _ Investment Tips 2022 _ Warikoo Hindi-HNPbY6fSeo8.mp4' -ss 00:03:49 -to 00:03:59 'data_root/custom/ankur_warikoo/clip11.mp4'",
# #     "ffmpeg -i 'data_root/custom/ankur_warikoo/STOCK MARKET INVESTING for BEGINNERS! _ Investment Tips 2022 _ Warikoo Hindi-HNPbY6fSeo8.mp4' -ss 00:03:59 -to 00:04:09 'data_root/custom/ankur_warikoo/clip12.mp4'",
# #     "ffmpeg -i 'data_root/custom/ankur_warikoo/STOCK MARKET INVESTING for BEGINNERS! _ Investment Tips 2022 _ Warikoo Hindi-HNPbY6fSeo8.mp4' -ss 00:04:09 -to 00:04:19 'data_root/custom/ankur_warikoo/clip13.mp4'",
# #     "ffmpeg -i 'data_root/custom/ankur_warikoo/STOCK MARKET INVESTING for BEGINNERS! _ Investment Tips 2022 _ Warikoo Hindi-HNPbY6fSeo8.mp4' -ss 00:04:19 -to 00:04:29 'data_root/custom/ankur_warikoo/clip14.mp4'",
# #     "ffmpeg -i 'data_root/custom/ankur_warikoo/STOCK MARKET INVESTING for BEGINNERS! _ Investment Tips 2022 _ Warikoo Hindi-HNPbY6fSeo8.mp4' -ss 00:04:29 -to 00:04:39 'data_root/custom/ankur_warikoo/clip15.mp4'",

# #     "ffmpeg -i 'data_root/custom/ankur_warikoo/STOCK MARKET INVESTING for BEGINNERS! _ Investment Tips 2022 _ Warikoo Hindi-HNPbY6fSeo8.mp4' -ss 00:04:45 -to 00:04:55 'data_root/custom/ankur_warikoo/clip16.mp4'",
# #     "ffmpeg -i 'data_root/custom/ankur_warikoo/STOCK MARKET INVESTING for BEGINNERS! _ Investment Tips 2022 _ Warikoo Hindi-HNPbY6fSeo8.mp4' -ss 00:04:55 -to 00:05:00 'data_root/custom/ankur_warikoo/clip17.mp4'"
# #     ]

# # print("\nTrimming videos")
# # for cmd_idx, cmd in enumerate(video_trimming_commands):
# #     print(f"\n>>> Trimming video #{cmd_idx+1}")
# #     subprocess.run(cmd, shell=True)   

# # print("\nDeleting the original video")
# # subprocess.run("rm -rf 'data_root/custom/ankur_warikoo/STOCK MARKET INVESTING for BEGINNERS! _ Investment Tips 2022 _ Warikoo Hindi-HNPbY6fSeo8.mp4'", shell=True)


# # python3.7 preprocess.py --batch_size 4 --data_root data_root/custom --preprocessed_root custom_preprocessed/
# # python3.7 wav2lip_train.py --data_root custom_preprocessed/ --checkpoint_dir wav2lip_ckpts --syncnet_checkpoint_path checkpoints/lipsync_expert.pth --checkpoint_path checkpoints/wav2lip.pth

# # import os
# # from glob import glob

# # p = "custom_preprocessed/ankur_warikoo/"
# # for i in range(1, 17+1):
# #     # print(f"-------\nclip{i}")
# #     files = sorted(glob(os.path.join(p, f"clip{i}", "*.jpg")))
# #     # print(len(files), files[:5], files[-5:])
# #     if len(files) == 0:
# #         print(f"DELETE DIRECTORY clip{i}")

# # data_root/custom/ankur_warikoo/
# # clip1.mp4   clip11.mp4  clip13.mp4  clip15.mp4  clip17.mp4  clip3.mp4   clip5.mp4   clip7.mp4   clip9.mp4   
# # clip10.mp4  clip12.mp4  clip14.mp4  clip16.mp4  clip2.mp4   clip4.mp4   clip6.mp4   clip8.mp4        

# # custom_preprocessed/ankur_warikoo/
# # clip10/ clip11/ clip12/ clip13/ clip14/ clip15/ clip16/ clip17/ clip2/  clip3/  clip4/  clip5/  clip6/  clip7/  clip8/  clip9/ 

# # eval every 10 epochs (100 steps)
# # L1: 0.02956991415956746, Sync loss: 1.027036318127413
# # L1: 0.026398279085200024, Sync loss: 1.0319932125369955
# # L1: 0.0251534758424907, Sync loss: 1.1191276804260586
# # L1: 0.023822497969828778, Sync loss: 1.129176222019314
# # L1: 0.02304582981543141, Sync loss: 1.2535146004664972 # >>> 252 396500 100 0
# # L1: 0.02266053646016195, Sync loss: 1.2443717529314646
# # L1: 0.02237203069355177, Sync loss: 1.2547436512034873

# # checkpoint_step000396250.pth 
# # checkpoint_step000396500.pth
# # checkpoint_step000396750.pth  

# # python3.7 inference.py --checkpoint_path checkpoints/wav2lip.pth                    --face "data_root/custom/ankur_warikoo/clip2.mp4" --audio "data_root/custom/ankur_warikoo/clip3.mp4" --outfile "results/v_clip2_a_clip3_000.mp4"
# # python3.7 inference.py --checkpoint_path wav2lip_ckpts/checkpoint_step000396250.pth --face "data_root/custom/ankur_warikoo/clip2.mp4" --audio "data_root/custom/ankur_warikoo/clip3.mp4" --outfile "results/v_clip2_a_clip3_250.mp4"
# # python3.7 inference.py --checkpoint_path wav2lip_ckpts/checkpoint_step000396500.pth --face "data_root/custom/ankur_warikoo/clip2.mp4" --audio "data_root/custom/ankur_warikoo/clip3.mp4" --outfile "results/v_clip2_a_clip3_500.mp4"
# # python3.7 inference.py --checkpoint_path wav2lip_ckpts/checkpoint_step000396750.pth --face "data_root/custom/ankur_warikoo/clip2.mp4" --audio "data_root/custom/ankur_warikoo/clip3.mp4" --outfile "results/v_clip2_a_clip3_750.mp4"

# # gsutil cp results/v_clip2_a_clip3_000.mp4 gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/examples_from_training_set/
# # gsutil cp results/v_clip2_a_clip3_250.mp4 gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/examples_from_training_set/
# # gsutil cp results/v_clip2_a_clip3_500.mp4 gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/examples_from_training_set/
# # gsutil cp results/v_clip2_a_clip3_750.mp4 gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/examples_from_training_set/



# # python3.7 -m pip install gdown

# lady_green_screen_download_commands = {
#     "00015.MTS": "cd data_root/custom/lady_green_screen/ && gdown https://drive.google.com/uc?id=1qSzmQPA7MH4pNYJj4AvaCIE5y4Ykr_31",
#     "00016.MTS": "cd data_root/custom/lady_green_screen/ && gdown https://drive.google.com/uc?id=1Q6VEaarX2mfLj6Xc49UdaggHiKJkLDsP",
#     "00018.MTS": "cd data_root/custom/lady_green_screen/ && gdown https://drive.google.com/uc?id=13eZb2fq4IjAkSZ8asuD1tzc8-mOJ7WDW",
#     "00019.MTS": "cd data_root/custom/lady_green_screen/ && gdown https://drive.google.com/uc?id=1-hZEUvaRxWVFg49f5uIP1CNfaZ64SUg5",
#     "00020.MTS": "cd data_root/custom/lady_green_screen/ && gdown https://drive.google.com/uc?id=1OP8dWtgw2FLsEXwdaM5asHKZk7j0i0HR"
# }

# make_custom_data_directory = 'mkdir -p data_root/custom/lady_green_screen/'
# subprocess.run(make_custom_data_directory, shell=True)

# for vid_name, download_command in lady_green_screen_download_commands.items():
#     subprocess.run(download_command, shell=True)

# # convert .MTS to .mp4
# for filename in lady_green_screen_download_commands:
#     command = f"ffmpeg -i data_root/custom/lady_green_screen/{filename} data_root/custom/lady_green_screen/{filename.split('.')[0]+'.mp4'}"
#     subprocess.run(command, shell=True)


# lady_green_screen_trim_timings = {
#     "00015.mp4": [
#         ["00:00:01", "00:00:05"], ["00:00:14", "00:00:19"], ["00:00:25", "00:00:30"], ["00:00:45", "00:00:55"],
#         ["00:00:55", "00:01:05"], ["00:01:05", "00:01:15"], ["00:01:15", "00:01:25"], ["00:01:25", "00:01:35"],
#         ["00:01:35", "00:01:45"], ["00:01:45", "00:01:55"], ["00:01:55", "00:02:05"], ["00:02:05", "00:02:15"],
#         ["00:02:15", "00:02:25"], ["00:02:25", "00:02:35"], ["00:02:35", "00:02:40"]
#                 ],

#     "00016.mp4": [
#         ["00:00:02", "00:00:06"]
#                 ],

#     "00018.mp4": [
#         ["00:00:01", "00:00:10"], ["00:00:10", "00:00:20"], ["00:00:20", "00:00:30"], ["00:00:30", "00:00:40"],
#         ["00:00:40", "00:00:50"], ["00:00:50", "00:01:00"], ["00:01:00", "00:01:10"], ["00:01:10", "00:01:20"],
#         ["00:01:20", "00:01:30"], ["00:01:30", "00:01:38"]
#                 ],

#     "00019.mp4": [
#         ["00:00:04", "00:00:10"], ["00:00:10", "00:00:20"], ["00:00:20", "00:00:30"], ["00:00:30", "00:00:40"], 
#         ["00:00:40", "00:00:50"], ["00:00:50", "00:01:00"], ["00:01:00", "00:01:10"], ["00:01:10", "00:01:16"]
#                 ],                

#     "00020.mp4": [
#         ["00:00:01", "00:00:10"], ["00:00:10", "00:00:20"], ["00:00:20", "00:00:30"], ["00:00:30", "00:00:40"],
#         ["00:00:40", "00:00:50"], ["00:00:50", "00:01:00"], ["00:01:00", "00:01:10"], ["00:01:10", "00:01:20"],
#         ["00:01:20", "00:01:30"], ["00:01:30", "00:01:40"], ["00:01:40", "00:01:50"], ["00:01:50", "00:02:00"],
#         ["00:02:00", "00:02:10"], ["00:02:10", "00:02:20"], ["00:02:20", "00:02:30"], ["00:02:30", "00:02:40"],
#         ["00:02:40", "00:02:50"], ["00:02:50", "00:03:00"], ["00:03:00", "00:03:10"], ["00:03:10", "00:03:20"],        
#         ["00:03:20", "00:03:30"], ["00:03:30", "00:03:40"], ["00:03:40", "00:03:50"], ["00:03:50", "00:04:00"],        
#         ["00:04:00", "00:04:05"]
#                 ]    
#                                 }

# import os


# def convert_to_sec(time_in_string):
#     t = time_in_string.split(":")    
#     h = int(t[0])
#     m = int(t[1])
#     s = int(t[2])
#     seconds = s + 60*m + 3600*h
#     return seconds

# inp.mp4 [], [], [], [], ["00:00:02", "00:00:06"]

# inp_0.mp4
# inp_1.mp4
# .
# .
# inp_4.mp4



# training_videos_time = 0
# for filename in lady_green_screen_trim_timings:
#     name = filename.split(".")[0]
#     from_and_to_path = "data_root/custom/lady_green_screen"    
#     orig_vid_path = os.path.join(from_and_to_path, filename)    
#     for idx, (from_time, to_time) in enumerate(lady_green_screen_trim_timings[filename]):
#         trimmed_vid_path = os.path.join(from_and_to_path, name + '_' + str(idx)+'.mp4')
#         command = f"ffmpeg -i '{orig_vid_path}' -ss {from_time} -to {to_time} '{trimmed_vid_path}'"            
#         subprocess.run(command, shell=True)
#         training_videos_time += (convert_to_sec(to_time) - convert_to_sec(from_time))
#     # delete the original mp4 and MTS files    
#     subprocess.run(f"rm -rf {orig_vid_path}", shell=True)
#     subprocess.run(f"rm -rf {orig_vid_path[:-4]+'.MTS'}", shell=True)

# sargam
# -s_01
# -s_15

# print(f"training_videos_time: {training_videos_time}")
# m, s = divmod(training_videos_time, 60)
# h, m = divmod(m, 60)
# print(f"that is: {h} hrs {m} mins {s} secs")

# # preprocess the data
# python3.7 preprocess.py --batch_size 4 --data_root data_root/custom --preprocessed_root custom_preprocessed/


# # delete directories with no jpg files in them
# import os
# from glob import glob

# base_preprocess_dir = "custom_preprocessed"
# dirs = os.listdir(base_preprocess_dir)
# k = []
# for d1 in dirs:
#     # print(f"in {d1}")
#     for d2 in os.listdir(os.path.join(base_preprocess_dir, d1)):
#         # print(f"d2: {d2}")        
#         jpg_files = glob(os.path.join(base_preprocess_dir, d1, d2, "*.jpg"))
#         # print(d1, d2, len(jpg_files))
#         print(f"{d1}/{d2}")
#         k.append(f"{d1}/{d2}")
#         if len(jpg_files) == 0:
#             print(f"DELETE DIRECTORY {base_preprocess_dir}/{d1}/{d2}")

# python3.7 wav2lip_train.py    --data_root custom_preprocessed/ --checkpoint_dir wav2lip_ckpts     --syncnet_checkpoint_path checkpoints/lipsync_expert.pth --checkpoint_path checkpoints/wav2lip.pth            
# python3.7 hq_wav2lip_train.py --data_root custom_preprocessed/ --checkpoint_dir wav2lip_gan_ckpts --syncnet_checkpoint_path checkpoints/lipsync_expert.pth --checkpoint_path checkpoints/wav2lip_gan.pth            


# # train data size = 64
# # bs = 16
# # 1 global epoch
# # 4 global step

# # ckpt interval: 500 global epoch (4*500 global step)
# # eval interval: 500 global epoch (4*500 global step)
# # eval_steps   : 40 global step (10 times of whole training data)

# # inference
# root@deeplearning-2-vm:/home/animesh0794/optimus# ls wav2lip_ckpts/
# 1 4 7
# 2 5 8
# 3 6 9
# # checkpoint_step000398000.pth  checkpoint_step000408000.pth  checkpoint_step000418000.pth  
# # checkpoint_step000400000.pth  "checkpoint_step000410000.pth"  checkpoint_step000420000.pth  
# # checkpoint_step000402000.pth  checkpoint_step000412000.pth  checkpoint_step000422000.pth  
# # "checkpoint_step000404000.pth"  checkpoint_step000414000.pth  checkpoint_step000424000.pth  
# checkpoint_step000406000.pth  checkpoint_step000416000.pth  "checkpoint_step000426000.pth"

# choose videos for video and audio
# 000_20_13.mp4 audio
# 000_20_12.mp4 vidio


# python3.7 inference.py --checkpoint_path checkpoints/wav2lip.pth                    --face "data_root/custom/lady_green_screen/00020_12.mp4" --audio "data_root/custom/lady_green_screen/00020_13.mp4" --outfile "results/v_00020_12_a_00020_13_00000.mp4"
# python3.7 inference.py --checkpoint_path wav2lip_ckpts/checkpoint_step000406000.pth --face "data_root/custom/lady_green_screen/00020_12.mp4" --audio "data_root/custom/lady_green_screen/00020_13.mp4" --outfile "results/v_00020_12_a_00020_13_06000.mp4"
# python3.7 inference.py --checkpoint_path wav2lip_ckpts/checkpoint_step000416000.pth --face "data_root/custom/lady_green_screen/00020_12.mp4" --audio "data_root/custom/lady_green_screen/00020_13.mp4" --outfile "results/v_00020_12_a_00020_13_16000.mp4"
# python3.7 inference.py --checkpoint_path wav2lip_ckpts/checkpoint_step000426000.pth --face "data_root/custom/lady_green_screen/00020_12.mp4" --audio "data_root/custom/lady_green_screen/00020_13.mp4" --outfile "results/v_00020_12_a_00020_13_26000.mp4"


# gsutil cp data_root/custom/lady_green_screen/00020_12.mp4 gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/lady_green_screen/
# gsutil cp data_root/custom/lady_green_screen/00020_13.mp4 gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/lady_green_screen/

# gsutil cp results/v_00020_12_a_00020_13_00000.mp4 gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/lady_green_screen/
# gsutil cp results/v_00020_12_a_00020_13_06000.mp4 gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/lady_green_screen/
# gsutil cp results/v_00020_12_a_00020_13_16000.mp4 gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/lady_green_screen/
# gsutil cp results/v_00020_12_a_00020_13_26000.mp4 gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/lady_green_screen/


# gsutil cp wav2lip_ckpts/checkpoint_step000406000.pth gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/lady_green_screen_models/
# gsutil cp wav2lip_ckpts/checkpoint_step000416000.pth gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/lady_green_screen_models/
# gsutil cp wav2lip_ckpts/checkpoint_step000426000.pth gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/lady_green_screen_models/

# https://storage.googleapis.com/justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/model_inputs/chatth_ka_tyohar.wav

# # wget "https://storage.googleapis.com/justbaat-dev.appspot.com/audio/lipsync_expert.pth"


# python3.7 inference.py --checkpoint_path wav2lip_ckpts/checkpoint_step000426000.pth --face "data_root/custom/lady_green_screen/00020_12.mp4" --audio "temp/chatth_ka_tyohar.wav" --outfile "results/v_00020_12_a_chatth_ka_tyohar_26000.mp4"
# gsutil cp results/v_00020_12_a_chatth_ka_tyohar_26000.mp4 gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/lady_green_screen/


# python3.7 inference.py --checkpoint_path wav2lip_ckpts/checkpoint_step000426000.pth --face "data_root/custom/lady_green_screen/00020_12.mp4" --audio "temp/chatth_ka_tyohar.wav" --outfile "results/v_00020_12_a_chatth_ka_tyohar_26000_pads_0_20_0_0.mp4" --pads 0 20 0 0
# gsutil cp results/v_00020_12_a_chatth_ka_tyohar_26000_pads_0_20_0_0.mp4 gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/lady_green_screen/

# python3.7 inference.py --checkpoint_path wav2lip_ckpts/checkpoint_step000426000.pth --face "data_root/custom/lady_green_screen/00020_12.mp4" --audio "temp/chatth_ka_tyohar.wav" --outfile "results/v_00020_12_a_chatth_ka_tyohar_26000_pads_0_40_0_0.mp4" --pads 0 40 0 0
# gsutil cp results/v_00020_12_a_chatth_ka_tyohar_26000_pads_0_40_0_0.mp4 gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/lady_green_screen/

# python3.7 inference.py --checkpoint_path wav2lip_ckpts/checkpoint_step000426000.pth --face "data_root/custom/lady_green_screen/00020_12.mp4" --audio "temp/chatth_ka_tyohar.wav" --outfile "results/v_00020_12_a_chatth_ka_tyohar_26000_resize_factor_2.mp4" --resize_factor 2
# gsutil cp results/v_00020_12_a_chatth_ka_tyohar_26000_resize_factor_2.mp4 gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/lady_green_screen/


# python3.7 inference.py --checkpoint_path wav2lip_ckpts/checkpoint_step000426000.pth --face "data_root/custom/lady_green_screen/00020_12.mp4" --audio "temp/chatth_ka_tyohar.wav" --outfile "results/v_00020_12_a_chatth_ka_tyohar_26000_nosmooth.mp4" --nosmooth
# gsutil cp results/v_00020_12_a_chatth_ka_tyohar_26000_nosmooth.mp4 gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/lady_green_screen/



# ############################# TRAINED wav2lip_gan ###########################
# checkpoint_step000264000.pth, disc_checkpoint_step000264000.pth  
# checkpoint_step000268000.pth, disc_checkpoint_step000268000.pth   

# python3.7 inference.py --checkpoint_path wav2lip_gan_ckpts/checkpoint_step000264000.pth
 
# --face "data_root/custom/lady_green_screen/00020_12.mp4" --audio "temp/chatth_ka_tyohar.wav" --outfile "results/v_00020_12_a_chatth_ka_tyohar_26000_nosmooth.mp4" --nosmooth




# python3.7 inference.py --checkpoint_path checkpoints/wav2lip_gan.pth                    --face "data_root/custom/lady_green_screen/00020_12.mp4" --audio "data_root/custom/lady_green_screen/00020_13.mp4" --outfile "results/gan/v_00020_12_a_00020_13_00000_gan.mp4"
# python3.7 inference.py --checkpoint_path wav2lip_gan_ckpts/checkpoint_step000264000.pth --face "data_root/custom/lady_green_screen/00020_12.mp4" --audio "data_root/custom/lady_green_screen/00020_13.mp4" --outfile "results/gan/v_00020_12_a_00020_13_64000_gan.mp4"
# python3.7 inference.py --checkpoint_path wav2lip_gan_ckpts/checkpoint_step000268000.pth --face "data_root/custom/lady_green_screen/00020_12.mp4" --audio "data_root/custom/lady_green_screen/00020_13.mp4" --outfile "results/gan/v_00020_12_a_00020_13_68000_gan.mp4"
# python3.7 inference.py --checkpoint_path wav2lip_gan_ckpts/checkpoint_step000264000.pth --face "data_root/custom/lady_green_screen/00020_12.mp4" --audio "temp/chatth_ka_tyohar.wav"                       --outfile "results/gan/v_00020_12_a_chatth_ka_tyohar_64000_gan.mp4"

# gsutil cp -r results/gan gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/lady_green_screen/



# # model uploaded to GCP cloud storage
# gsutil cp checkpoint_step000264000.pth gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/lady_green_screen_models/

# gsutil cp gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/model_inputs/karishma_green_screen_cropped.mp4 temp/

# python3.7 inference.py --checkpoint_path wav2lip_gan_ckpts/checkpoint_step000264000.pth --face "temp/karishma_green_screen_cropped.mp4" --audio "temp/chatth_ka_tyohar.wav" --outfile "results/gan/v_karishma_green_screen_cropped_a_chatth_ka_tyohar_64000_gan.mp4"
# gsutil cp results/gan/v_karishma_green_screen_cropped_a_chatth_ka_tyohar_64000_gan.mp4 gs://justbaat-dev.appspot.com/audio/wav2lip_custom_training_results/lady_green_screen/gan/


# gsutil cp gs://justbaat-dev.appspot.com/audio/Gagan/trim_videos.py .

########################################################################################################################
import subprocess, os, shutil
from glob import glob


# Step 1: Initialize base_dir and remove it if it exists
separator_string = "-------------------------"
root_dir = "data_root/custom/"
# data_dir = "karishma"
data_dir = "aajtak"
base_dir = os.path.join(root_dir, data_dir)
subprocess.run(f"rm -rf {base_dir}", shell=True)


# Step 2: Initialize a dict with all the names of the videos and their respective trim windows
# karishma_trim_window_dict = {
#     "00011.mp4": [["00:00:03", "00:00:13"], ["00:00:13", "00:00:23"], ["00:00:23", "00:00:33"], ["00:00:33", "00:00:43"], ["00:00:43", "00:00:53"], ["00:00:53", "00:01:03"], ["00:01:03", "00:01:13"], ["00:01:13", "00:01:23"], ["00:01:23", "00:01:33"], ["00:01:33", "00:01:43"], ["00:01:53", "00:02:03"], ["00:02:03", "00:02:13"], ["00:02:13", "00:02:23"], ["00:02:23", "00:02:33"], ["00:02:33", "00:02:43"], ["00:02:43", "00:02:53"], ["00:02:53", "00:03:03"]],
#     "00015.mp4": [["00:00:45", "00:00:55"], ["00:00:55", "00:01:05"], ["00:01:05", "00:01:15"], ["00:01:15", "00:01:25"], ["00:01:25", "00:01:35"], ["00:01:35", "00:01:45"], ["00:01:45", "00:01:55"], ["00:01:55", "00:02:05"], ["00:02:05", "00:02:15"], ["00:02:15", "00:02:25"], ["00:02:25", "00:02:35"]],
#     "00016.mp4": [["00:00:02", "00:00:06"]],
#     "00018.mp4": [["00:00:00", "00:00:10"], ["00:00:11", "00:00:21"], ["00:00:21", "00:00:31"], ["00:00:31", "00:00:41"], ["00:00:41", "00:00:51"], ["00:00:51", "00:01:01"], ["00:01:01", "00:01:11"], ["00:01:11", "00:01:21"], ["00:01:21", "00:01:31"]],
#     "00019.mp4": [["00:00:03", "00:00:13"], ["00:00:13", "00:00:23"], ["00:00:23", "00:00:33"], ["00:00:33", "00:00:43"], ["00:00:43", "00:00:53"], ["00:00:53", "00:01:03"], ["00:01:03", "00:01:13"]],
#     "00020.mp4": [["00:00:01", "00:00:11"], ["00:00:11", "00:00:22"], ["00:00:22", "00:00:32"], ["00:00:32", "00:00:42"], ["00:00:42", "00:00:52"], ["00:00:52", "00:01:02"], ["00:01:02", "00:01:12"], ["00:01:12", "00:01:22"], ["00:01:22", "00:01:32"], ["00:01:32", "00:01:42"], ["00:01:42", "00:01:52"], ["00:01:52", "00:02:02"], ["00:02:02", "00:02:12"], ["00:02:12", "00:02:22"], ["00:02:22", "00:02:32"], ["00:02:32", "00:02:42"], ["00:02:42", "00:02:52"], ["00:02:52", "00:03:02"], ["00:03:02", "00:03:12"], ["00:03:12", "00:03:22"], ["00:03:22", "00:03:32"], ["00:03:32", "00:03:42"], ["00:03:42", "00:03:52"]]
#                             }

aajtak_trim_window_dict = {
    "sargam_01.mp4": [["00:00:00", "00:00:10"], ["00:00:10", "00:00:20"], ["00:00:20", "00:00:30"], ["00:00:30", "00:00:40"], ["00:00:40", "00:00:50"], ["00:00:50", "00:01:00"], ["00:01:00", "00:01:10"], ["00:01:10", "00:01:20"], ["00:01:20", "00:01:30"], ["00:01:30", "00:01:40"], ["00:01:40", "00:01:50"], ["00:01:50", "00:02:00"], ["00:02:00", "00:02:10"], ["00:02:10", "00:02:20"], ["00:02:20", "00:02:30"], ["00:02:30", "00:02:40"], ["00:02:40", "00:02:50"]],
    "sargam_02.mp4": [["00:00:00", "00:00:10"], ["00:00:10", "00:00:20"], ["00:00:20", "00:00:30"], ["00:00:30", "00:00:40"], ["00:00:40", "00:00:50"], ["00:00:50", "00:01:00"], ["00:01:00", "00:01:10"], ["00:01:10", "00:01:20"], ["00:01:20", "00:01:30"], ["00:01:30", "00:01:40"], ["00:01:40", "00:01:50"], ["00:01:50", "00:02:00"], ["00:02:00", "00:02:10"], ["00:02:10", "00:02:20"], ["00:02:20", "00:02:30"], ["00:02:30", "00:02:40"], ["00:02:40", "00:02:50"]],
    "sargam_03.mp4": [["00:00:00", "00:00:10"], ["00:00:10", "00:00:20"], ["00:00:20", "00:00:30"], ["00:00:30", "00:00:40"], ["00:00:40", "00:00:50"], ["00:00:50", "00:01:00"], ["00:01:00", "00:01:10"], ["00:01:10", "00:01:20"], ["00:01:20", "00:01:30"], ["00:01:30", "00:01:40"], ["00:01:40", "00:01:50"], ["00:01:50", "00:02:00"], ["00:02:00", "00:02:10"], ["00:02:10", "00:02:20"], ["00:02:20", "00:02:30"], ["00:02:30", "00:02:40"], ["00:02:40", "00:02:50"]],
    "sargam_04.mp4": [["00:00:00", "00:00:10"], ["00:00:10", "00:00:20"], ["00:00:20", "00:00:30"], ["00:00:30", "00:00:40"], ["00:00:40", "00:00:50"], ["00:00:50", "00:01:00"], ["00:01:00", "00:01:10"], ["00:01:10", "00:01:20"], ["00:01:20", "00:01:30"], ["00:01:40", "00:01:50"], ["00:01:50", "00:02:00"], ["00:02:10", "00:02:20"], ["00:02:20", "00:02:30"], ["00:02:40", "00:02:50"]],
    "sargam_05.mp4": [["00:00:00", "00:00:10"], ["00:00:10", "00:00:20"], ["00:00:20", "00:00:30"], ["00:00:30", "00:00:40"], ["00:00:40", "00:00:50"], ["00:00:50", "00:01:00"], ["00:01:00", "00:01:10"], ["00:01:10", "00:01:20"], ["00:01:20", "00:01:30"], ["00:01:30", "00:01:40"], ["00:01:40", "00:01:50"], ["00:01:50", "00:02:00"]]
                        }


# Step 3: Initialize the path of the videos in Step 2 on cloud
# karishma_videos_cloud_path = "gs://justbaat-dev.appspot.com/audio/wav2lip_fine_tuning/v1/unprocessed_green_screen_videos/"
aajtak_videos_cloud_path = "gs://justbaat-dev.appspot.com/audio/wav2lip_fine_tuning/v2/unprocessed_green_screen_videos/"
                         

# Step 4: Download all the videos
# for filename, windows in karishma_trim_window_dict.items():
for filename, windows in aajtak_trim_window_dict.items():    
    # file_path_on_cloud = os.path.join(karishma_videos_cloud_path, filename)
    file_path_on_cloud = os.path.join(aajtak_videos_cloud_path, filename)
    file_path_on_local = os.path.join(base_dir, filename)
    download_video_command = f"gsutil cp {file_path_on_cloud} {file_path_on_local}"
    download_message = f"downloading {file_path_on_cloud} to {file_path_on_local}"
    print(f"{separator_string}\n{download_message}")
    try:
        subprocess.run(download_video_command, shell=True)
        print("SUCCESS")
    except:
        print("FAILURE")


# Step 5: Trim the videos
def convert_to_sec(time_in_string):
    t = time_in_string.split(":")    
    h = int(t[0])
    m = int(t[1])
    s = int(t[2])
    seconds = s + 60*m + 3600*h
    return seconds

training_videos_time = 0
# for filename, trim_windows in karishma_trim_window_dict.items():
for filename, trim_windows in aajtak_trim_window_dict.items():
    name = filename.split(".")[0] # 00015
    orig_vid_path = os.path.join(base_dir, filename)    
    for idx, (from_time, to_time) in enumerate(trim_windows):
        trimmed_vid_path = os.path.join(base_dir, name + '_' + str(idx)+'.mp4')
        trim_command = f"ffmpeg -i '{orig_vid_path}' -ss {from_time} -to {to_time} '{trimmed_vid_path}' -loglevel error"            
        trim_message = f"trimming {orig_vid_path} from {from_time} to {to_time} and creating {trimmed_vid_path}"
        print(f"{separator_string}\n{trim_message}")
        try:
            subprocess.run(trim_command, shell=True)
            training_videos_time += (convert_to_sec(to_time) - convert_to_sec(from_time))
            print("SUCCESS")
        except:
            print("FAILURE")
    # Delete the original mp4 and MTS files    
    delete_message = f"deleting {orig_vid_path}"
    print(f"{separator_string}\n{delete_message}")
    try:
        subprocess.run(f"rm -rf {orig_vid_path}", shell=True)
        # subprocess.run(f"rm -rf {orig_vid_path[:-4]+'.MTS'}", shell=True)
        print("SUCCESS")
    except:
        print("FAILURE")

print(f"{separator_string}\ntraining_videos_time: {training_videos_time}")
m, s = divmod(training_videos_time, 60)
h, m = divmod(m, 60)
print(f"that is: {h} hrs {m} mins {s} secs")


# Step 6: View the trimmed videos in base_dir
subprocess.run(f"tree {base_dir}", shell=True)


# Step 7: Upload the directory with trimmed videos to GCP storage
# karishma_trimmed_vids_cloud_path = "gs://justbaat-dev.appspot.com/audio/wav2lip_fine_tuning/v1/trimmed_green_screen_videos/"
aajtak_trimmed_vids_cloud_path = "gs://justbaat-dev.appspot.com/audio/wav2lip_fine_tuning/v2/trimmed_green_screen_videos/"
upload_trimmed_videos_dir_command = f"gsutil -m cp -r {base_dir} {aajtak_trimmed_vids_cloud_path}"
upload_trimmed_videos_dir_message = f"uploading {base_dir} to {aajtak_trimmed_vids_cloud_path}"
print(f"{separator_string}\n{upload_trimmed_videos_dir_message}")
try:
    subprocess.run(upload_trimmed_videos_dir_command, shell=True)
    print("SUCCESS")
except:
    print("FAILURE")


# Step 8: Run wav2lip preprocess step    
custom_training_data_preprocessed_dir = "custom_training_data_preprocessed"
wav2lip_preprocess_command = f"python3.7 preprocess.py --batch_size 4 --data_root {root_dir} --preprocessed_root {custom_training_data_preprocessed_dir}"
wav2lip_preprocess_message = f"running wav2lip preprocessing step"
print(f"{separator_string}\n{wav2lip_preprocess_message}")
try:
    subprocess.run(wav2lip_preprocess_command, shell=True)
    print("SUCCESS")
except:
    print("FAILURE")


# Step 9: Delete directories in custom_trainin_data_preprocessed_dir with no jpg files in them
custom_training_data_dirs = glob(custom_training_data_preprocessed_dir + "/*")
for custom_training_data_dir in custom_training_data_dirs:
    # print(custom_training_data_dir) # custom_trainin_data_preprocessed/karishma
    for vid_dir in glob(custom_training_data_dir + "/*"):
        # print(vid_dir) # custom_trainin_data_preprocessed/karishma/00020_10
        jpg_files = glob(os.path.join(vid_dir, "*.jpg"))    
        if len(jpg_files) == 0:
            print(f"Delete directory {vid_dir}")
            shutil.rmtree(vid_dir)


# Step 10: Upload items in custom_training_data_preprocessed_dir to GCP storage
# wav2lip_preprocessed_data_cloud_path = "gs://justbaat-dev.appspot.com/audio/wav2lip_fine_tuning/v1/wav2lip_preprocessed_data/"
wav2lip_preprocessed_data_cloud_path = "gs://justbaat-dev.appspot.com/audio/wav2lip_fine_tuning/v2/wav2lip_preprocessed_data/"
wav2lip_preprocessed_data_path = os.path.join(custom_training_data_preprocessed_dir, data_dir)
# -m is for multi-processing
upload_wav2lip_preprocessed_data_command = f"gsutil -m cp -r {wav2lip_preprocessed_data_path + '/'} {wav2lip_preprocessed_data_cloud_path}"
upload_wav2lip_preprocessed_data_message = f"uploading items in {wav2lip_preprocessed_data_path} to {wav2lip_preprocessed_data_cloud_path}"
print(f"{separator_string}\n{upload_wav2lip_preprocessed_data_message}")
try:
    subprocess.run(upload_wav2lip_preprocessed_data_command, shell=True)
    print("SUCCESS")
except:
    print("FAILURE")


# Step 11: Fine-tune wav2lip_gan
wav2lip_gan_ckpt_dir = "wav2lip_gan_ckpt"
wav2lip_gan_fine_tune_command = "python3.7 hq_wav2lip_train.py --data_root {custom_training_data_preprocessed_dir} --checkpoint_dir {wav2lip_gan_ckpt_dir} --syncnet_checkpoint_path checkpoints/lipsync_expert.pth --checkpoint_path checkpoints/wav2lip_gan.pth"
subprocess.run(wav2lip_gan_fine_tune_command, shell=True)


# python3.7 hq_wav2lip_train.py --data_root custom_training_data_preprocessed --checkpoint_dir wav2lip_gan_ckpt --syncnet_checkpoint_path checkpoints/lipsync_expert.pth --checkpoint_path checkpoints/wav2lip_gan.pth

# Starting Epoch: 91
# 0it [00:00, ?it/s]>>> 91 258010 500 10
# L1: 0.06015663057565689, Sync: 0.0, Percep: 0.6935766935348511 | Fake: 0.6927179098129272, Real: 0.6935502886772156: : 1it [00:19, 19.23s/it]>>> 91 258011 500 11

# Upload the fine-tuned models to GCP storage
# checkpoint_step000261000.pth  checkpoint_step000264000.pth  checkpoint_step000267000.pth
# karishma_gan_step000261000.pth  karishma_gan_step000264000.pth  karishma_gan_step000267000.pth
# gsutil -m cp -r wav2lip_gan_ckpt/* gs://justbaat-dev.appspot.com/audio/wav2lip_fine_tuning/v1/fine_tuned_models/
