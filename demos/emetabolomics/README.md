# In short

- **url**: [http://www.emetabolomics.org/results_tea_urine.html](http://www.emetabolomics.org/results_tea_urine.html)
    - IP-whitelisting: No
    - Requires login: No
    - Works better with GPU: N/A
    - Database: (speed) TODO
    - Network: Transferring data is not a bottleneck for this demo
- **screencast**: Not available
- **contact person**: [Lars Ridder](https://www.esciencecenter.nl/profile/dr.-lars-ridder), [Stefan Verhoeven](https://www.esciencecenter.nl/profile/ing.-stefan-verhoeven)
- **screenshot**:
![screenshot](/demos/emetabolomics/screencapture-demo-emetabolomics.png "emetabolomics demo screenshot")

# General idea of the project

In chemistry, when you have a complex mixture of unknown composition, you can put a sample of it through an LC/MS (liquid chromatography/mass spectrometry). The LC part of the LC/MS separates the mixture into its constituent compounds/molecules, while the MS part subsequently measures the mass of each compound. 

# Demo usage

You're probably going to need to explain a little bit about LC/MS'es. Read up on it [here](mass-spectrometry-and-liquid-chromatography.md).

TODO

## Known quirks

TODO

- IP-whitelisting:
- Requires login:
- Works better with GPU: (speed, memory)
- Database: (speed)
- Network: (speed, interference of other devices when on wireless)

**Known quirks** are collected [here](https://github.com/NLeSC/collab-demos/issues/64). See also the [general remarks](/doc/demo-usage-general-remarks.md) about web demos.

# Technologically interesting aspects

- The link between back-end algorithm and front-end interface is completely based on an sqlite database file containing all the results
- Both the computational algorithm and the webinterface are able to deal with nested multilevel mass spectrometry data. Hierarchical trees of fragments are linked to trees of substructures of candidate molecules.
- Both the computational algorithm and the webinterface deal with many to many relationships: candidates may match to multiple precursor ions and precursor ion may match to multiple candidates
- The user friendly and interactive interface allows to browse through this complex data with many relationships 

# Scientifically interesting aspects

- MAGMa combines metabolite prediction with automatic screening in/annotation of LC-MSn metabolomics datasets
- It allows mass spectrometry experts to interpret unknown molecules which helps to gain more biological insight from complex samples than otherwise would be possible
- MAGMa performed very well in the Critical Assessment of Small Molecule Identification (CASMI) contest. It was announced best automatic method in CASMI 2013 and winner of category 1 in CASMI 2014

# Further reading

- Project [website](https://www.esciencecenter.nl/project/chemical-informatics-for-metabolite-identification-and-biochemical-network) on esciencecenter.nl
- Project [video](https://vimeo.com/109444671) on vimeo.com
- A screencast [video] of the demo on vimeo.com
- Browse [the code](https://github.com/NLeSC/MAGMa) on github.com
- Pitch presentations on [sharepoint](https://nlesc.sharepoint.com/Shared%20Documents/Forms/AllItems.aspx?RootFolder=%2FShared%20Documents%2FNLeSC%20Project%20Presentations%2FCurrent%2FeMetabolomics&FolderCTID=0x0120004EB0DBA245A10041AA401E78745EB1B1&View=%7B2CC9F224-02CB-49B5-9DBB-C97AE29C8572%7D)
- Liquid chromatography/mass spectrometry on [wikipedia](https://en.wikipedia.org/wiki/Liquid_chromatography%E2%80%93mass_spectrometry)
- Introduction to mass spectrometry [playlist](https://www.youtube.com/watch?v=rBymrFzcaPM&list=PL43814409BA85D84C)





