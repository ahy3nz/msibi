from hoomd_script import *

system = init.read_xml(filename='start.xml')

pot_width = 61
table = pair.table(width=pot_width)
table.set_from_file('1', '1', 
        filename='../potentials/pot.t1t1.txt')

T_final = 0.5

all = group.all()
nvt_int = integrate.bdnvt(group=all, T=T_final)
integrate.mode_standard(dt=1e-3)


run(5e3)
output_dcd = dump.dcd(filename='query.dcd', period=1e3, overwrite=True)
run(5e4)

output_xml = dump.xml()
output_xml.set_params(all=True)
output_xml.write(filename='final.xml')
output_pdb = dump.pdb()
output_pdb.write(filename='final.pdb')

