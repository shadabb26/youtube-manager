import pymongo
from bson import ObjectId
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["youtubeManager"]
video_collection = db["videos"]

print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"ID:{video['_id']}, Name:{video['name']} and Time:{video['time']}")

def add_video(name,time):
    video_collection.insert_one({
        'name':name,
        'time':time
    })
    
def update_video(video_id,new_name,new_time):
    video_collection.update_one({'_id':ObjectId(video_id)},{'$set':{'name':new_name,'time':new_time}})

def delete_video(video_id):
    video_collection.delete_one({'_id':ObjectId(video_id)})
    

def main():
    while True:
        print("\nYoutube Manager | choose an option")
        print("1. List all youtube Videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice = input("Enter Choice: ")
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter Video Name: ")
            time = input("Enter Video Time: ")
            add_video(name, time)
        elif choice =='3':
            video_id = input("Enter Video ID to update: ")
            name = input("Enter Video Name: ")
            time = input("Enter Video Time: ")
            update_video(video_id,name,time)
        elif choice =='4':
            video_id = input("Enter Video ID to delete: ")
            delete_video(video_id)
        elif choice =='5':
            break
        else:
            print("Invalid Input !")


if __name__ == "__main__":
    main()