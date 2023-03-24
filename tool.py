# -*- coding: utf-8 -*-
import os
import glob

def run(context):
    """
    Function invoked by the SDK that passes a context object. This object can then be used
    to communicate with the platform in the context of that particular analysis to fetch files,
    report progress, and upload results, among others.

    Parameters
    ----------
    context : qmenta.sdk.context.AnalysisContext
        Analysis context object to communicate with the QMENTA Platform.
    """

    """ Basic setup """

    # Define directories for the input and output files inside the container
    input_dir = os.path.join(os.path.expanduser("~"), "INPUT")
    output_dir = os.path.join(os.path.expanduser("~"), "OUTPUT")
    os.makedirs(output_dir, exist_ok=True)
    context.set_progress(value=0, message="Processing")  # Set progress status so it is displayed in the platform

    """ Get the input data """

    # Retrieve input files
    dcm_handler = context.get_files("input_dcm", file_filter_condition_name="filter_dcm")[0]  # Only gets one file that passed the filter

    dcm = dcm_handler.download(input_dir)  # DICOM uncompressed folder
    modality = context.get_files("input_dcm", file_filter_condition_name="filter_dcm")[0].get_file_modality()

    # Retrieve settings
    settings = context.get_settings()

    """ Processing code """

    context.set_progress(value=10, message="Choosing output format")

    os.system(f"dcm2niix {dcm}")

    """ Upload results """

    nii_output = glob.glob(dcm + "/*.nii")[0]
    json_output = glob.glob(dcm + "/*.json")[0]

    context.upload_file(nii_output, os.path.basename(nii_output), modality=modality)
    context.upload_file(json_output, os.path.basename(json_output))
