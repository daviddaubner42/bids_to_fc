import nibabel as nib
import pandas as pd
import argparse

"""
Script that takes a Cifti dlabel.nii file and creates a .tsv info file that satisfies the XCP-D atlas requirements.
Params:
    -atlas-file :  Path to the atlas
    -output     :  Path to the output atlas info .tsv file
"""

parser = argparse.ArgumentParser(description="Create remap from label file.")
parser.add_argument("-atlas_file", type=str, help="Path to the atlas")
parser.add_argument("-output", type=str, help="Path to the output atlas info .tsv file")
args = parser.parse_args()

atlas = nib.load(args.atlas_file)
axes = [atlas.header.get_axis(i) for i in range(atlas.ndim)]

label_dict = axes[0].label[0]

label_df = pd.DataFrame({"index": [], "label": []})

for i, t in label_dict.items():
    if i > 0:
        label_df.loc[i] = [i, t[0]]

label_df.to_csv(args.output, sep='\t', index=False)