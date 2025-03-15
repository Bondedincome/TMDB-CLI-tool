import cmd


class MyShell(cmd.Cmd):
    intro = "Welcome to the MyShell. Type help or '?' to list commands."
    prompt = "tmdb-app "
    file = None

    def do_exit(self, arg):
        "Exit the program"
        return True
    
    def do_help(self, arg):
        return super().do_help(arg)
    
    def do_clear(self, arg):
        "Clear the screen"
        print("\033c", end="")
    
    def do_type(self, arg):
        "A command that takes an argument"
        if len(arg) < 3:
            print("Invalid arguments. Usage: type <category>")
            return

        # print(f"You typed: {' '.join(arg)}")
        category = arg[2].lower()
        movie_types = {
            "playing": "The movie is playing.",
            "popular": "The movie is popular.",
            "upcoming": "The movie is upcoming.",
            "top": "The movie is a top-rated movie."
        }
        print(movie_types.get(category, "Unknown movie type."))


        
if __name__ == "__main__":
    MyShell().cmdloop()

    

