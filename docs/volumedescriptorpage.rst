=========================================
Describing volume data
=========================================

General
~~~~~~~
In order to reference existing volume data from a VG project, you have
to create an instance of the class Project with the project type \a Volume.
You can then reference one or more volumes using the VolumeDescriptor class. When the project
is loaded into a VG application, the volume data will imported according to the chosen
settings and volumes will be placed into the scene.

General concepts of project creation can be found \ref PageVolumeGraphicsProject "here".

* VolumeDescriptor class for detail parameter description.
* examples/volumes and examples/manual_setup for basic examples


Object file settings
~~~~~~~~~~~~~~~~~~~~

In order to describe a volume grid, you have to create one or more instances
of the VolumeDescriptor::File class. These instances are passed to the
descriptor with addFile() method.

Each VolumeDescriptor::File defines one or more xy slices, which are stacked in the order of
their addition. They include some information, e.g., the file format, the file
name, the endianess and the data type.  Additionally, you have to set the
voxel dimensions for each VolumeDescriptor::File. For \a RAW and \a GZIP files
you can also set the header skip, thereby defining how many header bytes will
be skipped when reading the file.


.. warning::
   Please note that settings like Region Of Interest, Voxel Skip
   or Axis Mirror are not included in every single file definition, but on
   the volume level

Usually the grid resolution for the whole volume is set using \a
Resolution. In order to define a volume with non-equidistant slices, you can
define the physical position of each slice within the volume using the
optional method \a setPositionList(). If valid values are given for all slices
within the volume the defined position instead of the z resolution will be
used.

Volume settings
~~~~~~~~~~~~~~~

The grid structure defined by the VolumeDescriptor::File list can be changed
using the VolumeDescriptor options. If those options are not set, the volume
will be identified using the information of the VolumeDescriptor::File
instances.
You can also change the position and orientation of the volumes in the scene
coordinate system. By default, each volume is positioned in 
the origin of this coordinate system, with the axes of the volume coordinate
system aligned with the scene coordinate systems' axes.

.. note::
   If multiple volumes are added to a project, you might want to use different
   positions for each one. Otherwise their visualizations will intersect initially.