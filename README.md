# OpenBCI_Data_Acquisition
Biomedical Electroencephalography (EEG) signals are the result of measuring the electric potential difference generated on the scalp surface by neural activity corresponding to each brain area. Accurate and automatic detection of neural activity from the upper and lower limbs using EEG may be helpful in rehabilitating people suffering from mobility limitations or disabilities. This article presents a dataset containing 7440 CSV files from 60 test subjects during motor and motor imagery tasks. The motor and motor imagery tasks performed by the test subjects were: Closing Left Hand (CLH), Closing Right Hand (CRH), Dorsal flexion of Left Foot (DLF), Plantar flexion of Left Foot (PLF), Dorsal flexion of Right Foot (DRF), Plantar flexion of Right Foot (PRF) and Resting in between tasks (Rest). The volunteers were recruited from research colleagues at ESPOL and patients at the Luis Vernaza Hospital in Guayaquil, Ecuador. Each CSV file has 501 rows, of which the first one lists the electrodes from 0 to 15, and the remaining 500 rows correspond to 500 data recorded during the task is performed due to sample rate. In addition, each file has 17 columns, of which the first one indicates the sampling number and the remaining 16 columns represent 16 surface EEG electrodes. As a data recording equipment, the OpenBCI is used in a monopolar setup with a sampling rate of 125 Hz. This work includes statistical measures about the demographic information of all recruited test subjects. Finally, we outline the experimental methodology used to record EEG signals during upper and lower limb task execution. This dataset is called MILimbEEG and contains microvolt (µV) EEG signals acquired during motor and motor imagery tasks. The collected data may facilitate the evaluation of EEG signal detection and classification models dedicated to task recognition.

⭐ When using this resource, please cite the original publication:
- [Asanza, V., Lorente-Leyva, L. L., Peluffo-Ordóñez, D. H., Montoya, D., & Gonzalez, K. (2023). MILimbEEG: A dataset of EEG signals related to upper and lower limb execution of motor and motor imagery tasks. Data in Brief, 50, 109540.](https://doi.org/10.1016/j.dib.2023.109540)

## Database for Upper and Lower Limb Task Based on EEG Signals During the Execution of Motor and Motorimagery Tasks
Víctor Asanza, Daniel Montoya, Enrique Peláez, Francis Loayza, Leandro L. Lorente-Leyva, Diego H. Peluffo-Ordóñez and Kleber Gonzalez
- Main Code: https://github.com/Human-Machine-Interface/OpenBCI_Data_Acquisition
- Data Mendeley: http://dx.doi.org/10.17632/w9xfz56txv.1
- More Matlab Examples: https://github.com/Human-Machine-Interface
- Hardware: FM=16 chanels , Cyton + Dasy , Campling Rate = 125 Hz
- Subjects: 24

# Visual Stimuli Used
## Baseline with Eyes Open (BEO)
![Baseline](https://user-images.githubusercontent.com/12642226/134744392-57566b82-94a9-4061-a7fd-289a851e1f42.jpg)

## Close Left Hand (CLH)
![LCH](https://user-images.githubusercontent.com/12642226/134744791-76ab393e-fd8a-4acc-a8aa-619a6767df48.jpg)

## Close Right Hand (CRH)
![RCH](https://user-images.githubusercontent.com/12642226/134744835-ab66fbf9-d89a-4858-a2cc-028ba7ac09a7.jpg)

## Dorsal flexion of Left Foot (DLF)
![LDF](https://user-images.githubusercontent.com/12642226/134744874-8f65537b-806f-41b2-b551-3657274b2250.jpg)

## Plantar flexion of Left Foot (PLF)
![LPF](https://user-images.githubusercontent.com/12642226/134744919-598c95f2-de5e-4a89-96a1-270ad650b5ad.jpg)

## Dorsal flexion of Right Foot (DRF)
![RDF](https://user-images.githubusercontent.com/12642226/134744946-40acf814-d047-4a0c-93cd-95ad033d85e4.jpg)

## Plantar flexion of Right Foot (PRF)
![RPF](https://user-images.githubusercontent.com/12642226/134745001-c03f0464-5450-42d1-855b-91c0d6026497.jpg)

## Rest between the execution (Rest)
![Descanso](https://user-images.githubusercontent.com/12642226/134745058-c8b88ae7-16b0-4dcd-92be-3d19d7a21983.jpg)
