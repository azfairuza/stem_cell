import stemcell as sc

# read SIMCON.txt

# open file
simcon = sc.readFile('SIMCON')

# get value
iter_simulation = sc.getValue(simcon, 'iteration')
dstlimit = sc.getValue(simcon, 'dstlimit')
savefig = bool(sc.getValue(simcon, 'savefig'))
movespeed = sc.getValue(simcon, 'movespeed')
metadata = sc.getValue(simcon, 'METADATA')


# Read PATCON.txt
# open file
patcon = sc.readFile('PATCON')

# get value
dot_number = sc.getValue(patcon, 'dotnumber')
grid_size = sc.getValue(patcon, 'unitsize')
substrate_size = sc.getValue(patcon, 'subsize')
dot_size = sc.getValue(patcon, 'dotsize')
ligand_position = sc.getValue(patcon,'LIGAND') 

sc.Ligand.resetNumber()
substrate = sc.Nanopattern(substrate_size[0], substrate_size[1], grid_size[0], grid_size[1], ligand_position, dot_size)
substrate.show(True, folder='nanopatern')

print(sc.Ligand.ligand_number)

#Read CELCON.txt

# open file
celcon = sc.readFile('CELCON')

# get value
cell_number = sc.getValue(celcon, 'cellnumber')
integrin_size = sc.getValue(celcon, 'ressize')
integrin_mass = sc.getValue(celcon, 'resmass')
cell_properties = sc.getValue(celcon, 'CELL')

print(cell_properties)

# reset the cell and integrin counter 
sc.Integrin.resetNumber()
sc.Cell.resetNumber()

# build the cell
cells = []
for obj in cell_properties:
    build_cell = sc.Cell(obj[0], obj[1], obj[2], obj[3], obj[4], integrin_size)
    cells.append(build_cell)
    # build_cell.show(substrate)


#print cell and integrin counter

sc.showAll(cells, substrate, show_substrate=True, save=savefig, folder='all', line=True)


# Simulate

sc.simulate1(cells, substrate)

