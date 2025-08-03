# BIDS to FC pipeline

Defines a Snakemake processing pipeline that creates a functional connectivity matrix using a Desikan-Killiany cortical + Fischl subcortical parcellation (based on the FreeSurfer aparc+aseg parcellation).

The input directory must be in the BIDS format and contain the following files:
- `$DATADIR/sub-$SUBID/anat/sub-$SUBID_T1w.nii.gz`
- `$DATADIR/sub-$SUBID/fmap/sub-$SUBID_magnitude1.nii.gz`
- `$DATADIR/sub-$SUBID/fmap/sub-$SUBID_magnitude2.nii.gz`
- `$DATADIR/sub-$SUBID/fmap/sub-$SUBID_phasediff.nii.gz`
- `$DATADIR/sub-$SUBID/func/sub-$SUBID_task-rest_bold.nii.gz`
where $DATADIR is the `datadir` specified in the `config/config.yaml`.

Additionally T2 can be used to make fMRIPrep results more precise, but is not necessary if it is not available. If you do not wish to use T2, please comment it out in the input requirements of the fmriprep rule.
- `$DATADIR/sub-$SUBID/anat/sub-$SUBID_T2w.nii.gz`

The directories specified in `config/config.yaml` need to be changed to match the system the pipeline is running on.

If you want to use different XCP-D preprocessing parameters than the default ones, you can change the command line arguments to the XCP-D shell command in the xcp_d rule.

To run the pipeline, launch a terminal in the `rootdir` specified in the `config/config.yaml`, and run `snakemake --cores all --sdm apptainer conda --singularity-args="--cleanenv -B $DATADIR:$DATADIR -B $ROOTDIR:$ROOTDIR"` (or whatever the desired number of cores is).
The singularity arguments clear environmental variables and bind the data and pipeline directories into the container, to avoid naming conflicts inside the containers.