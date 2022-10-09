## Preflopper

**An app that helps train your preflop ranges in different positions within 6 max poker.**
<img width="800" alt="Screenshot 2022-10-06 at 17 20 57" src="https://user-images.githubusercontent.com/75863764/194367105-ea90d3d0-c17f-42f1-a185-7df0367fd401.png">

## Installation
 **For windows download preflopper zip from the releases section.**
 
 **For mac-os , newest version of mac-os has had problems with creating a disk-image so no executable option like in windows.Python required**
 
 
    
      git clone https://github.com/prawnsup/Preflopper.git #clones directory
      python -m ensurepip #installs pip
      pip install -r REQUIREMENTS.txt
      python main.py
    
      
## Range editing

**By default the ranges are set according to preflop charts from Jonathan Little for 6 max poker.**
<img width="800" alt="Screenshot 2022-10-06 at 13 34 49" src="https://user-images.githubusercontent.com/75863764/194366972-d3d40e86-acc3-4119-ba44-08d9c6342816.png">

**Ranges can be edited after clicking RANGES from the start window. The symbols used are ++ , + , - .**

<img width="1439" alt="Screenshot 2022-10-06 at 13 33 53" src="https://user-images.githubusercontent.com/75863764/194369492-4d915eee-36a5-4475-b69b-90c3ca722b76.png">


**++ : Range includes pair of card specified and pairs of cards vertically above the specified cards according to preflop chart.**

**A8++**

<img width="408" alt="Screenshot 2022-10-06 at 17 30 53" src="https://user-images.githubusercontent.com/75863764/194368415-a6739a77-0d14-440f-be76-5cb4e76037f9.png">

**+ : Range includes pair of cards specified and pairs of card diagnally across to the left from the specified cards.**
**89s+**


<img width="406" alt="Screenshot 2022-10-06 at 17 41 12" src="https://user-images.githubusercontent.com/75863764/194370476-dc70caf8-4d77-4547-b361-2c64bff8c00e.png">

**- : Range includes pair of cards specified and pairs of card horizontally across to the left from the specified cards . **

**A2s-**

<img width="401" alt="Screenshot 2022-10-06 at 17 46 52" src="https://user-images.githubusercontent.com/75863764/194371647-3a9704fb-1af5-4d98-a87f-77d428a82470.png">

## Contributions

**Create a branch , and after making commits just open a pull request :)**

## Future updates

**Add blind vs blind , add preflop raising after RFI , 3-bets and 4-bets. DMG for Mac-os**

**Have fun!**
