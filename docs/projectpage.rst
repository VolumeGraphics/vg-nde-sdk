=========================================
VG project concepts
=========================================

General
~~~~~~~
  
A VG project consists of two mandatory components, the \a project \a file and the \a project \a folder.

The project file has the file extension \c{.vgl} and contains basic information about the project and also
references to volume data, projection files or mesh files. In addition supplementary internal files are automatically
created when saving a project via the SDK or other VG applications. These supplementary files are stored in the project folder
next to the vgl file. The project folder is named after the project file, prefixed with \c{[vg-project]}.

A VG project file must always be accompanied by its project folder and the
file(s) containing the referenced data. You cannot open an SDK created project file without the
associated project folder, or without the volume data, projection files or meshes referenced by it.
Volume data, projection files and mesh files must be addressed via an absolute path in either Unix or Windows notation.

.. important::
   SDK created files need to be opened and saved with a licensed VG application at least once before they can be loaded into myVGL.

Volume data files
~~~~~~~~~~~~~~~~~

These files contain the voxel data of the volume objects in the scene. The number and type of files per volume can vary. You might have
one file containing the whole object (volume file formats) or an image stack (e.g., bitmaps or
tiffs) where each file represents one slice of the scanned object. Look at the VolumeDescriptor class for supported data types and file formats.


Projection files
~~~~~~~~~~~~~~~~

Projection data files are generated from CT scanning systems and have to be reconstructed into volume data. Look at the ReconstructionDescriptor
class for supported data types, file formats and reconstruction modes.


Mesh files
~~~~~~~~~~

Mesh data files represent a parts surface, and can be created by various means. Look at the MeshDescriptor
class for supported data types and file formats.


Creating portable projects
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to use the SDK to create VG projects that can be easily moved to different systems, it is strongly advided to
store referenced data in the data folder of the project. The data folder uses the same naming pattern as the project folder, but with the prefix \c{[vg-data]}.

.. hint::
   Storing referenced files in the [vg-data] folder is especially beneficial when creating projects for use with a VGinLINE system - it greatly simplifies automated export, cleanup
   and related mechanisms used there.


A portable project should then look like this:

\code
myresult.vgl          // VG project file
[vg-project] myresult // required project folder containing internal, proprietary data files
|_
  |
   696E666F746970.vgp
   70726576696477.vgp
   nominalactual-5FF03AD9.vgd
   6d6573685F82D1E5.vgs
   76670764455363.vge
[vg-data] myresult // optional data folder containing referenced files
|_
  |
   scanned_obj.raw // data file referenced by the vgl file via its absolute path
\endcode
\n

Any files contained in the data folder and referenced via absolute path in the .vgl file will be automatically found even if the project and its folders are moved on the disk
or across PCs.

You can also create (semi-)portable projects by referencing any data files via a path that is accessible from all the PCs you are using the project on (e.g. a shared network location).

Meta information
~~~~~~~~~~~~~~~~~~~~~~~~~~

The SDK offers you the possibility to include additional meta information in a
VG project, which will then be used in VG applications (e.g. when creating reports) or the VGExplorer
Integration.  

.. important::
   Only volume and reconstruction projects currently support meta information.

Additional meta information is split into the following categories:
\li manufacturer information
\li scan information
\li component information
\li logo and preview

The meta information can be inspected via the object properties dialog in most VG applications.

\n
The classes ManufacturerInfo, ScanInfo and ComponentInfo and the properties
logo and preview of the Project class represent those categories. Both a \a
Volume and a \a Reconstruction project can include all four categories.

All meta information strings are optional, but if you set them they must be \wikipedia{UTF-8, UTF-8}
encoded.

\subsection SubSectionCustomInformation User defined meta information

All info classes include some sensible pre-defined information tags as well as optional user defined
tags. You can use the methods of MetaInfo class to add user defined
tag/description pairs. You can add no more than \a ten tags per category.

\code
manufacturerInfo.add ("address", "Speyerer Strasse 4-6 69115 Heidelberg");
manufacturerInfo.add ("url", http://www.volumegraphics.com");

// tag     |  description
// -------------------
// address |  Speyerer Strasse 4-6 69115 Heidelberg
// url     |  http://www.volumegraphics.com
\endcode

.. hint::
   Your custom tags should be short and concise. Avoid blanks or special characters in your tags.


