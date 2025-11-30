import sys
import os
import shutil
import time

def do_backup(src, dst):
    
    if not os.path.exists(src):
        print("Source folder does not exist")
        return

    if not os.path.exists(dst):
        print("Destination folder does not exist")
        return

    all_files = os.listdir(src)
    
    for f in all_files:
        
        full_src_path = src + "/" + f
        full_dst_path = dst + "/" + f
        
        if os.path.isfile(full_src_path):
            
            if os.path.exists(full_dst_path):
                
                t = str(int(time.time()))
                
                name_parts = os.path.splitext(f)
                new_name = name_parts[0] + "_" + t + name_parts[1]
                
                full_dst_path = dst + "/" + new_name
            
            shutil.copy2(full_src_path, full_dst_path)
            print("Copied " + f)


source_dir = sys.argv[1]
dest_dir = sys.argv[2]

try:
    do_backup(source_dir, dest_dir)
except Exception as e:
    print("Something went wrong")
    print(e)