import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            test = json.load(file)
            # print(type(test)) -> <class 'list'> but this file content json list
            return test
    except FileNotFoundError:
        return []
    finally:
        pass

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print("\n")
    print("*"*70)
    for index, video in enumerate(videos,start=1):
        print(f"{index}, Name: {video['name']}, Duration: {video['time']}")
    # print("\n")
    print("*"*70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter viedo time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(video):
    list_all_videos(video)
    index = int(input("Enter video number that will be updated: "))
    if 1 <= index <= len(video):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        video[index-1] = {'name': name, 'time': time}
        save_data_helper(video)
    else:
        print("Invalid index Selected")

def delete_video(video):
    list_all_videos(video)
    index = int(input("Enter the video index that you wants to delete: "))
    if 1 <= index <= len(video):
        del video[index-1]
        save_data_helper(video)
    else:
        print("Invalid index Selected")

# main function
def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager | Choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid input")
                break

# to run this main function we need to do this
if __name__ == "__main__":
    main()