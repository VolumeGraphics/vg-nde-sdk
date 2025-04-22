=========================================
Beam hardening correction preset handling
=========================================

General
~~~~~~~

The beam hardening correction handling here relates directly to the functionality of the slice preview
of the reconstruction import wizard in the application.

It is possible to use an exported preset in the application referenced by the name of the preset.
For this the beam hardening correction has to be activated with \a setBeamHardeningCorrectionMode(Preset).
The name of the exported preset has to be set with \a setBeamHardeningCorrectionPreset("PresetName").

The application of the preset values is done directly after all other parameters of the reconstruction
project were loaded. The preset holds a subset of the reconstruction parameters.

Lookup table for correction of radiation intensities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The next thing to consider is the so called preset mode. It controls how the lookup table range is
applied to the radiation intensities in the application when the preset is applied.

There is a static and dynamic mode available for application of the lookup table range. Use the static mode
if no compensation for variation of radiation intensities is used at all. If the compensation is active,
the dynamic mode may be a good choice. This applies the lookup table range according to the determined value range
of each of the intensity images.

Enum         | Mode of application
-------------|---------------------
\a Automatic | use mode of application specified in the preset (either \a Static or \a Dynamic, see next enums)
\a Static    | preset application does not change the lookup table range
\a Dynamic   | preset application changes the lookup table range according to the radiation intensity ranges
\a Explicit  | set the value range via \a setBeamHardeningCorrectionPresetValueRange()

If the predefined presets "Low", "Medium" or "High" are used the mode of application is always \a Dynamic.

