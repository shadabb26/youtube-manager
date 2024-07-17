import sqlite3
connection = sqlite3.connect('youtube_videos.db')

cursor = connection.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    connection.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ?,time = ? WHERE id = ?",(new_name,new_time,video_id))
    connection.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    connection.commit()

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

    connection.close()



if __name__ == "__main__":
    main()
