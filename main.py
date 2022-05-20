from dirsync import sync
import schedule
import time

# C:\Users\Matei\Desktop\Original
# C:\Users\Matei\Desktop\Replica

# Here the user inputs the path to the 2 folders, one being the source ant the other one being the replica

print("Please write the full path to the folder you want as source!")
source = str(input())

print("Please write the full path to the folder you want as replica!")
replica = str(input())

f = open("data.txt", "a")

print("Please select the time interval you want your folders to sync ( one-way )")
#f.write("Please select the time interval you want your folders to sync ( one-way ) ")
interval = int(input())
f.write(str(interval))

# I defined a function so i could run in the schedule function
def syncron(src, des):
    # Here i made use of the dirsync library, making a one way synchronisation; This function also allows files that dont exist in the source folder get deleted from
    # the replica folder and also create the folder we want as a replica
    sync(src, des, 'sync', purge=True, create=True)


    print("The folder " + source + " was coppied into folder " + replica)

schedule.every(interval).seconds.do(syncron, source, replica)


while True:
    schedule.run_pending()
    time.sleep(1)
