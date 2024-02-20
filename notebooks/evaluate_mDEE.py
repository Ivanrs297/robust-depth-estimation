# pip install imagecorruptions

import subprocess

script_path = "AF-SfMLearner/evaluate_depth.py"
script_monovit_path = "endo-manydepth/manydepth/evaluate_hr_depth.py"
script_endosfmlearner_path = "EndoSLAM/EndoSfMLearner/eval_depth.py"

corruptions = [
    "gaussian_noise",
    "shot_noise",
    "impulse_noise",
    "defocus_blur",
    "glass_blur",
    "motion_blur",
    "zoom_blur",
    "snow",
    "frost",
    "fog",
    "brightness",
    "contrast",
    "elastic_transform",
    "pixelate",
    "jpeg_compression",
]



for corr in corruptions:
    for sev in range(1, 6):

        # afsfmlearnar
        # command = rf"python {script_path} --corruption {corr} --severity {sev} --data_path ..\data\raw\SCARED\ --load_weights_folder ..\models\Model_MIA\Model_MIA\ --eval_mono"

        # monodepth
        # command = rf"python {script_path} --corruption {corr} --severity {sev} --data_path ..\data\raw\SCARED\ --load_weights_folder ..\models\weights_19\weights_19\ --eval_mono"

        # monovit TODO: modificy evaluate script
        command = rf"python {script_monovit_path} --corruption {corr} --severity {sev} --data_path ..\data\raw\SCARED\ --load_weights_folder ..\models\weights_19_MonoViT\weights_19\ --eval_mono"

        # endoSLAM
        # command = rf"python {script_endosfmlearner_path} --corruption {corr} --severity {sev} --data_path ..\data\raw\SCARED\ --load_weights_folder ..\models\weights_19_MonoViT\weights_19\ --eval_mono"

        print("CMD", command)
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        print("Output:", result.stdout)
        print("Errors:", result.stderr)
        print("-" * 40)
