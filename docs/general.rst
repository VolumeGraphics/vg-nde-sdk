VG NDE SDK: Simplified Data Import for VG software
==================================================

VG NDE SDK is a simple Python interface with the purpose of streamlining the process of importing various
types of data into VG software products like VGSTUDIO MAX or VGinLINE. It serves as a reference implementation for the
.xvgi format, which is used to create parameter files that facilitate the import of meshes, volume data, and projection data, 
removing the need to manually import data through the user interface, and enabling automatic workflows.

Key Features
------------

- **Easy Parameter File Creation**: Generate .xvgi parameter files with minimal effort, allowing for quick and efficient data import.
- **Support for Multiple Data Types**: Import meshes, volume data, and projection data for reconstruction
- **Meta Information Support**: Include scanning parameters and traceability information (e.g., serial numbers) about the parts that the data represents.
- **Compatibility with VG software products**: Ensure smooth data integration with e.g. VGSTUDIO MAX or VGinLINE.
- **Comprehensive Documentation**: Includes documentation and examples to help you get started quickly

Important details
-----------------
- Files created with the SDK are compatible with all VG software versions that are as recent as or newer than the interface used.
- The free viewer myVGL cannot immediately use the created .xvgi files; they must first be saved with a licensed software version.
- The created .xvgi files reference the data to be imported via file paths, and these paths must be accessible by the VG software opening the .xvgi file.
- Once opened, .xvgi files will turn into .vgl projects and be saved as such.