# kgetParserLib/parser.py
import re
import os
from .utils import get_input_output_files

class FileParser:
    def __init__(self, input_directory, output_directory):
        self.input_directory = input_directory
        self.output_directory = output_directory
    
    def parse_files(self):
        input_files = get_input_output_files(self.input_directory)

        for file_name in input_files:
            self._parse_file(file_name)
    
    def _parse_file(self, file_name):
        input_file_path = os.path.join(self.input_directory, file_name)
        output_file_path = os.path.join(self.output_directory, f"{file_name}_parsed.txt")
        
        with open(output_file_path, "w") as text_file, open(input_file_path, 'r') as file:
            #adding headers to text file
            text_file.write("row#MOClass#MOClassUpdate#MO#parameter#value\n")
            #variables to store different structures
            MO01, MOClass01, MOClassUp = "", "", ""
            struct01flag, struct02flag, struct02Aflag = 0, 0, 0
            parameterPart01_1, parameterPart02_1, parameterPart02A_1 = "", "", ""
            
            for num, line in enumerate(file, 1):
                if line.startswith("=") or line.startswith("Proxy"):
                    continue
                
                MO = re.match(r"MO\s+(SubNetwork=.*),(\w+)=(.*)", line)
                if MO:
                    MO01 = f"{MO.group(1)},{MO.group(2)}={MO.group(3)}"
                    MOClass01 = MO.group(2)
                    MOClassUp = f"{MO.group(2)}={MO.group(3)}"
                    continue
                ######################################################################################################################                
                struct01 = re.match(r"Struct\s+(\w+)\s+has\s+(\d+)\s+members:$", line) # example Struct eNodeBPlmnId has 3 members:
                if struct01:
                    struct01flag = int(struct01.group(2))
                    parameterPart01_1 = struct01.group(1)
                    continue
                
                struct01A = re.match(r"\s+>>>\s+\d+\.(\w+)\s+=\s+(.*)$", line) # example # >>> Struct[1]  has 4 members:
                # >>> 1.mcc = 310	
                # >>> 2.acBarringForSpecialAC = false false false false false
                
                if struct01A and struct01flag > 0:
                    parameterPart01A_2 = struct01A.group(1)
                    value01A = struct01A.group(2)
                    text_file.write(f"{num}#{MOClass01}#{MOClassUp}#{MO01}#{parameterPart01_1}.{parameterPart01A_2}#{value01A}\n")
                    struct01flag -= 1
                    continue
                ######################################################################################################################                  
                struct02 = re.match(r"(\w+)\[(\d+)\]$", line) # example #x2BlackList[64]
                if struct02:
                    struct02flag = int(struct02.group(2))
                    parameterPart02_1 = struct02.group(1)
                    continue
                
                struct02A = re.match(r"\s+>>>\s+Struct\[(\d+)\]\s+has\s+(\d+)\s+members:$", line)
                if struct02A and struct02flag > 0:
                    struct02Aflag = int(struct02A.group(2))
                    parameterPart02A_1 = int(struct02A.group(1))
                    struct02flag -= 1
                    continue
                
                struct02B = re.match(r"\s+>>>\s+\d+\.(\w+)\s+=\s+(.*)$", line)
                if struct02B and struct02Aflag > 0:
                    parameterPart02B_1 = struct02B.group(1)
                    value02B = struct02B.group(2)
                    struct02Aflag -= 1
                    text_file.write(f"{num}#{MOClass01}#{MOClassUp}#{MO01}#{parameterPart02_1}[{parameterPart02A_1}].{parameterPart02B_1}#{value02B}\n")
                    continue
                ######################################################################################################################                  
                temp01 = re.match(r"(\w+)\s+(\w+)", line) or re.match(r"(\w+)\s+(\d+)", line)
                if temp01:
                    parameter = temp01.group(1)
                    value = temp01.group(2)
                    text_file.write(f"{num}#{MOClass01}#{MOClassUp}#{MO01}#{parameter}#{value}\n")
                    continue
                ######################################################################################################################                  
                temp01 = re.match(r"(\w+)\s+-(\d+)", line)
                if temp01:
                    parameter = temp01.group(1)
                    value = temp01.group(2)
                    text_file.write(f"{num}#{MOClass01}#{MOClassUp}#{MO01}#{parameter}#-{value}\n")

        print(f"Parsed {file_name}")

