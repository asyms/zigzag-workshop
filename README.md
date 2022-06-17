# zigzag-v2
ZigZag written with OOP and new data format.

## Environment

We recommend setting up an anaconda environment.

A `conda-spec-file-{platform}.txt` is provided to set up the environment for linux64 and win64.

`$ conda create --name myzigzagenv --file conda-spec-file-{platform}.txt`

Alternatively, you can also install all packages directly through pip using the pip-requirements.txt with the command:

`$ pip install -r requirements.txt`

## Example

The inputs folder provides some example accelerator/workload/settings.

For example, the xception snippet running on a single core accelerator using loma:

`$ python main.py --workload inputs.examples.workloads.xception_block --accelerator inputs.examples.hardware.single_core`
