# OpenBCI Data Acquisition
EEG signals are collected using OpenBCI, during the execution of motor activities, motor imaging and motion observation!

New version of data acquisition in folder **"AcquisitionProgram_V2.0"** , with two methods.
- Link: https://github.com/vasanza/OpenBCI/tree/main/AcquisitionProgram_V2.0
- Method 1 : Using pyLSL (Library) and OpenBCI_GUI
- Method 2 : Using Brainflow (Library)

Note: Check the path of the images and the folder to save the files

⭐ Explanatory Video of Data Acquisition Codes:
- https://www.youtube.com/watch?v=h6JpvZ4K_Ik

⭐ When using this resource, please cite the original publication:
- [Asanza, V., Lorente-Leyva, L. L., Peluffo-Ordóñez, D. H., Montoya, D., & Gonzalez, K. (2023). MILimbEEG: A dataset of EEG signals related to upper and lower limb execution of motor and motor imagery tasks. Data in Brief, 50, 109540.](https://doi.org/10.1016/j.dib.2023.109540)

# [MILimbEEG](https://data.mendeley.com/datasets/w9xfz56txv/2)
Biomedical Electroencephalography (EEG) signals are the result of measuring the electric potential difference generated on the scalp surface by neural activity corresponding to each brain area. Accurate and automatic detection of neural activity from the upper and lower limbs using EEG may be helpful in rehabilitating people suffering from mobility limitations or disabilities. This article presents a dataset containing 7440 CSV files from 60 test subjects during motor and motor imagery tasks. The motor and motor imagery tasks performed by the test subjects were: Closing Left Hand (CLH), Closing Right Hand (CRH), Dorsal flexion of Left Foot (DLF), Plantar flexion of Left Foot (PLF), Dorsal flexion of Right Foot (DRF), Plantar flexion of Right Foot (PRF) and Resting in between tasks (Rest). The volunteers were recruited from research colleagues at ESPOL and patients at the Luis Vernaza Hospital in Guayaquil, Ecuador. Each CSV file has 501 rows, of which the first one lists the electrodes from 0 to 15, and the remaining 500 rows correspond to 500 data recorded during the task is performed due to sample rate. In addition, each file has 17 columns, of which the first one indicates the sampling number and the remaining 16 columns represent 16 surface EEG electrodes. As a data recording equipment, the OpenBCI is used in a monopolar setup with a sampling rate of 125 Hz. This work includes statistical measures about the demographic information of all recruited test subjects. Finally, we outline the experimental methodology used to record EEG signals during upper and lower limb task execution. This dataset is called MILimbEEG and contains microvolt (µV) EEG signals acquired during motor and motor imagery tasks. The collected data may facilitate the evaluation of EEG signal detection and classification models dedicated to task recognition.

Database for Upper and Lower Limb Task Based on EEG Signals During the Execution of Motor and Motorimagery Tasks
- **Journal**: https://www.sciencedirect.com/science/article/pii/S2352340923006406?via%3Dihub
- Main Code: https://github.com/Human-Machine-Interface/OpenBCI_Data_Acquisition
- Data Mendeley: https://data.mendeley.com/datasets/x8psbz3f6x/2
- More Matlab Examples: https://github.com/Human-Machine-Interface
- Hardware: FM=16 chanels , Cyton + Dasy , Campling Rate = 125 Hz
- Subjects: 60

# Equipment
We use the OpenBCI Cyton + Daisy (www.openbci.com) [1] Biosensing Board for EEG signal recording. The equipment has an active bandpass filter in the 5 to 50 Hz range, additionally, a notch filter at 60 Hz [1]. This non-invasive device operates within a sampling frequency of 125 Hz and has 16 dry electrodes with two ground references, distributed in the international 10–20 system. All 16 EEG electrodes were recorded in monopolar configuration, in which the potential of each electrode is compared with a neutral electrode located in both lobes of the ears [2]. To guarantee the replicability of the EEG signal recording, the international 10/10 system standardized by the AES was used [10]. The distribution of the 16 electrodes is shown in the figure:

![image](https://github.com/user-attachments/assets/0585a66f-c9a4-4255-9215-ce7315257354)

The connections of the electrodes to the Cyton and Dazzy PCBs are as follows:
- [Cyton board](https://docs.openbci.com/Cyton/CytonLanding/)
  - Electrode 1: CH1 (FC5 in 10-10 system EEG)
  - Electrode 2: CH2 (F3 in 10-10 system EEG)
  - Electrode 3: CH3 (FZ in 10-10 system EEG)
  - Electrode 4: CH4 (F4 in 10-10 system EEG)
  - Electrode 5: CH5 (FC5 in 10-10 system EEG)
  - Electrode 6: CH6 (FC1 in 10-10 system EEG)
  - Electrode 7: CH7 (FC2 in 10-10 system EEG)
  - Electrode 8: CH8 (CZ in 10-10 system EEG)
- [Dazzy board](https://docs.openbci.com/GettingStarted/Boards/DaisyGS/)
  - Electrode 9: CH1 (T3 in 10-10 system EEG)
  - Electrode 10: CH2 (CP5 in 10-10 system EEG)
  - Electrode 11: CH3 (C3 in 10-10 system EEG)
  - Electrode 12: CH4 (CP1 in 10-10 system EEG)
  - Electrode 13: CH5 (CP2 in 10-10 system EEG)
  - Electrode 14: CH6 (C4 in 10-10 system EEG)
  - Electrode 15: CH7 (CP6 in 10-10 system EEG)
  - Electrode 16: CH8 (T4 in 10-10 system EEG)
This is summarized in the following image:
![ultracoretex_mark4_nodelocation](https://github.com/user-attachments/assets/a4064d1b-d4b8-4ed7-acdc-b184a2b40fbb)

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
