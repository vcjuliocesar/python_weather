import weather

def run():
    while True:
        
        city = input("Enter a city => ")
        weather.get_weater(city)
        answer = input('Do you want to check another city? (yes/no) => ').lower()
        if answer != 'yes':
            print("Bye")
            break
    
if __name__ == '__main__':
    run()