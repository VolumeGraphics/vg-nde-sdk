# Introduction
The VG NDE SDK contains python interfaces to write the .xvgi file format, to enable the easy import of supported
data into VG software. It is also possible to add pre-defined or custom meta information for the imported objects,
for use in reporting or data exports, e.g. when connecting to Q-DAS products.

![Image](docs/images/data_types.png)

> Oftentimes .vgl projects can already be created by the software of the acquisition system. In these cases there
> is no benefit to using the VG NDE SDK. 


# Using .xvgi files
VG software products starting from 2025.1 version are able to load these files, and support their use in
 * Open
 * Merge object(s)
 * Batch processing

Once loaded, the resulting project can be saved as a normal .vgl file, and the .xvgi file is no longer necessary.
It is only used for the initial import of the data, and can be discarded. It is strongly recommended to use the name
of the .xvgi file when saving, as is proposed by the software. This helps maintaining the association with referenced
data.


# Referencing data

.xvgi files reference the data that is to be imported via absolute file paths. These file paths must be accessible to
the application loading the file, making the created files dependent on the original location of the data. If the
referenced data is intended to be moved or copied together with the .xvgi file (and the .vgl file eventually created 
from it), **the [vg-data] folder must be used.**

# [vg-data] folder

Data that is referenced by the file **test.xvgi** can be stored in the matching "[vg-data] test" folder. Any file paths
that point into a [vg-data] folder using the same name as the .xvgi file will be automatically adjusted to point into
the [vg-data] folder next to the file when it is loaded. Organizing and referencing data this way ensures that .xvgi 
files and their associated [vg-data] folder can be moved and copied around easily.

![Image](docs/images/folder_and_file.png)

# Getting Started
Requires Python 3.9 or newer. The `examples` folder contains example of how to create files referencing volume or mesh
data, or projections for reconstruction.

# Build and Test

 ```shell
  uv sync
  uv run poe test
 ```
