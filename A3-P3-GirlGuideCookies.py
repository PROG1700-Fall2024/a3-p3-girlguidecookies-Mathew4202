#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:    w0461513 
#Student Name:  Mathew Akunyili
def determinePrize(boxesSold, maxBoxes, avg):
        if boxesSold == maxBoxes and maxBoxes > avg:
            return "Trip to Girl Guide Jamboree in Aruba!"
        elif boxesSold > avg:
            return "Supper Seller Badge"
        elif boxesSold == 0:
            return ""
        else:
            return "Left over cookies"
def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    numberOfGuides = int(input("Enter the number of guides selling cookies: "))
    print("")
    boxes =[]
    numOfBoxes = ""
    guide = []
    nameOfGuide = ""

    for i in range (numberOfGuides):
        nameOfGuide = input(f"Enter the name of guide #{i+1}: ")
        numOfBoxes = int(input("Enter the number of boxes sold by "+ nameOfGuide + ": "))
        print("")
        boxes.append(numOfBoxes)
        guide.append(nameOfGuide)

    avg = sum(boxes) / numberOfGuides

    print(f"The average number of boxes sold by each guide was: {avg:.1f}")
    print("")
    print("Guide          Prizes Won:")
    print("--------------------------")
    for i in range(numberOfGuides):
        prize = determinePrize(boxes[i], max(boxes), avg)
        print(f"{guide[i]:<15} - {prize}")






    # YOUR CODE ENDS HERE

main()