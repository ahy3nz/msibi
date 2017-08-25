import argparse
import numpy as np

""" Plot a potential and rdf for a particular step
and particular pair """ 
parser = argparse.ArgumentParser()
parser.add_argument("--step")
parser.add_argument("--first")
parser.add_argument("--second")
parser.add_argument("--save", default=False, action="store_true")
args = parser.parse_args()

import matplotlib
if args.save:
    matplotlib.use('Agg')
import matplotlib.pyplot as plt



target_rdf = np.loadtxt('rdfs/{}-{}-state_A.txt'.format(args.first, args.second))
step_rdf = np.loadtxt('rdfs/pair_{}-{}-state_state-7.500-step{}.txt'.format(
    args.first, args.second, args.step))
step_potential = np.loadtxt('potentials/step{}.pot.{}-{}.txt'.format(args.step,
    args.first, args.second))

fig, axarray = plt.subplots(2,1)
axarray[0].plot(step_rdf[:,0], step_rdf[:,1], label="Step {}".format(args.step))
axarray[0].plot(target_rdf[:,0], target_rdf[:,1], label="Target")
axarray[0].set_xlabel("Distance (nm)")
axarray[0].set_ylabel("RDF")
axarray[0].legend(loc="upper right")

axarray[1].plot(step_potential[:,0], step_potential[:,1], label="Step {}".format(args.step))
axarray[1].set_xlabel("Distance (nm)")
axarray[1].set_ylabel("Energy (kJ/mol)")
axarray[1].set_ylim([-1e2, 1e2])
axarray[1].legend(loc="upper right")

plt.tight_layout()
plt.savefig("{}-{}_step{}.jpg".format(args.first, args.second, args.step), 
        transparent=True)
if not args.save:
    plt.show()
