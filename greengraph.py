from matplotlib import image as img
from matplotlib import pyplot as plt
import argparse
from graph import Greengraph


#mygraph=Greengraph('New York','Chicago')
#data = mygraph.green_between(20)
#plt.plot(data)
#plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Finds the number of green pixels between two points.")
    parser.add_argument('--from', dest='start', default='New York', help='Starting point')
    parser.add_argument('--to', dest='end', default='Chicago', help='Ending point')
    parser.add_argument('--steps', default='20', help='Steps between points')
    parser.add_argument('--out', help='File to save to, else display plot')
    
    args=parser.parse_args()

    mygraph=Greengraph(args.start, args.end)
    data = mygraph.green_between(args.steps)
    plt.plot(data)

    if args.out:
        plt.savefig(args.out)
        plt.show()
    else:
        plt.show()




