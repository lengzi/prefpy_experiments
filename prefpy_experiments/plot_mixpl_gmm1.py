import sys
import numpy as np
import matplotlib.pyplot as plt


def print_usage(argv0):
    print("USAGE: python3", argv0, "<error description> <error csv filename> <time csv filename> [output png filename]")
    sys.exit()

def plot_error_time_data(str_error_type,          # string, title of the error measure in use
                         error_results,           # error results
                         time_results,            # time results
                         output_img_filename=None # output png filename
                        ):
    # Plot data
    fig = plt.figure(num=1, figsize=(1400/96, 500/96), dpi=96)
    plt.subplot(121)
    plt.title(str_error_type)
    plt.xlabel("n (votes)")
    gmm_line1, = plt.plot(error_results.T[0], error_results.T[1], "bs", label="GMM")

    plt.subplot(122)
    plt.title("Time (seconds)")
    plt.xlabel("n (votes)")
    plt.plot(time_results.T[0], time_results.T[3], "bs", label="GMM")
    momntCalc_line, = plt.plot(time_results.T[0], time_results.T[1], "ro", label="GMM-Moments") # GMM moment value calc time
    optoCalc_line, = plt.plot(time_results.T[0], time_results.T[2], "yd", label="GMM-Opt") # GMM optimization time

    fig.legend([gmm_line1, momntCalc_line, optoCalc_line], ["GMM", "GMM-Moments", "GMM-Opt"], loc="center right")
    if output_img_filename is not None:
        plt.savefig(output_img_filename, dpi=96)
    else:
        plt.show()

def main(argv):
    if len(argv) < 4:
        print("Inavlid number of arguments provided")
        print_usage(argv[0])

    error_type = argv[1] # i.e. "MSE" or "WMSE"

    # Load data from file
    error_results = np.loadtxt(argv[2], delimiter=',')
    time_results = np.loadtxt(argv[3], delimiter=',')

    out_img = None
    if len(argv) >= 5:
        out_img = argv[4]

    plot_error_time_data(str_error_type=error_type,
                         error_results=error_results,
                         time_results=time_results,
                         output_img_filename=out_img
                        )


if __name__ == "__main__":
    main(sys.argv)
