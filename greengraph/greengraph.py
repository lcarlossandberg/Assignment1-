from matplotlib import image as img
from matplotlib import pyplot as plt
import argparse
from graph import Greengraph


def greengraph_parser():
    parser = argparse.ArgumentParser(description = "Finds the number of green pixels between two points.")
    parser.add_argument('--from', dest='start', default='New York', help='Starting point')
    parser.add_argument('--to', dest='end', default='Chicago', help='Ending point')
    parser.add_argument('--steps', default='20', help='Steps between points')
    parser.add_argument('--out', help='File to save to, else display plot')
    
    args=parser.parse_args()
    
    mygraph=Greengraph(args.start, args.end)
    data = mygraph.green_between(args.steps)
    plt.plot(data)
    plt.title("Green pixels from "+args.start+" to "+args.end)
    plt.xlabel("Number of steps")
    plt.ylabel("Amount of green pixels")
    
    if args.out:
        plt.savefig(args.out)
        plt.show()
    else:
        plt.show()




if __name__ == "__main__":
    greengraph_parser()




