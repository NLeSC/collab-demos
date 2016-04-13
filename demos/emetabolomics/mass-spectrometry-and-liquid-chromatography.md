_How liquid chromatography and mass spectrometry can help understand molecular structure_

Liquid chromatography and mass spectrometry techniques are useful in identifying what molecules are present in a given sample. Let's focus on the mass spectrometry first.

Mass spectrometers aim to measure the mass of individual molecules. Because measuring the mass of something so small is diffucult, mass spectrometers employ a neat trick: instead of measuring the mass directly, they first give the molecule an electric charge (so-called _ionization_) and subsequently send it through a magnetic field. Because the molecule is charged, it will experience a force that changes its trajectory. Assuming equal charge (e.g. electron unit), the resulting trajectory depends on the mass of the molecule. There are different designs of MS instruments. In the setup shown below a lighter molecule's trajectory will be more curved than a heavier molecule's trajectory. When the molecule hits the _detector_ at the end of its trajectory, a lighter molecule will hit near the bottom of the detector, whereas a heavier molecule will hit nearer the top. This way, you can now use position along the detector surface as a measure of the molecular mass.

![mass-spectrometer.png](mass-spectrometer.png)

So for example, if we introduce methane (CH4) into the apparatus, the mass spectrum will show a peak at a mass of about 16.03 (because the carbon atomic mass is 12.0 and the hydrogen mass is 1.008):

![mass-spectrum-ch4.png](mass-spectrum-ch4.png)

Note that the horizontal axis is labeled _M/z_, the mass-over-charge ratio. This is because it's not guaranteed that the molecule has unit charge (it depends on the experimental setup). The vertical axis is an indication (but not absolute measure) of how abundant a given mass is. 

It's likely that the mass spectrum will have multiple peaks. One of the reasons is that the molecule may fall apart into so-called _fragments_. For example, a methane molecule can fragment into one CH2 molecule and one H2 molecule. If this happens, the mass spectrum will show two additional peaks:

![mass-spectrum-ch4-ch2-h2.png](mass-spectrum-ch4-ch2-h2.png)

If other fragments are formed then there will be additional peaks in the mass spectrum. Also, the atoms may occur as different isotopes, which have slightly different mass. Therefore each molecule (or fragment) usually occurs as multiple peaks in the mass spectrum.

The full mass spectrum of carbon dioxide looks like this:

![mass-spectrum-co2.png](mass-spectrum-co2.png)

So when the initial sample consists of just one type of molecule, most of the time you can figure out what fragment each peak represents, but when we're dealing with things like urine or blood samples, there are simply too many peaks to make any sense of the mass spectrum. So in order to use mass spectrometry in combination with a complex mixture of molecules, we need a way to separate the complex mixture into groups of molecules, i.e. we need _chromatography_. 

_Separating a complex mixture by chromatography_

Chromatography can be _liquid chromatography_ (_LC_) or _gas chromatography_ (_GC_), but the principle is much the same: the complex mixture is diluted by a _solvent_, and then the resulting mixture is introduced into a so-called _column_. The column is basically a small tube filled with _packing material_. The purpose of the packing material is to slow down certain molecules more than others, depending on the molecule's structure, size, and charge. This way, each type of molecule will be associated with a characteristic travel time through the column (the so-called _retention time_): 

![chromatography-idealized.png](chromatography-idealized.png)

By placing the LC before the MS, individual, or at least much smaller numbers of, molecules are simultaneously introduced into the mass spectrometer, which greatly simplifies the MS analysis later on.

