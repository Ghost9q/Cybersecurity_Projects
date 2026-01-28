from l_func import locate
def main():
    running = True
    print("""---------Welcome to the File Detector---------""")
    while running:
        print()
        print("Enter a file path bellow, eg: C:\\path\\to\\your\\file.jpg|mp4|pdf...")
        file = input("Path to your file (q to quit) ==> : ").strip()
        if file.lower() == "q":
            break
        else:
            try:
                matches = locate(file)
                print()
                print()
                d_matches =  []
                for match in matches:
                    for m1 in matches:
                        if match["sig"] == m1["sig"] and match["des"] != m1["des"]:
                            d_matches.append(match)
                            break

                if matches == []:
                    print("No matches found!!")
                elif  d_matches != []:
                    i  = 1
                    print("---------Multiple matches was found!---------")
                    print()
                    print("""NOTE: If you see your expected file format in the list bellow
that is probably the real file type.
""")
                    for match in d_matches:
                        print(f"""{i}. this file is a ".{match["exten"]}" file
Description: {match["des"]}
Magic number: {match["sig"]}
File Extencion: {match["exten"]}""")
                        i += 1
                        print()

                else:
                    match = matches[-1]
                    print(f"""this file is a ".{match["exten"]}" file
Description: {match["des"]}
Magic number: {match["sig"]}
File Extencion: {match["exten"]}""")
                    print()
            except Exception:
                print()
                print("""AN ERROR ACCURED! PLEASE CHECK THE FOLLOWING:
1. the file path exists. 
2. the spelling is correct.
3. you have access to the file.""")
                print()
                while True:
                    choice = input("try again? (y/n): ").lower().strip()
                    if choice == "n":
                        running = False
                        break
                    elif choice == "y":
                        break
                    else:
                        continue
                    
if __name__ == "__main__":
    main()